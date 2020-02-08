import sqlite3
import time
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, "./data/terminal_trader.db")

class Trade:
    dbpath = ""
    tablename = "trades"
    
    def __init__(self, pk, account_pk, ticker, volume, price, market_value):
        self.pk = pk
        self.account_pk = account_pk
        self.ticker = ticker
        self.price = price
        self.volume = volume
        self.market_value = market_value
        self.time = time.time()
    
    def save(self):
        if self.pk is None:
            self._insert()
        self._update()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()

            sql = """INSERT INTO {} (account_pk, ticker, volume, price, market_value, time)
                VALUES(?,?,?,?,?,?)""".format(self.tablename)

            values = (self.account_pk, self.ticker, self.volume, self.price, self.market_value, self.time)
            cur.execute(sql, values)

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()

            sql = """UPDATE {} SET account_pk = ?, ticker = ?, volume = ?, price = ?, market_value = ?, time = ?
            WHERE pk = ?;""".format(self.tablename)

            values = (self.account_pk, self.ticker, self.volume, self.price, self.market_value, self.time, self.pk)
            cur.execute(sql, values)

    @classmethod
    def select_all(cls, user_account_pk, ticker = None):
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row 
            cur = conn.cursor()
            if ticker == None:
                sql = """SELECT * FROM {} WHERE account_pk = ?;""".format(cls.tablename)
                cur.execute(sql, (user_account_pk,))
            else:
                sql = """SELECT * FROM {} WHERE account_pk = ? and ticker = ?;""".format(cls.tablename)
                cur.execute(sql, (user_account_pk))

            rows = cur.fetchall()
            return [cls(**row) for row in rows]
 


