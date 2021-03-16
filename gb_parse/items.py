
    characteristics = scrapy.Field()
    descriptions = scrapy.Field()
    author = scrapy.Field()


class Insta(scrapy.Item):
    _id = scrapy.Field()
    date_parse = scrapy.Field()
    data = scrapy.Field()
    photos = scrapy.Field()


class InstaTag(Insta):
    pass


class InstaPost(Insta):
    pass