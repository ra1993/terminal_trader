from app.account import Account
from app import view
import bcrypt


def run():

    while True:
        choice = view.main_menu()

        if choice == '1':
            #view.create_account()
            account_create()

        elif choice == '2':
            #account.login()
            user_login()
        elif choice == '3':
            exit(0)


def crypt_password(password):
    #salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pw



def account_create():
    # view.create_account()
    #new_account = view.create_account()
    # user_name = view.user_name()
    # password = view.create_password()
    # crypted_password = crypt_password(password)
    # f_name = view.f_name()
    # l_name = view.l_name()
    # deposit = view.initial_deposit()

    username, password, f_name, l_name, deposit = view.create_account() #takes all return values from create_account
    crypted_password = crypt_password(password)
    new_account = Account(username = username, crypted_password = crypted_password, f_name = f_name, l_name = l_name, balance = deposit)
    new_account.save()

def user_login():
    username, password = view.user_login() #pass username and password from view.user_login
    
    user_account = Account.login(username, password) #passes entered username and password to login check in account class
    
    if user_account == False: #checks user
        print("invalid login")
        username, password = view.user_login()
        user_account = Account.login(username, password) #passes username and password to login function in account class
    else:
        login_loop()          #if user passes login check will loop to following login menu function


    

def login_loop():

   
    while True:
        choice = view.login_menu()
        if choice == '1':
            buy()
        elif choice == '2':
            sell()
        elif choice == '3':
            trades()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            deposit()
        elif choice == '6':
            balance()
        elif choice == '7':
            get_positions()
        elif choice == '8':
            get_trades()
        elif choice == '9':
            look_up()
        elif choice == '10':
            logout_exit()

def buy():
    ticker, quantity = view.buy()


def sell():
    ticker, quantity = view.sell()


def trades():
    pass


def withdraw():
    pass

def deposit():
    pass


def balance():
    pass

def get_positions():
    pass

def view_trades():
    pass

def look_up(): #select_one
    pass

def logout_exit():
    print("Thank you for your business. Have a nice day!")
    exit(0)

if __name__ == "__main__":
    run()