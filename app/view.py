def main_menu():

    print("What would you like to do?")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    
    choices = ['1','2', '3']
    choice = input()

    while choice not in choices:
        choice = input("Invalid input, please try again!")
    return choice

def create_account():

    print("Thank you for making an account, please enter account details: ")
    f_name = input("Please enter your first name")
    l_name = input("Please enter your last name")
    user_name = input("Please enter your username")
    password = input("Please enter your password")
    deposit = input("Please state how much you'd like to deposit")

    return user_name, password, f_name, l_name, deposit 

#create account
# def f_name():
#     print("Please enter your first name: ")
#     return input()

# def l_name():
#     print("Please enter your last name: ")
#     return input()

# def username():
#     print("Please enter a new username: ")
#     return input()

# def create_password():
#     password = input("Please enter your password")
#     return password

# def initial_deposit():
#     return("How much would you like to deposit?")

#---------------------------------------------------------------------
def user_login():
    username = input("Please provide username: ")
    password = input("Please provide password: ")
    return username, password

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
    print("9. Lookup Stock Price")
    print("10. Logout")
 
    choices = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    choice = input()
    if choice not in choices:
        bad_input()
    else:
        return choice
        

#----------------------------------Buy
def buy():
    
    ticker = input("Which company would you like to buy stocks from?")
    quantity = input("How many shares would you like to buy? (Buy in lots. 100 = 1 lot)")
  

    return ticker, quantity


#----------------------------------Sell
def sell():
    
    ticker = input("Which company would you like to buy stocks from?")
    quantity = input("How many shares would you like to buy? (Buy in lots. 100 = 1 lot)")
  

    return ticker, quantity


#----------------------------------Trade


#----------------------------------Withdraw
def withdraw():
    amount = input("How much would you like to withdraw? ")
    amount = float(amount)   
    return amount

#----------------------------------Deposit
def deposit():
    deposit = input("How much would you like to deposit? ")

    return deposit

#----------------------------------


#----------------------------------
def lookup_stock_price():
    ticker = input("What stock would you like to look up? (Please enter ticker)")

    return ticker


#bad functions----------------------
def bad_input():
    print("Invalid Input!")
    

def bad_login():
    print("Invalid Login! Please try again!")
    



