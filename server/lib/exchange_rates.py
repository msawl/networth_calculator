from locale import currency
import requests
from lib.vars import API_KEY


headers = {"apikey": API_KEY}


def convert_currency(currency_from: str, currency_to: str, amount: int) -> int:
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=CAD,AUD,HKD,GBP,SGD,JPY,INR,EUR,AED,USD&base=USD"
    # response = requests.get(url=url, headers=headers, verify=False)

    # print(response.json())

    temp_result = {
        "success": True,
        "timestamp": 1659336184,
        "base": "USD",
        "date": "2022-08-01",
        "rates": {
            "CAD": 1.279695,
            "AUD": 1.430501,
            "HKD": 7.85015,
            "GBP": 0.82045,
            "SGD": 1.379285,
            "JPY": 132.559498,
            "INR": 79.174996,
            "EUR": 0.978145,
            "USD": 1.00,
        },
    }
    # TODO : Put some cache here
    return temp_result


if __name__ == "__main__":
    print(convert_currency("USD", "INR", 81))
