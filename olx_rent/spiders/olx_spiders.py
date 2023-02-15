import scrapy
from scrapy.http import Response

from config import START_URLS
from helper_func import convert_price, convert_date


class OlxSpiders(scrapy.Spider):
    name = "olx_spiders"
    allowed_domains = ["www.olx.ua"]
    start_urls = START_URLS

    custom_settings = {
        "FEEDS": {
            "data/%(name)s/%(name)s_%(time)s.csv": {"format": "csv", "overwrite": False}
        }
    }

    def parse(self, response: Response, **kwargs):
        for advertisements in response.css("div.css-1sw7q4x > a"):
            detail_url = advertisements.css("a::attr(href)").get()
            yield response.follow(detail_url, self.parse_detail_page)

        next_page = (
            response.css("div.css-4mw0p4 > ul > a:last-child")
            .css("a::attr(href)")
            .get()
        )
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail_page(self, response: Response):
        detail_information = {
            "Посилання": response.url,
            "Заголовок": response.css("h1.css-1soizd2::text").get(),
            "Ціна": convert_price(response.css("h3.css-ddweki::text").getall()),
            "Область": response.css("ol.css-jramwl > li:nth-of-type(5) > a::text")
            .get()
            .split(" - ")[1],
            "Місто": response.css("ol.css-jramwl > li:nth-of-type(6) > a::text")
            .get()
            .split(" - ")[1],
            "Id": response.css("span.css-12hdxwj::text").getall()[1],
            "Власник": response.css("p.css-b5m1rv > span::text").get(),
            "Дата": convert_date(response.css("span.css-19yf5ek::text").get()),
            "Район": None,
            "Поверх": None,
            "Поверховість": None,
            "Загальна площа": None,
            "Площа кухні": None,
            "Тип стін": None,
            "Кількість кімнат": None,
            "Планування": None,
            "Опалення": None,
            "Ремонт": None,
        }
        if (
            response.css("ol.css-jramwl > li:nth-of-type(7) > a::text").get()
            is not None
        ):
            detail_information.update(
                {
                    "Район": response.css("ol.css-jramwl > li:nth-of-type(7) > a::text")
                    .get()
                    .split(" - ")[1]
                }
            )
        for li in response.css(".css-b5m1rv::text").getall():
            key = li.split(": ")[0]
            if key in detail_information.keys():
                value = li.split(": ")[1]
                detail_information[key] = value
        return detail_information
