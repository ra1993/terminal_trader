import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'terminal_trader.db')

#volume in lots = 100 shares
#note to self, to delete db and run schema again to make a new one

def schema(db = DBPATH):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()

        cur.execute("""DROP TABLE IF EXISTS account""")
        cur.execute(
        """
                CREATE TABLE account (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                account_num VARCHAR UNIQUE,
                username VARCHAR UNIQUE,
                crypted_password VARCHAR, 
                f_name VARCHAR,
                l_name VARCHAR,
                balance FLOAT,
                api_key VARCHAR
            );""")
        cur.execute("""DROP TABLE IF EXISTS trades""")
        cur.execute(
        """     CREATE TABLE trades(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                account_pk INTEGER,
                time INTEGER,
                ticker VARCHAR,
                price FLOAT,
                volume FLOAT,
                market_value FLOAT,  
                FOREIGN KEY (account_pk) REFERENCES account(pk)
            );""")
        cur.execute("""DROP TABLE IF EXISTS position""")
        cur.execute(
        """
                CREATE TABLE position(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker VARCHAR,
                lots INTEGER,
                account_pk INTEGER,
                FOREIGN KEY (account_pk) REFERENCES account(pk)
            );""")

if __name__ == "__main__":
    schema()