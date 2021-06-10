import requests

#payload = {"data":["id"]}
#r = requests.get("https://api.coinbase.com/v2/currencies",params=payload)
#r = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.json())