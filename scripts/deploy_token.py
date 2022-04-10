from brownie import OurToken, network, config
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3
import time

def deploy_token():
    account = get_account()
    print("Deployed token!")
    our_token = OurToken.deploy(
        1000000000000000000000,
        {"from":account}
    )
    print("Deployed token!")

    print("balance of account is " + str(our_token.balanceOf(account)))

    return our_token


def main():
    deploy_token()