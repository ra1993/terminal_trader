from app.account import Account
from app import view
import bcrypt


def main_loop():

    while True:
        choice = view.main_menu()

        if choice == '1':
            view.create_account()

        elif choice == '2':
            #account.login()
            user_login():
        elif choice == '3':
            exit(1)


def crypt_password(password):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password, salt)
    return hashed_pw, salt



def account_create():
    
    #new_account = view.create_account()
    # user_name = view.user_name()
    # password = view.create_password()
    # crypted_password = crypt_password(password)
    # f_name = view.f_name()
    # l_name = view.l_name()
    # deposit = view.initial_deposit()

    username, password, f_name, l_name, deposit = view.create_account() #takes all return values from create_account
    crypted_password, salt = crypt_password(password)
    new_account = Account(None, user_name, crypted_password, f_name, l_name, deposit, salt)

    new_account.save()

def user_login():
    username, password = view.user_login() #passed username and password from view.user_login
    while user_account == False: #checks user
        view.bad_login()
        user_account = Account.login(username, password) #passes username and password to login function in account class
        user = Account.login(username, password)

        if user == True:
            login_loop()          #if user passes login check will loop to following login menu function
        else:
            print("invalid login")
    

# def login_loop():

      
#     while True:
#         choice = view.login_menu():
#         loginaccount = account.Account()
#         if choice == '1':
#             loginaccount.buy()
#         elif choice == '2':
#             loginaccount.sell()
#         elif choice == '3':
#             #loginaccount.get_trades()
#         elif choice == '4':
#             loginaccount.withdraw()
#         elif choice == '5':
#             loginaccount.deposit()
#         # elif choice == '6':
#         #     loginaccount.balance()
#         elif choice == '7':
#             loginaccount.get_positions()
#         elif choice == '8':
#             loginaccount.get_trades()
#         elif choice == '9':
#             loginaccount.select_one_where()
#         elif choice == '10':
#             exit(1)




if __name__ == "__main__":
    main_loop()