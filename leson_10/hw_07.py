import datetime as dt
import json
from pathlib import Path

import requests

src_root = Path(__file__).parent
file_name = src_root / "logs.json"

api_key = "V2V43QAQ8RILGBOW"
url = "https://www.alphavantage.co/query"
BASIC_CURRENCY = "CHF"


def convert(value, currency_from, currency_to):
    parameters = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": currency_from,
        "to_currency": currency_to,
        "apikey": api_key,
    }

    result = requests.get(url=url, params=parameters)
    data = result.json()["Realtime Currency Exchange Rate"]
    coefficient = float(data["5. Exchange Rate"])

    log_data = [
        {
            "currency_from": data["1. From_Currency Code"],
            "currency_to": data["3. To_Currency Code"],
            "rate": data["5. Exchange Rate"],
            "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    ]
    with open(file_name, mode="r") as file:
        try:
            old_log_data = json.load(file)
        except json.decoder.JSONDecodeError:
            old_log_data = log_data
        else:
            old_log_data.extend(log_data)

    with open(file_name, mode="w") as f:
        json.dump(old_log_data, f, indent=4)

    return value * coefficient


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def __str__(self):
        return f"Total price is {self.value} {self.currency}"

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(value=self.value + other.value, currency=self.currency)
        else:
            # Converting both prices to the CHF
            left_in_basic = convert(
                value=self.value,
                currency_from=self.currency,
                currency_to=BASIC_CURRENCY,
            )
            right_in_basic = convert(
                value=other.value,
                currency_from=other.currency,
                currency_to=BASIC_CURRENCY,
            )
            total_in_basic = left_in_basic + right_in_basic
            # Converting total price in CHF to the first currency
            total_in_main_currency = convert(
                value=total_in_basic,
                currency_from=BASIC_CURRENCY,
                currency_to=self.currency,
            )
            return Price(value=round(total_in_main_currency, 2), currency=self.currency)


flight = Price(value=10000, currency="UAH")
hotel = Price(value=1000, currency="EUR")

total: Price = flight + hotel

print(total)
