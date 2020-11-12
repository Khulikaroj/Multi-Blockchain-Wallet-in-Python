import os
import subprocess
import json
from constant import *
from dotenv import load_dotenv
load_dotenv()
from eth_account import Account
from web3 import Web3
from web3.middleware import geth_poa_middleware
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

mnemonic = os.getenv('MNEMONIC')
coins = {"eth","btc-test"}
numderives = 3

#Derive Wallet
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    keys = json.loads(output)
    return  keys

keys = {}
for coin in coins:
    keys[coin]= derive_wallets(mnemonic, coin, numderive=2)

#priv_key_to_account function
eth_PrivateKey = keys["eth"][0]['privkey']
btc_PrivateKey = keys['btc-test'][0]['privkey']
print(json.dumps(eth_PrivateKey, indent=4, sort_keys=True))
print(json.dumps(btc_PrivateKey, indent=4, sort_keys=True))

def priv_key_to_account(coin,key):
    print(coin)
    print(key)
    if coin == ETH:
        return Account.privateKeyToAccount(key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(key)

#create_tx function
def create_tx(coin,account, recipient, amount):
    if coin == ETH: 
        gasEstimate = w3.eth.estimateGas({"from":eth_acc.address, "to":recipient, "value": amount})
        return { 
            "from": eth_acc.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(eth_acc.address)
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])

#send_tx function
def send_tx(coin,account,recipient, amount):
    tx = create_tx(coin, account, recipient, amount)
    if coin == ETH:
        signed_tx = eth_acc.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    elif coin == BTCTEST:
        tx_btctest = create_tx(coin, account, recipient, amount)
        signed_tx = account.sign_transaction(tx)
        print(signed_tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)

#create account
eth_acc = priv_key_to_account(ETH, eth_PrivateKey)
btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)

#send BTC-test 
create_tx(BTCTEST,btc_acc,"mjCdMZyGzYSE7gCHN7DomFfxysqsTXpGyH", 0.000000001)
send_tx(BTCTEST,btc_acc,"mjCdMZyGzYSE7gCHN7DomFfxysqsTXpGyH", 0.000000001)

#send ETH
create_tx(ETH,eth_acc,"0x8B63736c9D91adeE61c9e773E9986bf76457Ea3a", 0.00001)
send_tx(ETH,eth_acc,"0x8B63736c9D91adeE61c9e773E9986bf76457Ea3a", 0.00001)
