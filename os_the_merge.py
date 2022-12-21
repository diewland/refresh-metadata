import sys
from _opensea import refresh_metadata

contract = '0xacfad2b4843af4a1467ce60e4d2a9d965901f15b'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(contract, from_id, to_id)
