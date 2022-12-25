import sys
from _zonic import refresh_metadata

chain = 'optimism'
contract = '0x67709f880F66E15f6aE93b1D737f8d8D9FB9827f'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(chain, contract, from_id, to_id)
