import os
from app import Account, Position, Trade, run
#from app import ORM

from app import app as flask_app #renamed to avoid clashing

DIR = os.path.dirname(__file__)
DBFILENAME = "terminal_trader.db"
DBPATH = os.path.join(DIR, 'data', DBFILENAME)


#enter ORM.dbpath = DBPATH


#comment these out when implementing ORM
Account.dbpath = DBPATH
Position.dbpath = DBPATH
Trade.dbpath = DBPATH


#run() #for terminal testing
flask_app.run(debug=True) #for flask testing