import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.load(open('abi.json'))
bytecode = '6060604052341561000c57fe5b5b604060405190810160405280600481526020017f416d616e0000000000000000000000000000000000000000000000000000000081525060019080519060200190610059929190610060565b505b610105565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a157805160ff19168380011785556100cf565b828001600101855582156100cf579182015b828111156100ce5782518255916020019190600101906100b3565b5b5090506100dc91906100e0565b5090565b61010291905b808211156100fe5760008160009055506001016100e6565b5090565b90565b61039a806101146000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806341c0e1b514610051578063a413686214610063578063cfae3217146100bd575bfe5b341561005957fe5b610061610156565b005b341561006b57fe5b6100bb600480803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919050506101f1565b005b34156100c557fe5b6100cd61020c565b604051808060200182810382528381815181526020019150805190602001908083836000831461011c575b80518252602083111561011c576020820191506020810190506020830392506100f8565b505050905090810190601f1680156101485780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3373ffffffffffffffffffffffffffffffffffffffff16600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415156101b35760006000fd5b600060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b5b565b80600190805190602001906102079291906102b5565b505b50565b610214610335565b60018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102aa5780601f1061027f576101008083540402835291602001916102aa565b820191906000526020600020905b81548152906001019060200180831161028d57829003601f168201915b505050505090505b90565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106102f657805160ff1916838001178555610324565b82800160010185558215610324579182015b82811115610323578251825591602001919060010190610308565b5b5090506103319190610349565b5090565b602060405190810160405280600081525090565b61036b91905b8082111561036757600081600090555060010161034f565b5090565b905600a165627a7a723058207988271be842d15027a517df223322d3322929a919c7e8801241ac79dfd7f93b0029'

# print(abi)
Greeter = web3.eth.contract(bytecode=bytecode,abi=abi)
tx_hash = Greeter.constructor().transact()
print(tx_hash)

# Waiting for block to be mined and get receipt
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)

contract = web3.eth.contract(
    address = tx_receipt.contractAddress,
    abi = abi
)
print(contract.functions.greet().call())