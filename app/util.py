import hashlib
import requests
import json
import bcrypt
import pandas as pd
# import numpy as np
# import plotly.express as px


#for initializing token object

with open("/home/richarda/Projects/terminal_trader/app/credentials/creds.txt", 'r') as file_object:
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

#TODO new feature work on getting historical stock data, then build chart

def historical_chart(ticker, token, year):
    # response = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/chart/{year}?token={token}')
    # data = response.json()
    data = pd.read_json(f'https://cloud.iexapis.com/stable/stock/{ticker}/chart/{year}?token={token}')

    # data.head(3) #first 3 rows
    # data.tail(3) #last 3 rows
    date_data = data['date']
    price_data = data['high']
    
    #return type(response)
    return date_data, price_data

def graph_data(ticker, token, year):
    time, price = historical_chart(ticker, token, year)

    x = time
    y = price

    fig = px.line(x="Time", y="Price")
    fig.show()
    # plt.xlabel('Time')
    # plt.ylabel('Price')
    # plt.title('Stock Price Over Time')

    # plt.figsize(16,10)
    # plt.plot(time, price)
    # plt.show()

    # plt.rcParams["figure.figsize"] = (30,5)
    # plt.figure
    # my_plot = x, y.plot(kind='time series plot', color = 'yellow')
    # return plt.figure 
    


#print(historical_chart("aapl", token, '1y'))
#print(graph_data("aapl", token, '1y'))



    


    







