import scrapy


class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        table = response.xpath('//*[contains(@class, "table table-bordered")]')[0]
        trs = table.xpath('.//tr')[9:223]
        for tr in trs:
            country = tr.xpath('.//td[2]//a//text()|'
                               './/td[2]//text()').extract_first().strip()
            tcases = tr.xpath('.//td[3]//text()').extract_first()
            tdeaths = tr.xpath('.//td[5]//text()').extract_first()
            trecovered = tr.xpath('.//td[7]//text()').extract_first()
            ttests = tr.xpath('.//td[13]//text()').extract_first()
            population = tr.xpath('.//td[15]//text()').extract_first()

            yield {
                "Country": country,
                "Total Cases": tcases,
                "Total Deaths": tdeaths,
                "Total Recovered": trecovered,
                "Total Tests": ttests,
                "Population": population

            }

