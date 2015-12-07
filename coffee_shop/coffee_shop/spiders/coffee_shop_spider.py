from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
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
    urlTemplate = 'http://www.yelp.com/biz/{shop_name}-coffee-san-francisco?q='
    shop_name = shop_name.replace (" ", "-")
    urlTemplate = urlTemplate.format(shop_name=shop_name)
    for query in query_words:
        query = urllib.quote(query)
        url = urlTemplate + query
        self.start_urls.append(url)
        url = urlTemplate


  def parse(self, response):
    reviewCount = response.xpath('//h3[@class="feed_search-results"]/text()').re_first(r'\d+')
    reviewCount = int(reviewCount)
    total = response.xpath('//span[@itemprop="reviewCount"]/text()').extract_first()
    total = int(total)
    percentage = (reviewCount*100)/total
    name = response.xpath('//div[@class="biz-page-header-left"]/h1/text()').extract_first()
    name = name.replace('\n','')
    name = name.strip()
    url = response.url
    attribute = url.split('=', 1)[1]
    attribute = urllib.unquote(attribute)
    attribute = attribute.replace(" ", "_")
    item = CoffeeShopItem()
    item['name'] = name
    item[attribute] = percentage
    yield item
