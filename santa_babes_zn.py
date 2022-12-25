import sys
from _zonic import refresh_metadata

chain = 'arbitrum_one'
contract = '0x890e631A8466377F45CBc32eF02E6ec51f176ad7'

[from_id, to_id] = [ int(id) for id in sys.argv[1:] ]
refresh_metadata(chain, contract, from_id, to_id)
