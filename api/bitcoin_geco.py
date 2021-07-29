#!/usr/bin/env python3

import requests, json

btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", headers = {"accept":"application/json"})

print('Bitcoin price: ', btc_price.json()['bitcoin']['usd'], '$')
