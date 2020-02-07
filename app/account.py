import random
import sqlite3
from .util import get_price, crypt_password
from .position import Position
from .trade import Trade
import bcrypt
#from app import ORM


class Account:

    tablename = "account"
    dbpath = "./data/terminal_trader.db"
  
    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.account_num = str(random.randint(100000000000, 999999999999))
        self.username = kwargs.get("username")
        self.crypted_password = kwargs.get("crypted_password")
        self.f_name = kwargs.get("f_name")
        self.l_name = kwargs.get("l_name")
        self.balance = kwargs.get('balance')
               

    def save(self):     #saves file
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """
            INSERT INTO {} (account_num, username, crypted_password, f_name, l_name,  balance)
            VALUES(?,?,?,?,?,?);
            """.format(self.tablename)

            values = (self.account_num, self.username, self.crypted_password, self.f_name, self.l_name, self.balance)
            cur.execute(sql, values)
            

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """UPDATE {} SET
                     username = ?, f_name = ?, l_name = ?, crypted_password = ?, balance = ?,
                     WHERE pk = ?;
            """.format(self.tablename)
            values = (self.username, self.crypted_password, self.f_name, self.l_name, self.balance, self.pk)

    @classmethod
    def select_one(cls, pk):
        #selects one entry from the database
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            sql = f"""SELECT * FROM {cls.tablename} WHERE pk =?;"""
            cur.execute(sql, (pk,))
            row = cur.fetchone()
            return cls(**row)

    @classmethod
    def login(cls, username, password):

        # return cls.select_one_where("WHERE username=? AND password=?", username, crypted_password)
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            sql= f"""SELECT * FROM {cls.tablename} WHERE username == ?
            """
            cur.execute(sql, (username,)) 
            row = cur.fetchone()
            
            if row is None:
                return False
            print("Inside login classmethod: ", row)
            user_account = cls(**row)
 
            if not bcrypt.checkpw(password.encode(), user_account.crypted_password): #checking password against crypt password
                return False
            else:
                return user_account

        #When the user logs in, and is prompted what todo
        #if username doesnt equal username in database
        
       
    def buy(self, ticker, quantity):
        """checks if ticker exists and if sufficient funds exist for this user"""
        """create a new trade and modify a position as well as user's balance. returns nothing"""

        if self.balance < market_value:
            return False
        
        ticker = ticker.upper() #capitalizes the ticker
        position = Position.select_one(ticker)
        if position == False:
            position = Position(None, ticker, shares, self.pk)
        else:
            position.shares += shares
        
        #save our user instance
        pass

    # def sell(self, ticker, quantity):
    #     """make a sale. checks if a stock exists in user's positions and has sufficient shares and creates a new trade"""
    #    """and modfies the position as well as adding to the user's balance. returns nothing""" 
    #     pass

    # def select_one_where(cls, where_clause, values = tuple{}):
    #     pass

    
    # def get_positions(self):
    #     #returns a list of position objects/tuple
    #     return Position.select_all("WHERE account_pk=?", {self.pk,})

    # def get_trades(self):
    #     return Trade.select_all("WHERE account_pk=?", {self.pk,})

    # def get_position_for(self, ticker):
    #     return Position.select_one("WHERE account_pk=? AND ticker =?", (self.pk, ticker))


