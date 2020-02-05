import hashlib
import requests
import json
import bcrypt


#for initializing token object

with open("app/credentials/creds.txt", 'r') as file_object:
    token = file_object.readline()
    
   
# SALT = "lkjhgfdsertyujd2345678765432345".encode()

# def hash_password(password):
#     hashed_pw = hashlib.sha512(password.encode() + SALT).hexdigest()
#     return hashed_pw

def crypt_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def get_price(ticker, token):
    #TODO: get price from IEX Cloud API
    response = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={token}')
    #response = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/batch?token={token}')
    type(response)
    data = response.json()
    #return response #see if response is 200
    #return response.content#to see contents of api
    #print(data)
    return data['latestPrice']

    







