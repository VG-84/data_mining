from itemadapter import ItemAdapter
from pymongo import MongoClient


class GbParsePipeline:
    def process_item(self, item, spider):
        return item


class GbParseMongoPipeline:
    def __init__(self):
        client = MongoClient()
        self.db = client["gb_parse"]

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(item)
        return item