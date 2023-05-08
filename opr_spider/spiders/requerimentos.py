import re
import scrapy

class RequerimentosSpider(scrapy.Spider):
    name = "requerimentos"

    def start_requests(self):
        urls = [f"https://cmbelem.pb.gov.br/public/portal/requerimentos/geral?page={i}" for i in range(1, 23)]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        regex=r"(https:\/\/cmbelem\.pb\.gov\.br\/public\/portal\/requerimentos\/geral\/(\w*-?)+)"

        for url in [t[0] for t in re.findall(regex, response.body.decode("utf-8"))]:
            yield {
                'url': url
            }