import locale
from datetime import datetime
import pandas as pd
import requests


def convert_date(date: str) -> datetime.date:
    locale.setlocale(locale.LC_ALL, "uk_UA.UTF-8")

    today = "Сьогодні"
    if today in date:
        return datetime.now().date()
    return datetime.strptime(date[:-3], "%d %B %Y").date()


def convert_price(price: list[str]) -> int:
    usd = "$"
    euro = "€"
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url, params={"base": "UAH", "symbols": "USD,EUR"})
    data = response.json()
    if usd in price:
        return int(price[0]) / data["rates"]["USD"]
    elif euro in price:
        return int(price[0]) / data["rates"]["EUR"]

    return int(price[0].replace(" ", ""))


def create_df(
    rooms: list[pd.DataFrame], group_by: str, price: str, city: str = None
) -> pd.DataFrame:
    if city:
        average_prices = [
            room[room["Місто"] == city].groupby(group_by)[price].mean()
            for room in rooms
        ]
    else:
        average_prices = [room.groupby(group_by)[price].mean() for room in rooms]

    data_frame = pd.DataFrame(
        {
            "1 кімната": average_prices[0],
            "2 кімнати": average_prices[1],
            "3 кімнати": average_prices[2],
        }
    )
    return data_frame

