DOWNLOAD_DELAY = 0.05

IMAGES_STORE = "images"

ITEM_PIPELINES = {
    "gb_parse.pipelines.GbImageDownloadPipeline": 300,
    "gb_parse.pipelines.GbParseMongoPipeline": 400,
}

AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_START_DELAY = 2

AUTOTHROTTLE_MAX_DELAY = 10

AUTOTHROTTLE_DEBUG = True