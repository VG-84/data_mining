from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from pymongo import MongoClient


    def __init__(self):
    def process_item(self, item, spider):
        self.db[spider.name].insert_one(item)
        return item


class GbImageDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item.get("photos", []):
            yield Request(url)

    def item_completed(self, results, item, info):
        if item.get("photos"):
            item["photos"] = [itm[1] for itm in results]
        return item