import json
from copy import deepcopy
import datetime as dt
from urllib.parse import urlencode
import scrapy
from ..items import InstaTag, InstaPost, InstaUser


class InstagramSpider(scrapy.Spider):
    def __init__(self, login, password, tags, *args, **kwargs):
        self.login = login
        self.password = password
        self.tags = tags
        self.users = ["teslamotors"]

    def parse(self, response):
        try:
    def parse(self, response):
        except AttributeError as e:
        print(e)
        if response.json()["authenticated"]:
        for user_name in self.users:
            yield response.follow(f"/{user_name}/", callback=self.user_page_parse)

    def tag_page_parse(self, response):
        js_data = self.js_data_extract(response)

    def tag_page_parse(self, response):
            callback = self._api_tag_parse,
        )

    def user_page_parse(self, response):
        callback = self._api_tag_parse,
    )

    def user_page_parse(self, response):
        print(1)
        js_data = self.js_data_extract(response)
        insta_user = InstUser(js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"])
        yield insta_user.get_user_item()
        yield response.follow(
            f"{self.api_url}?{urlencode(insta_user.get_followed_vars())}",
            callback=self._api_follow_parse,
            cb_kwargs={"insta_user": insta_user},
        )

    def _api_follow_parse(self, response, **kwargs):
        print(1)

    def _api_tag_parse(self, response):
        data = response.json()
        insta_tag = InstTag(data["data"]["hashtag"])

    def paginate_params(self):
        def get_post_items(self):
            for edge in self.hashtag["edge_hashtag_to_media"]["edges"]:
                yield InstaPost(date_parse=dt.datetime.utcnow(), data=edge["node"])

class InstUser:
    def __init__(self, user):
        self.user = user
        self.user_followers = InstaFollowers(user["id"])

    def get_user_item(self):
        data = {}
            for key, value in self.user.items():
            if not (isinstance(value, dict) or isinstance(value, list)):
                data[key] = value
            return InstaUser(date_parse=dt.datetime.utcnow(), data=data)

    def get_followed_vars(self):
            return self.user_followers.get_variables("followed")

class InstaFollowers:
    query_hashs = {
        "followed": {"query": "3dec7e2c57367ef3da3d987d89f9dbc8", "next": None},
        "followers": {"query": "5aefa9893005572d237da5068082d8d5", "next": None},
    }

    def __init__(self, user_id):
        self.user_id = user_id
        self.variables = {"id": user_id, "include_reel": True, "fetch_mutual": True, "first": 24}

    def get_variables(self, key):
        variables = deepcopy(self.variables)
        if self.query_hashs[key]["next"]:
            variables["after"] = self.query_hashs[key]["next"]

        url_query = {
            "query_hash": self.query_hashs[key]["query"],
            "variables": json.dumps(self.variables),
        }
        return url_query
