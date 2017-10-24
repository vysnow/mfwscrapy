# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from myapp.models import City, Scenery


class MfwscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CityItem(DjangoItem):
	django_model = City

class SceneryItem(DjangoItem):
	django_model = Scenery