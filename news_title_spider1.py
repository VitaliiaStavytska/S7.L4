
import scrapy
import json

class IlSole24OreSpider(scrapy.Spider):
    name = 'ilsole24ore_spider'
    start_urls = ['https://www.ilsole24ore.com/']

    def parse(self, response):

        news_titles = response.css('a').getall()

        json_data = {'titles': news_titles}
        with open('ilsole24ore_titles.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=2)

        for title in news_titles:
            self.log(title)
            