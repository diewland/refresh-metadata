import sys
from _opensea import refresh_metadata

contract = '0x75c8b866ac237a689bdbc1557e9dc0bd90200ed4'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(contract, from_id, to_id)
