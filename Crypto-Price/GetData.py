import requests
from colorama import init as color_init, Fore
color_init()

# First get the non cypto-currencies from the website
fiat = requests.get("https://api.coinbase.com/v2/currencies").json()

# Use list comprehension to generate a list of all the non-cryptos
fiat = [i["id"] for i in fiat["data"]]


# Here we get the list of all Currencies
exchange_rates = requests.get(
    "https://api.coinbase.com/v2/exchange-rates").json()

# Then we need to make a list for the same
crypto_currencies = list(exchange_rates["data"]["rates"].keys())


# Finally we compare the the two above lists to get the crypto currencies
crypto_currencies = [
    val for val in crypto_currencies if val not in fiat]

#r = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")


def get_price(crypto, base):
    ''' Get the current price of the [crypto-currencies] \
        in terms of the physical currency specified '''

    # if crypto in crypto_currencies and base in fiat:
    if crypto in crypto_currencies and base in fiat:
        curr_conv_code = crypto + "-" + base
    
        get_url = "https://api.coinbase.com/v2/prices/" + curr_conv_code + "/buy"
        r = requests.get(get_url).json()
    
        print("1 {red}{base}{rst} costs {blue}{amount}{rst} {green}{currency}{rst}"
            .format(rst=Fore.RESET, red=Fore.LIGHTRED_EX, blue=Fore.LIGHTCYAN_EX, green=Fore.LIGHTGREEN_EX,
                    base=r["data"]["base"], amount=r["data"]["amount"], currency=r["data"]["currency"]))
    else:
        #TODO: cli prompt to enter correct
        print("Check inputs")


crp = input("Enter crypto: ")
fiat = input("ENter fiat currency: ")

get_price(crp, fiat)
#get_price("ETH", "USD")
