DOWNLOAD_DELAY = 1.2

ITEM_PIPELINES = {
    "gb_parse.pipelines.GbParsePipeline": 300,
    "gb_parse.pipelines.GbParseMongoPipeline": 400,
}