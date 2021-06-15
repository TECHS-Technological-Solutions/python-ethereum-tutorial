from web3 import Web3
from main import settings


def connect_with_infura_provider(url:str='https://mainnet.infura.io/v3/<infura-project-id>') -> Web3:
    w3 = Web3(Web3.HTTPProvider(url))
    return w3


def connect_with_test_provider() -> Web3:
    w3 = Web3(Web3.EthereumTesterProvider())
    return w3



if __name__ == "__main__":
    w3 = connect_with_test_provider()
    pass