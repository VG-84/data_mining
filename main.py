crawler_settings = Settings()
crawler_settings.setmodule("gb_parse.settings")
crawler_proc = CrawlerProcess(settings=crawler_settings)
crawler_proc.crawl(
    InstagramSpider,
    login=os.getenv("INST_LOGIN"),
    password=os.getenv("INST_PASSWORD"),
    tags=tags,
)
# crawler_proc.crawl(ZillowSpider)
crawler_proc.start()