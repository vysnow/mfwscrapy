# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from django.db import IntegrityError
from scrapy.exceptions import DropItem
from asgiref.sync import sync_to_async


class MfwscraperPipeline:
    async def process_item(self, item, spider):
        try:
            await self.save_item(item)
            spider.action_successful = True
            spider.logger.info("Item {id} saved to Django DB".format(
                id=item['id']))
        except IntegrityError as e:
            spider.logger.error(str(e))
            raise DropItem("Save error, Missing attribute.")
        return item
    
    @sync_to_async
    def save_item(self, item):
        item.save()
