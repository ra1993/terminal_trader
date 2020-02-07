import os
from app import Account, Position, Trade, run
#from app import ORM



DIR = os.path.dirname(__file__)
DBFILENAME = "terminal_trader.db"
DBPATH = os.path.join(DIR, 'data', DBFILENAME)



#enter ORM.dbpath = DBPATH


#comment these out when implementing ORM
Account.dbpath = DBPATH
Position.dbpath = DBPATH
Trade.dbpath = DBPATH

run()