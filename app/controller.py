import account
import view

def login_loop():
    while True:
        choice = view.login_menu():
        loginaccount = account.Account()

        if choice == '1':
            loginaccount.buy()
        elif choice == '2':
            loginaccount.sell()
        elif choice == '3':
            #loginaccount.get_trades()
        elif choice == '4':
            loginaccount.withdraw()
        elif choice == '5':
            loginaccount.deposit()
        # elif choice == '6':
        #     loginaccount.balance()
        elif choice == '7':
            loginaccount.get_positions()
        elif choice == '8':
            loginaccount.get_trades()
        elif choice == '9':
            loginaccount.select_one_where()
        elif choice == '10':
            exit(1)


def main_loop():

    while True:
        choice = view.main_menu()
        account = account.Account()

        if choice == '1':
            account.create_account()
        elif choice == '2':
            login_loop()
            account.login()
        elif choice == '3':
            exit(1)

        
            



if __name__ == "__main__":
    run()