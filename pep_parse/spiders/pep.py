import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        pep_table = response.css('section#numerical-index')
        rows = pep_table.css('a[href^="pep-"]')
        for row in rows[1:7]:


            cb_kwargs = {}
            print(row.css('a.pep.reference.internal::text').get())
            yield response.follow(row, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css('.breadcrumbs li::text').getall()[2].strip('PEP ')
        name = response.css('h1.page-title::text').get()[len(number)+7::]
        yield {
            'number': number,
            'name': name,
            'status': response.css('dd.field-even::text').get(),
        }
