from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from coffee_shop.items import CoffeeShopItem
import urllib

query_words = ['hipster', 'wood', 'natural lighting','almond milk', 'pour over', 'single origin', 'macbook', 'fixie', 'artisan', 'mason jar', 'instagram', 'ironic', 'skinny jeans']
# query_words = ['hipster', 'wood', 'natural lighting']


class ArgSpider(CrawlSpider):
  name = 'CoffeeShopSpider'
  allowed_domains = ['yelp.com']

  def start_requests(self):
    # yield Request('http://www.yelp.com/search?find_desc=hipster+coffee+shop&find_loc=San+Francisco/', self.parse)
    # yield Request('http://www.yelp.com/search?find_desc=hipster+coffee+shop&find_loc=San+Francisco,+CA&start=10', self.parse)
    yield Request('http://www.yelp.com/search?find_desc=hipster+coffee+shop&find_loc=San+Francisco,+CA&start=20', self.parse)

  def parse(self, response):
    for href in response.xpath('//a[@class="biz-name"]'):
        link = href.xpath('@href').extract_first()
        #check if href starts with /biz
        if link.split('/', 2)[1] == 'biz':
            url = 'http://www.yelp.com' + link
            yield Request(url, self.parse_shop_page)

  def parse_shop_page(self, response):
    name = response.xpath('//div[@class="biz-page-header-left"]/h1/text()').extract_first()
    name = name.replace('\n','')
    name = name.strip()
    name = name.replace(' ', '-')
    name = name.lower()
    item = CoffeeShopItem()
    item['name'] = name
    base_url = response.url.split('?', 1)[0]
    urlTemplate = base_url + '?q='
    #loop through each query word and call parse_attributes to scrape data and calculate percentages
    for query in query_words:
        query = urllib.quote(query)
        query_url = urlTemplate + query
        yield Request(query_url, callback=self.parse_attributes, meta={'item': item})

  def parse_attributes(self, response):
    item = response.meta['item']
    reviewCount = response.xpath('//h3[@class="feed_search-results"]/text()').re_first(r'\d+')
    reviewCount = int(reviewCount)
    total = response.xpath('//span[@itemprop="reviewCount"]/text()').extract_first()
    total = int(total)
    percentage = (reviewCount*100) / float(total)
    percentage = round(percentage, 2)
    url = response.url
    attribute = url.split('=', 1)[1]
    attribute = urllib.unquote(attribute)
    attribute = attribute.replace(" ", "_")
    item[attribute] = percentage
    return item


