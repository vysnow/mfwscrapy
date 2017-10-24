# -*- coding: utf-8 -*-
import scrapy
import re
import json
from mfwscraper.items import CityItem, SceneryItem
from myapp.models import City
from asgiref.sync import sync_to_async

class MddSpider(scrapy.Spider):
    name = 'mdd'
    allowed_domains = ['www.mafengwo.cn']
    start_urls = ['https://www.mafengwo.cn/mdd/']
    cityid = 0

    def __init__(self, q="chenzhou", *args, **kwargs):
        super(MddSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.mafengwo.cn/search/s.php?q=' + q]

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_city)

    def parse_city(self, response):
        # get the cityId and do scenery search
        url = response.xpath('//*[@id="_j_search_result_left"]/div[1]/a/@href').extract()[0]
        print("#######", url)
        
        pattern = r'id=(\d+)'  
        match = re.search(pattern, url)
        cityId = match.group(1)
        self.cityid = cityId

        cityName = response.css('#_j_search_result_left > div.search-mdd-wrap > a > div > p.title::text').extract_first()
        cityItem = CityItem()
        cityItem['id'] = cityId
        cityItem['name'] = cityName
        yield cityItem

        # get the gonglve of this city to get the sceneries
        url = "https://www.mafengwo.cn/jd/"
        url = url + cityId + "/gonglve.html"
        yield scrapy.Request(url, callback=self.parse_scenery)

    async def parse_scenery(self, response):
        #richtext = response.xpath('//*[@id="container"]/div[5]/div/script/text()').extract_first()
        richtext = response.css('#container > div.row.row-allPlace.row-bg > div > script::text').extract_first()
        richtext = re.sub(r"\n", "", richtext)
        richjson = re.search(r"mapponints[\s]?=(.+)M[\.]closure", richtext).group(1)
        lastcolon = richjson.find("];", 0, -1)
        richjson = richjson[:lastcolon]
        richjson = richjson + ']' # to make up the json end

        sceneries = json.loads(richjson)
        for scenery in sceneries:
            sceneryItem = SceneryItem()
            sceneryItem['id'] = scenery['id']
            sceneryItem['name'] = scenery['name']
            sceneryItem['typeId'] = scenery['type_id']
            sceneryItem['typeCode'] = scenery['type_code']
            sceneryItem['lat'] = scenery['lat']
            sceneryItem['lng'] = scenery['lng']
            sceneryItem['rank'] = scenery['rank']
            sceneryItem['description'] = scenery['description']
            sceneryItem['attraction'] = ''
            sceneryItem['img'] = scenery['img']
            sceneryItem['imgPlaceHolder'] = scenery['img_placeholder']
            sceneryItem['parentId'] = 0
            # foreign key the cityId
            city = await self.get_city(self.cityid)
            sceneryItem['city'] = city
            yield sceneryItem

    @sync_to_async
    def get_city(self, id):
        return City.objects.get(id = id)