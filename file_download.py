import scrapy


class FileDownloadSpider(scrapy.Spider):
    name = 'file_download'
    allowed_domains = ['uristhome.ru']
    start_urls = [
        'https://uristhome.ru/document'
    ]

    def parse(self, response):
        urls = response.xpath('//ul[@class="y_articles-document-list"]//a/@href').getall()
        for url in urls:
            yield response.follow(url, callback=self.parse_file_page)

    def parse_file_page(self, response):
        for a in response.xpath('//div[@class="files"]//a'):
            item = {
                'name': a.xpath('text()').get(),
                'file_urls': [a.xpath('@href').get()]
            }
            yield item
