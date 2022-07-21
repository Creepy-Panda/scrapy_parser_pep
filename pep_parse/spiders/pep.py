import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_link = response.css('section#numerical-index tbody tr td')
        for link in all_link:
            pep_link = link.css('a::attr(href)').get()
            if pep_link is not None:
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        data = {
            'number': [int(s) for s in title.split() if s.isdigit()][0],
            'name': title,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
