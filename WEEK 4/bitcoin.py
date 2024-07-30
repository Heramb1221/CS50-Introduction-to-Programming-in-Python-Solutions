import requests
import sys
import json

try:

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        x = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    factor = r.json()
    price = factor["bpi"]["USD"]['rate_float']
    total = price * float(x)
    print(f"${total:,.4f}")

except requests.RequestException:
    pass
