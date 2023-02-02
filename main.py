# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
from pandas import DataFrame
base_url = "https://www.olx.ua/d/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/"
cities = ["lvov/", "kiev/"]
currency = "?currency=UAH"
filter_ordering = "&search%5Border%5D=created_at%3Adesc"
filter_rooms = "&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D="
filter_page = "&page="
num_of_rooms = ["odnokomnatnye", "dvuhkomnatnye", "trehkomnatnye"]

url = "https://www.olx.ua/d/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/lvov/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye"

response = requests.get(url)
soup_content = BeautifulSoup(response.content, "html.parser")


flats = soup_content.select("h6.er34gjf0")


print(flats)