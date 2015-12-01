from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from coffee_shop.items import CoffeeShopItem
import urllib

# query_words = ['hipster', 'wood', 'natural lighting', 'almond milk']

class ArgSpider(CrawlSpider):
  name = 'CoffeeShopSpider'

  def __init__(self,shop_name=None,query=None,*args,**kwargs):
    super(ArgSpider, self).__init__(*args,**kwargs)
    self.start_urls = []
    urlTemplate = 'http://www.yelp.com/biz/{shop_name}-san-francisco?q={query}'
    # shop_name = shop_name.replace (" ", "-")
    query = urllib.quote(query)
    self.start_urls.append(urlTemplate.format(shop_name=shop_name, query=query))

  def parse(self, response):
    frequency = response.xpath('//div[@class="feed_filters"]/h3/text()').re_first(r'\d+')
    print('before frequency', frequency)
    # frequency = frequency[1:]
    # frequency = frequency.replace("'", "")
    print('Hi, this is the url', response.url)
    print('after frequency', frequency)
    item = CoffeeShopItem()
    item['name'] = response.url
    item['hipster'] = frequency
    print item
    yield item
