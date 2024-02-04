import scrapy

class LinksSpider(scrapy.Spider):
    name = "ebaylinks"
    start_urls = ["https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=roma&_sacat=0&_odkw=41"]

    def parse(self,response):
        links = response.css("a::attr(href)").getall()
        for link in links:
            yield{
                "url":link
                }
        for next_page in links:
            yield response.follow(next_page, callback = self.parse)
            

            