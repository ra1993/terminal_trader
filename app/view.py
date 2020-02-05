def main_menu():

    print("What would you like to do?")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    
    choices = ['1','2', '3']

    if choice not in choices:
        return choice
    else:
        bad_input()

def create_account():

    print("Thank you for making an account, please enter account details!")
    f_name = input("Please enter your first name")
    l_name = input("Please enter your last name")
    user_name = input("Please enter your username")
    password = input("Please enter your password")
    deposit = input("Please state how much you'd like to deposit")

    return user_name, password, f_name, l_name, deposit 


    

def login_menu():
    print("What would you like to do?")
    print("1. Buy")
    print("2. Sell")
    print("3. Trade")
    print("4. Withdraw")
    print("5. Deposit")
    print("6. Balance")
    print("7. View Positions")
    print("8. View Trades")
    print("9. Lookup")
    print("10. Logout")
 
    choices = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']

    if choice not in choices:
        return choice
    else:
        bad_input()



def bad_input():
    print("Invalid Input!")



