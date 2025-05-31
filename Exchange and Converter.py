import requests, sys

API_KEY = 'enter API here'    #API token from https://www.freecurrencyapi.com
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["EUR","USD","JPY","BGN","CZK","DKK","GBP","HUF","PLN","RON","SEK","CHF","ISK","NOK","HRK","RUB","TRY",
              "AUD","BRL","CAD","CNY","HKD","IDR","ILS","INR","KRW","MXN","MYR","NZD","PHP","SGD","THB","ZAR"]

def convert_currency(base): #Gets data from online database based on a currency
    curr=','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={curr}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
    
    
    
def inputs():   #Ensures correct values are inserted with the option to quit on steps 1 and 2
    while True:
        a = input('Select the currency you want to exchance from (press q for quit): ').upper() #accepts both capital and lowercase curr
        if a =="Q":
            sys.exit()
        else:
            if a in CURRENCIES:
                break
            else:
                print("insert correct type of currency from this list: EUR,USD,JPY,BGN,CZK,DKK,GBP,HUF,PLN,RON,SEK,CHF,ISK,NOK,HRK,RUB,TRY,AUD,BRL,CAD,CNY,HKD,IDR,ILS,INR,KRW,MXN,MYR,NZD,PHP,SGD,THB,ZAR")
        
    while True:
        b = input('Select the currency you want to exchance to (press q for quit): ').upper()  #accepts both capital and lowercase curr
        if b == "Q":
            sys.exit()
        else:
            if b in CURRENCIES:
                break
            else:
                print("insert correct type of currency from this list: EUR,USD,JPY,BGN,CZK,DKK,GBP,HUF,PLN,RON,SEK,CHF,ISK,NOK,HRK,RUB,TRY,AUD,BRL,CAD,CNY,HKD,IDR,ILS,INR,KRW,MXN,MYR,NZD,PHP,SGD,THB,ZAR")
        
    while True:
        try:
            amount = abs(float(input('Select the amount you are looking for in the form of integer or floating number: '))) #converts to a floating, positive number in case neg num is given.
            break
        except ValueError:
            continue
    
            
    return a, b, amount
            
def convert_between_currencies(a,b, amount, data): #Displays current exchange rates pulled from the database, omitting the one you asked for (it will always show as 1) - and also convverts the value of interest, to the currency of interest
    while True:
        try:
            conversion= data[b] * amount
            print("\nCurrent exchange rates:")
            for k,v in data.items():
                if k == a:
                    continue
                else:
                    print(f"{k} : {v}")
            print(f"\nThe conversion value from {a} to {b} for the amount: {amount:,} is : {conversion:,.2f}")
            break
        except (TypeError, ValueError):
            print("please insert correct values")
            sys.exit()


a,b,amount = inputs()
data= convert_currency(a)
convert_between_currencies(a,b, amount, data)
