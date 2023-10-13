from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "809d3ed93e9d424a274c"

# nicely formatted output of json
printer = PrettyPrinter()


def main():
    currencies = get_currencies()

    print("Welcome to the Currency Converter!")
    print("Select an option: ")
    print("List - list all the currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print("Name - gets the name of the currency id")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        elif command == "name":
            id = input("Enter a currency id: ").upper()
            print(currency_name(id, currencies))
        else:
            print("Unrecognized Command!")


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    # converting dictionary to list (contains tuples)
    data = list(data.items())
    # sorting by the currency name
    data.sort()

    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']

        # try to find the key in dictionary if exist give the value otherwise give default value
        # because not all of them contains symbol
        symbol = currency.get("currencySymbol", "")

        print(f"{_id} - {name} - {symbol}")


def currency_name(id, currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']

        if  _id == id:
            print(f"{id} -> {name}")
            return name


def exchange_rate(currency1, currency2):
    # convert currency1 to currency2
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    # incase of an invalid input an empty list is returne
    if len(data) == 0:
        print("Invalid Currencies")
        return

    rate = list(data.values())[0]

    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid Amount")
        return

    converted_amount = rate * amount

    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")

    return converted_amount


if __name__ == "__main__":
    main()
