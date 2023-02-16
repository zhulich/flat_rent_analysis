from scrapy.crawler import CrawlerProcess

from olx_rent.spiders.olx_spiders import OlxSpiders


def main():
    process = CrawlerProcess(
        {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
    )
    process.crawl(OlxSpiders)
    process.start()


if __name__ == "__main__":
    main()
