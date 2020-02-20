from flask import Flask, render_template, request, redirect, session, jsonify, flash, url_for
# from form import RegistrationForm, Login
import time
import random
from app.account import Account
from app.trade import Trade
from app.position import Position
# from app import view
from app.util import get_price, token #ask about this
import bcrypt
import string

dbpath = "./data/terminal_trader.db"

app = Flask(__name__)

#generates secret key
key = string.digits + string.ascii_letters
app.secret_key = ''.join([random.choice(key) for i in range(20)])
app.secret_key = str(app.secret_key)

#encrypts password
def crypt_password(password):
    #salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #hashed_pw = password.encode()
    return hashed_pw
#-----------------------------------------------------------------------------
#homepage
@app.route('/')
@app.route('/home', methods=["GET"])
def home():
    
    return render_template("homepage.html") or render_template("/")


#create account
@app.route('/create_account', methods=["GET", "POST"])
def create_account():

    error_message = "There was an error creating your account! Please enter your details again."
    if request.method == "GET":
        return render_template("create_account.html")

    if request.method == "POST": #pass values from html file when form is submitted
        username = request.form.get('username')
        password = request.form.get('password')
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        balance = request.form.get('balance')
        crypted_password = crypt_password(password) #gets user pw and encrypts it
        
    new_account = Account(username = username, crypted_password = crypted_password, f_name = f_name, l_name = l_name, balance = balance)

    try:
        new_account.save()
        print("Thanks for joining our family!", new_account.username)
    except:
        time.sleep(5)
        return redirect("create_account.html", error = error_message)
    finally: 
        return redirect("/home")

#login function
@app.route('/login', methods=["GET", "POST"])
def login():

    error_message = "Error: Invalid Credentials!"
    if request.method == "GET":
        return render_template("login.html")
   
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
       
        try:
            user_account = Account.login(username, password)
            session['user_account'] = user_account.pk
        except:
            if user_account == False:
                print("Invalid user credentials")
                return render_template("/login.html")
        else:
            # session['user_account'] = user_account.pk
            return render_template("/loggedin_menu.html/", user_account = session)

        # session['user_account'] = user_account.pk
        # return render_template("/loggedin_menu.html/", user_account = session)
        # # print("user_account success!", user_account.username)
        # if user_account == False:
        # #if session == None:
        #     print("invalid login!")
        #     return redirect("login.html")
        # else:
        # return render_template("/loggedin_menu.html/", user_account = session)
       
          


# @app.route('/loggedin_menu', methods=["GET"])
@app.route('/loggedin_menu/<user_account>', methods = ["GET", "POST"])
def loggedin_menu(user_account):
    print(user_account)
    return render_template("loggedin_menu.html")

    if request.method == "GET":
        render_template("logout.html", user_account)


#-----------------------------------logout
@app.route('/logout/<user_account>', methods = ["GET", "POST"])
def logout(user_account):
    print("Thank you for your business!")

    if request.method == "GET":
        time.sleep(5)
    return render_template("logout.html", username = user_account.username)

if __name__ == "__main__":
    app.run(debug=True)