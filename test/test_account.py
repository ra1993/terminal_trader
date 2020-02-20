import unittest
from .account import Account
import sqlite3

class TestAccount(unittest.TestCase):
    DIR = os.path.dirname(__file__)
    DBPATH = os.path.join(DIR, 'test_terminal_trader.db')
    tablename = "account"

    @classmethod
    def setUpClass(cls):
         #need to create test db
        cls.test_db(DBPATH)

    @classmethod
    def tearDownClass(cls):
        #tears down test db
        cls.test_db(DBPATH)

    def setUp(self): #runs before every test
        #need to create test db

        #creating test users
        self.user_1 = Account(None, None, "OreoAhoy", "1234", "Oreoo", "Ahoyyy", 900000, None)
        self.user_2 = Account(None, None, "NachoSalsa", "1234", "Nacho", "Salsa", 15000000, None)
        

    def tearDown(self): #runs after every test to delete newly created users
        self.user_1
        self.user_2

    def test_api_key(self):
        #test set api_key
        self.assertEqual(self.user_1.generate_api_key())
        self.assertEqual(self.user_2.generate_api_key())


    #creates test db
    def test_db(cls):
        with sqlite3.connect(db=DBPATH) as conn:
            cur = conn.cursor()

            cur.execute("""DROP TABLE IF EXISTS {tablename}""")
            cur.execute(
            """
                    CREATE TABLE {tablename} (
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_num VARCHAR UNIQUE,
                    username VARCHAR UNIQUE,
                    crypted_password VARCHAR, 
                    f_name VARCHAR,
                    l_name VARCHAR,
                    balance FLOAT,
                    api_key VARCHAR
                );""")


if __name__ == "__main__":
    unittest.main()
