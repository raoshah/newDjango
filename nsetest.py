from nsetools import Nse
from pprint import pprint
nse = Nse()
q = nse.get_index_quote("nifty 50")
pprint(q)
