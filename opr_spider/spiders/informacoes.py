import scrapy
import csv
import re

class InformacoesSpider(scrapy.Spider):
    name = "informacoes"

    def start_requests(self):
        with open("requerimentos.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            next(reader, None)  # skip the headers
            for row in reader:
                yield scrapy.Request(url=row[0], callback=self.parse)

    def parse(self, response):
        yield {
            'titulo': self.get_titulo(response),
            'descricao': self.get_descricao(response)
        }

    def get_titulo(self, response):
        tag = response.xpath("//title/text()")
        return tag.get().split("|")[0].strip()

    def get_descricao(self, response):
        tag = response.xpath('//p[@class="MsoNormal"]//text()')
        return re.sub(r"\r?\n", " ", " ".join(tag.getall()))