from unittest import TestCase
from app import Trade




class TestTrade(TestCase):

    def setUp(self):
        print("Setup!!")

    

    def test_trade(self):
        trade = Trade(volume = 30)
        self.assertIsInstance(trade, Trade) #is it a Trade()
        self.assertEqual(trade.volume, 30) #trade.volume == 30
        self.assertIsNone(trade.price) #trade.price is None
        self.assertIsInstance(trade.time, float) # type(trade.time) is a float
        self.assertEqual(trade.tablename, "trades") #trade.tablename == 'trade'

        trade.volume == 30
        trade.price is None
        type(trade.time) == int()
        trade.tablename == "trades"


    # trade = Trade(volume = 30)
    # is it a Trade()
    # trade.volume == 30
    # trade.price is None
    # type(trade.time) == int()