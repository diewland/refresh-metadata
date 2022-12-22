import sys
from _zonic import refresh_metadata

contract = '0x22C38dc91701AA955F9fA6A95539cDd5043dc2e3'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(contract, from_id, to_id)
