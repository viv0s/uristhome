from scrapy.crawler import CrawlerProcess
from file_download import FileDownloadSpider


settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'ROBOTSTXT_OBEY': False,
    'CONCURRENT_REQUESTS': 1,
    'DOWNLOAD_DELAY': 3,
    'ITEM_PIPELINES': {
        'pipelines.FilePathPipeline': 300,
    },
    'FILES_STORE': 'files'
}

process = CrawlerProcess(settings)
process.crawl(FileDownloadSpider)
process.start()
