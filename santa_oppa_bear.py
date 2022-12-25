import sys
from _opensea import refresh_metadata

contract = '0x67709f880f66e15f6ae93b1d737f8d8d9fb9827f'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(contract, from_id, to_id)
