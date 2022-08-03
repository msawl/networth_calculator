from locale import currency
import requests
from lib.vars import API_KEY


headers = {"apikey": API_KEY}


def convert_currency() -> int:
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=CAD,AUD,HKD,GBP,SGD,JPY,INR,EUR,AED,USD&base=USD"
    # response = requests.get(url=url, headers=headers, verify=False)

    # print(response.json())

    temp_result = {
        "success": True,
        "timestamp": 1659499444,
        "base": "USD",
        "date": "2022-08-03",
        "rates": {
            "CAD": 1.285625,
            "AUD": 1.44219,
            "HKD": 7.85005,
            "GBP": 0.820203,
            "SGD": 1.380495,
            "JPY": 132.344498,
            "INR": 78.710103,
            "EUR": 0.981105,
            "AED": 3.673102,
            "USD": 1,
        },
    }
    return temp_result


if __name__ == "__main__":
    print(convert_currency())
