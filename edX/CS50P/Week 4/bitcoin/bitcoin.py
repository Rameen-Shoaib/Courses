import json
import requests
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

    elif len(sys.argv) == 2:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(response.json(), indent=2))
        output = (response.json())

        rate = output["bpi"]["USD"]["rate_float"]

        perCoin = rate * float(sys.argv[1])
        print(f"${perCoin:,.4f}")

except requests.RequestException:
    sys.exit(1)