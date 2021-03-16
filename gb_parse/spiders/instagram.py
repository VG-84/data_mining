import json

import datetime as dt
from urllib.parse import urlencode
import scrapy
from ..items import InstaTag, InstaPost


class InstagramSpider(scrapy.Spider):
class InstagramSpider(scrapy.Spider):
    start_urls = ["https://www.instagram.com/"]
    _login_url = "https://www.instagram.com/accounts/login/ajax/"
    _tags_path = "/explore/tags/"
    api_url = "/graphql/query/"

    def __init__(self, login, password, tags, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def parse(self, response):
                    yield response.follow(f"{self._tags_path}{tag}/", callback=self.tag_page_parse)

    def tag_page_parse(self, response):
        js_data = self.js_data_extract(response)
        insta_tag = InstTag(js_data["entry_data"]["TagPage"][0]["graphql"]["hashtag"])
        yield insta_tag.get_tag_item()
        yield from insta_tag.get_post_items()
        yield response.follow(
            f"{self.api_url}?{urlencode(insta_tag.paginate_params())}",
            callback=self._api_tag_parse,
        )

    def _api_tag_parse(self, response):
        data = response.json()
        insta_tag = InstTag(data["data"]["hashtag"])
        yield from insta_tag.get_post_items()
        yield response.follow(
            f"{self.api_url}?{urlencode(insta_tag.paginate_params())}",
            callback=self._api_tag_parse,
        )

    def js_data_extract(self, response):
        script = response.xpath(
            "//script[contains(text(), 'window._sharedData = ')]/text()"
        ).extract_first()
        return json.loads(script.replace("window._sharedData = ", "")[:-1])


class InstTag:
    query_hash = "9b498c08113f1e09617a1703c22b2f32"

    def __init__(self, hashtag: dict):
        self.variables = {
            "tag_name": hashtag["name"],
            "first": 100,
            "after": hashtag["edge_hashtag_to_media"]["page_info"]["end_cursor"],
        }
        self.hashtag = hashtag

    def get_tag_item(self):
        item = InstaTag()
        item["date_parse"] = dt.datetime.utcnow()
        data = {}
        for key, value in self.hashtag.items():
            if not (isinstance(value, dict) or isinstance(value, list)):
                data[key] = value
        item["data"] = data
        return item

    def paginate_params(self):
        url_query = {"query_hash": self.query_hash, "variables": json.dumps(self.variables)}
        return url_query

    def get_post_items(self):
        for edge in self.hashtag["edge_hashtag_to_media"]["edges"]:
            yield InstaPost(date_parse=dt.datetime.utcnow(), data=edge["node"])