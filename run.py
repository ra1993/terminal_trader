# from .controller import run
# from .account import Account 
# from .trade import Trade
# from .position import Position

import os
from app import Account, Position, Trade, run

DIR = os.path.dirname(__file__)
DBFILENAME = "terminal_trader.db"
DBPATH = os.path.join(DIR, 'data', DBFILENAME)

Account.dbpath = DBPATH
Position.dbpath = DBPATH
Trade.dbpath = DBPATH

run()