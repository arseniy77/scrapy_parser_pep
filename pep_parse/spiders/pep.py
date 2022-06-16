import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        pep_table = response.css('section#numerical-index')
        # rows = pep_table.css('a[href^="pep-"]')
        rows = pep_table.css('tr')
        for row in rows[1::]:
            pep_number, pep_name = row.css('a::text').getall()
            link = row.css('a.pep.reference.internal::attr(href)').get()
            # print('LINK', link)
            # print(pep_number, pep_name)

            cb_kwargs = {'pep_number': pep_number,
                         'pep_name': pep_name,
                         }
            # print(row.css('a.pep.reference.internal::text').get())
            yield response.follow(
                link, callback=self.parse_pep, cb_kwargs=cb_kwargs
            )

    def parse_pep(self, response, pep_number, pep_name):
        # number = response.css('.breadcrumbs li::text').getall()[2].strip('PEP ')
        # name = response.css('h1.page-title::text').get()[len(number)+7::]
        print(pep_name)
        yield {
            'number': pep_number,
            'name': pep_name,
            'status': response.css('dd.field-even::text').get(),
        }
