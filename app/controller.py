from app.account import Account
from app.trade import Trade
from app.position import Position
from app import view
from app.util import get_price, token #ask about this
import bcrypt

def run():

    while True:
        choice = view.main_menu()

        if choice == '1':
            account_create()
        elif choice == '2':
            user_login()
        elif choice == '3':
            exit(0)

def crypt_password(password):
    #salt = bcrypt.gensalt()
    # hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    hashed_pw = password.encode()
    return hashed_pw

def account_create():
    username, password, f_name, l_name, deposit = view.create_account() #takes all return values from create_account
    crypted_password = crypt_password(password)
    new_account = Account(username = username, crypted_password = crypted_password, f_name = f_name, l_name = l_name, balance = deposit)
    new_account.save()

def user_login():
    username, password = view.user_login() #pass username and password from view.user_login
    user_account = Account.login(username, password) #passes entered username and password to login check in account class
    print(user_account)
    if user_account == False: #checks user
        print("invalid login")
        username, password = view.user_login()
        user_account = Account.login(username, password) #passes username and password to login function in account class
    else:
        print("Welcome: ",user_account.username)
        
        login_loop(user_account)          #if user passes login check will loop to following login menu function
   
def login_loop(user_account):
    while True:
        choice = view.login_menu()
        if choice == '1':
            buy(user_account)
        elif choice == '2':
            sell(user_account)
        elif choice == '3':
            trades(user_account)
        elif choice == '4':
            withdraw(user_account)
        elif choice == '5':
            deposit(user_account)
        elif choice == '6':
            balance(user_account)
        elif choice == '7':
            get_positions(user_account)
        elif choice == '8':
            get_trades(user_account)
        elif choice == '9':
            look_up()
        elif choice == '10':
            logout_exit()

def buy(user_account):
    ticker, quantity = view.buy()
    buy_shares = user_account.buy_shares(ticker, quantity)
 

def sell(user_account):
    ticker, quantity = view.sell()
    sell_shares = user_account.sell_shares(ticker, quantity)
    

def trades():
    pass

def withdraw(user_account):
    amount = view.withdraw()
    if user_account.balance < amount:
        print("Invalid Input")
    else:
        user_account.balance -= amount
        user_account.save()

def deposit():
    amount = view.deposit()
    user_account.balance += amount
    user_account.save()

def balance(user_account):
    #TODO: make a view function do this
    print("Your balance is: ", user_account.balance)

def get_positions(user_account):
    pass

def view_trades(user_account):
    pass

def look_up(): #select_one
    ticker = view.lookup_stock_price()
    price = get_price(ticker, token)
    print(f"The current price for {ticker} is: {price}")
   
def logout_exit():
    print("Thank you for your business. Have a nice day!")
    exit(0)

if __name__ == "__main__":
    run()