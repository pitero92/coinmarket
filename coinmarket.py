import requests
import json

while True:
    #URL
    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

    #Get data
    request = requests.get(globalURL)
    data = request.json()
    globalCoinMarket = data["total_market_cap_usd"]

    #Menu
    print()
    print("Coinmarketcap.com price checker")
    print("TOTAL MARKETCAP: $" + str(globalCoinMarket))
    choice = input("Enter name of cryptocurrency to see a price (to see all type \"all\"): ")
    print()
    
    if choice == "all":
        request = requests.get(tickerURL)
        data = request.json()

        for currency in data:
            ticker = currency['symbol']
            price = currency['price_usd']

            print(symbol + ":\t\t$" + price)
        print()

    else:
        tickerURL += "/" + choice + "/"
        request = requests.get(tickerURL)
        data = request.json()

        ticker = data[0]['symbol']
        price = data[0]['price_usd']

        print(ticker + ":\t\t$" + price)
        print()

    secondChoice = input("Another check? (y/n): ")
    if secondChoice == "y":
        continue
    elif secondChoice == "n":
        break
    else:
        print("Wrong answer!")