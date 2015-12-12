from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import Selector
from coffee_shop.items import CoffeeShopItem
import urllib

query_words = ['hipster', 'wood', 'natural lighting', 'almond milk', 'pour over', 'single origin', 'macbook', 'glasses', 'fixie', 'rustic', 'artisan']
# query_words = ['hipster', 'wood', 'almond milk']

class ArgSpider(CrawlSpider):
  name = 'CoffeeShopSpider'

  def __init__(self,shop_name=None,*args,**kwargs):
    super(ArgSpider, self).__init__(*args,**kwargs)
    self.start_urls = []
    self.query_urls = []
    initial_url = 'http://www.yelp.com/biz/{shop_name}-san-francisco'
    shop_name = shop_name.replace (" ", "-")
    initial_url = initial_url.format(shop_name=shop_name)
    self.start_urls.append(initial_url)
    urlTemplate = initial_url + '?q='
    for query in query_words:
        query = urllib.quote(query)
        url = urlTemplate + query
        self.query_urls.append(url)
        url = urlTemplate


  def parse(self, response):
    name = response.xpath('//div[@class="biz-page-header-left"]/h1/text()').extract_first()
    name = name.replace('\n','')
    name = name.strip()
    item = CoffeeShopItem()
    item['name'] = name
    yield Request(self.query_urls.pop(0), callback=self.parse_attributes, meta={'item': item})

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
    if self.query_urls:
        return Request(self.query_urls.pop(0), callback=self.parse_attributes, meta={'item': item})
    return item


