import sqlite3
import os
from .util import get_price

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, "terminal_trader.db")


class Position:
    dbpath = ""
    tablename = "position"

    def __init__(self, pk, ticker, lots, account_pk):
        self.pk = pk
        self.ticker = ticker
        self.lots = lots
        self.account_pk = account_pk


    def save(self):     #saves file
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """
            INSERT INTO {} (ticker, lots, account_pk)

            VALUES(?,?,?);
            """.format(self.tablename)

            values = (self.ticker, self.lots, self.account_pk)
            cur.execute(sql, values)


    def _update(self):

        with sqlite3.connect(self.dbpath) as conn:
            cur = conn.cursor()
            sql = """UPDATE {} SET
                    ticker = ?, lots = ?, account_pk = ?
                    WHERE pk = ?;
            """.format(self.tablename)
            values = (self.ticker, self.lots, self.account_pk, self.pk)
            cur.execute(sql, values)

    @classmethod
    def select_one(cls, ticker, user_account_pk):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE account_pk = ? AND ticker = ?"""
            cur.execute(sql, (user_account_pk, ticker))
            position = cur.fetchone()

            if not position:
                return None
            position = cls(**position)
            return position

    @classmethod
    def select_all(cls, user_account_pk):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            sql = """SELECT * FROM {} WHERE account_pk = ?;""".format(cls.tablename)
            cur.execute(sql, (user_account_pk,))

            rows = cur.fetchall()
            return [cls(**row) for row in rows]


    def __repr__(self):
        return f"<{self.pk}, {self.ticker}>"
            