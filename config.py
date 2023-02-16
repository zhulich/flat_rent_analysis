# Spider variables
cities = [
    "kiev",
    "ivano-frankovsk",
    "vinnitsa",
    "lutsk",
    "dnepr",
    "donetsk",
    "zhitomir",
    "uzhgorod",
    "zaporozhe",
    "kropivnitskiy",
    "lugansk",
    "lvov",
    "nikolaev_106",
    "odessa",
    "poltava",
    "rovno",
    "sumy",
    "ternopol",
    "kharkov",
    "kherson",
    "khmelnitskiy",
    "chernigov",
    "cherkassy",
    "chernovtsy",
]
START_URLS = [
    f"https://www.olx.ua/d/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/{city}/?currency=UAH&search%5Border%5D=created_at:desc"
    for city in cities
]

# Pandas variables
city_group_by = "Київ"
prices = {"price": "Ціна", "price m2": "Ціна м2"}
group_by = {
    "heating": "Опалення",
    "repair": "Ремонт",
    "walls": "Тип стін",
    "city": "Місто",
    "district": "Район",
}
