from pathlib import Path

import scrapy

class RequerimentosSpider(scrapy.Spider):
    name = "requerimentos"

    def start_requests(self):
        urls = [f"https://cmbelem.pb.gov.br/public/portal/requerimentos/geral?page={i}" for i in range(1, 23)]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = f"requerimentos-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")