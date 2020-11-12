# Multi-Blockchain-Wallet-in-Python

Here is a univesal wallet built on `HD wallet` that can be used to manage multiple accounts with multiple coins in each account. Instruction, installation requirement and example for using this wallet are as belowed.

## 1. Requirement
Here are packages and tools you need to install before using the wallet.
- HD Wallet. https://github.com/dan-da/hd-wallet-derive#installation-and-running 
-  Python libraries: web3, bit.

## 2. Clone Github
Using Gitbash to clone this repo to your local drive.
- `git clone https://github.com/Khulikaroj/Multi-Blockchain-Wallet-in-Python.git` 

## 3. Setting Mnemonic Phrase
Within wallet directory, create `.env file` (no extension type) to store your mnemonic phrase under an object named `MNEMONIC`.

## 4. Install wallet.py
Within wallet directory, run `wallet.py` in Anaconda Prompt.
- `python wallet.py`

## 5. How to use functions to transfer coins?
To transfer coins, use these functions,
- `create_tx(COIN_NAME,"ADD SENDER ACCOUNT","ADD RECIPIENT ACCOUNT",AMOUNT)`
- `send_tx(COIN_NAME,"ADD SENDER ACCOUNT","ADD RECIPIENT ACCOUNT",AMOUNT)`

## 6. Expand the Wallet!

To expand the account, settint number of accounts need in variable `numderive` in `wallet.py`.

You can add coins into `coins` list in `wallet.py`



