import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_table = response.css('section#numerical-index')
        rows = pep_table.css('tr')
        for row in rows[1::]:
            pep_number, pep_name = row.css('a::text').getall()
            link = row.css('a.pep.reference.internal::attr(href)').get()
            cb_kwargs = {'pep_number': pep_number,
                         'pep_name': pep_name,
                         }
            yield response.follow(
                link, callback=self.parse_pep, cb_kwargs=cb_kwargs
            )

    def parse_pep(self, response, pep_number, pep_name):
        data = {
            'number': pep_number,
            'name': pep_name,
            'status': response.css('dt:contains("Status") + dd::text').get(),
        }
        yield PepParseItem(data)
