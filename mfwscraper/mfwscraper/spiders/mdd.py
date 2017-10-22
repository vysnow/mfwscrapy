import scrapy


class MddSpider(scrapy.Spider):
    name = "mdd"
    allowed_domains = ["www.mafengwo.cn"]
    start_urls = ["https://www.mafengwo.cn/mdd/"]

    def parse(self, response):
        pass
