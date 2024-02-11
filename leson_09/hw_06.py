currency_exchange = {
    "EUR": (0.94, 1.06),
    "USD": (0.87, 1.14),
    "UAH": (0.023, 42.99)
}


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
            first_price = self.value * currency_exchange[self.currency][0]
            second_price = other.value * currency_exchange[other.currency][0]

            # Converting total price in CHF to the first currency
            total_price = (first_price + second_price) * currency_exchange[self.currency][1]
            return Price(value=round(total_price, 2), currency=self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(value=self.value - other.value, currency=self.currency)
        else:
            return f"Can't subtract {other.currency} from {self.currency}"


flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")

total: Price = flight + hotel

print(total)