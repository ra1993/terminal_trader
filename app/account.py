import random
import sqlite3
from .util import get_price, crypt_password
from .position import Position
from .trade import Trade
import bcrypt


class Account:

    tablename = "account"
    dbpath = "./data/terminal_trader.db"
  
    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.account_num = str(random.randint(100000000000, 999999999999))
        self.username = kwargs.get("username")
        self.crypt_password = kwargs.get("crypt_password")
        self.f_name = kwargs.get("f_name")
        self.l_name = kwargs.get("l_name")
        self.balance = kwargs.get('balance')
        self.salt = kwargs.get("salt")
        

    def save(self):     #saves file
        if self.pk is None:
            self._insert()
        else:
            self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """
            INSERT INTO {} (account_num, username, f_name, l_name, password, balance, salt)
            VALUES(?,?,?,?,?,?);
            """.format(self.tablename)

            values = (self.account_num, self.username, self.password, self.f_name, self.l_name, self.balance, self.salt)
            cur.execute(sql, values)
            

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """UPDATE {} SET
                     username = ?, f_name = ?, l_name = ?, password = ?, balance = ?, salt = ?,
                     WHERE pk = ?;
            """.format(self.tablename)
            values = (self.username, self.password, self.f_name, self.l_name, self.balance, self.pk, self.salt)



    # @classmethod
    # def login(cls, username, password):
        
    def login(cls, username, password):

        return cls.select_one_where("WHERE username=? AND password=?", username, crypt_password)
        with sqlite3.connect(cls.dbpath) as conn:
            cur = conn.cursor()
            sql= f"""SELECT * FROM {cls.tablename} WHERE username == ?
            """
            cur.execute(sql, (username,)) 
            user_account = cur.fetchall()

            if len(user_account) == 0:
                return False

            conn.row_factory = sqlite.Row
            cur = conn.cursor()
            cur.execute(sql,(username,))
            user_account = cur.fetchone()
            user_account = cls(**user_account)

            if not bcrypt.checkpw(password, user_account.crypt_password): #checking password against crypt password
                return False
            else:
                return user.account

        #When the user logs in, and is prompted what todo
        #if username doesnt equal username in database
        
       
    # def buy(self, ticker, quantity):
    #     """checks if ticker exists and if sufficient funds exist for this user"""
    #     """create a new trade and modify a position as well as user's balance. returns nothing"""
    #     #save our user instance
    #     pass

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


