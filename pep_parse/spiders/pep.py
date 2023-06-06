import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse_pep(self, response):
        name = response.css('section#pep-content h1::text').get()
        data = {
            'number': re.findall(r'\d+', name)[0],
            'name': name,
            'status': response.css('dd abbr::text').get(),
        }
        yield PepParseItem(data)

    def parse(self, response):
        pep_links = response.css(
            'section#numerical-index').css('a[href^="pep"]')
        for pep_link in pep_links:
            if pep_link is not None:
                yield response.follow(pep_link, callback=self.parse_pep)
