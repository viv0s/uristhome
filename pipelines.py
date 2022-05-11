import os
from urllib.parse import urlparse
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class FilePathPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        adapter = ItemAdapter(item)
        return adapter['name'] + '.' + request.url.split('.')[-1]
