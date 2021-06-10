import requests

# First get the non cypto-currencies from the website
govt_currencies = requests.get("https://api.coinbase.com/v2/currencies").json()

# Use list comprehension to generate a list of all the non-cryptos
govt_currencies = [i["id"] for i in govt_currencies["data"]]



# Here we get the list of all Currencies
exchange_rates = requests.get("https://api.coinbase.com/v2/exchange-rates").json()

# Then we need to make a list for the same
crypto_currencies = list(exchange_rates["data"]["rates"].keys())


# Finally we compare the the two above lists to get the crypto currencies
crypto_currencies = [val for val in crypto_currencies if val not in govt_currencies]

#r = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")