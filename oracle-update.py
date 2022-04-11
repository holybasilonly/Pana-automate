from web3 import Web3

w3 = Web3(Web3.HTTPProvider(
    'https://arbitrum-rinkeby.infura.io/v3/ca086b5ab8cd4572b6e72621e836363f'))

def update():
    if (w3.isConnected()):
        # automate update task
        address = '0x69AB7266FF0db1564A57c8855fBc75A8A13C2B95'
        abi = '[ { "inputs": [ { "internalType": "address", "name": "factory_", "type": "address" }, { "internalType": "uint256", "name": "windowSize_", "type": "uint256" }, { "internalType": "uint8", "name": "granularity_", "type": "uint8" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "tokenIn", "type": "address" }, { "internalType": "uint256", "name": "amountIn", "type": "uint256" }, { "internalType": "address", "name": "tokenOut", "type": "address" } ], "name": "consult", "outputs": [ { "internalType": "uint256", "name": "amountOut", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "factory", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "granularity", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "timestamp", "type": "uint256" } ], "name": "observationIndexOf", "outputs": [ { "internalType": "uint8", "name": "index", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "pairObservations", "outputs": [ { "internalType": "uint256", "name": "timestamp", "type": "uint256" }, { "internalType": "uint256", "name": "price0Cumulative", "type": "uint256" }, { "internalType": "uint256", "name": "price1Cumulative", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "periodSize", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "tokenA", "type": "address" }, { "internalType": "address", "name": "tokenB", "type": "address" } ], "name": "update", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "windowSize", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" } ]'
        contract_instance = w3.eth.contract(address=address, abi=abi)
        build_tx = contract_instance.functions.update('0x327459343E34F4c2Cc3fE6678ea8cA3Cf22fBfC8', '0x40D18617Af5D891499381eC6a42c959E4423E1bf').buildTransaction(
            {
                'value': '0',
                'from': '0x914f32397c264020142359BDe032734AF40ea4F6',
                'nonce': w3.eth.get_transaction_count(address),
                'maxFeePerGas': 2000000000, 'maxPriorityFeePerGas': 1000000000
            }
        )
        build_tx['data']

        signed_txn = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count('0x914f32397c264020142359BDe032734AF40ea4F6'),
            # maxFeePerGas=2000000000,
            # maxPriorityFeePerGas=1000000000,
            gasPrice=800000000000,
            gas=210000000,
            to=address,
            value=0,
            data= build_tx['data'],
            # (optional) the type is now implicitly set based on appropriate transaction params
            # type=2,
            chainId=w3.eth.chainId,
        ),
            '88c486eacbd0b0d439d1a55ec4949aa811087af6ff981068ec6035e5e266b253',
        )

        print("====== RAW TX ==========")
        print(signed_txn.rawTransaction)
        print("====== RAW TX ==========")

        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(tx_hash)
        # print(contract_instance.functions.factory().call())
    else:
        print("connection issue on web3")
