import requests
from colorama import init as color_init
color_init()

# First get the non cypto-currencies from the website
govt_currencies = requests.get("https://api.coinbase.com/v2/currencies").json()

# Use list comprehension to generate a list of all the non-cryptos
govt_currencies = [i["id"] for i in govt_currencies["data"]]


# Here we get the list of all Currencies
exchange_rates = requests.get(
    "https://api.coinbase.com/v2/exchange-rates").json()

# Then we need to make a list for the same
crypto_currencies = list(exchange_rates["data"]["rates"].keys())


# Finally we compare the the two above lists to get the crypto currencies
crypto_currencies = [
    val for val in crypto_currencies if val not in govt_currencies]

#r = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")


def get_price(crypto, base):
    ''' Get the current price of the [crypto-currencies] 
        in terms of the physical currency specified '''

    #if crypto in crypto_currencies and base in govt_currencies:
    curr_conv_code = crypto + "-" + base
    get_url = "https://api.coinbase.com/v2/prices/" + curr_conv_code + "/buy"
    r = requests.get(get_url).json()
    print("1 \x1b[1;31;40m{base}\x1b[0m costs \x1b[0;34;40m{amount}\x1b[0m \x1b[1;32;40m{currency}\x1b[0m"\
        .format(base=r["data"]["base"], amount=r["data"]["amount"], currency=r["data"]["currency"]))
    

'''crp = input("Enter crypto")
bas = input("ENter bas")

get_price(crp, bas)'''
get_price("ETH","USD")