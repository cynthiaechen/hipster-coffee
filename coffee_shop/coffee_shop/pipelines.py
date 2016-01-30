# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy import settings
from scrapy.exceptions import DropItem

class MongoDBPipeline(object):

  collection_name = 'coffee_shops'

  def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db
    # connection = pymongo.MongoClient(
    #   settings['MONGODB_SERVER'],
    #   settings['MONGODB_PORT']
    # )
    # db = connection[settings['MONGODB_DB']]
    # self.collection = db[settings['MONGODB_COLLECTION']]
  
  @classmethod

  def from_crawler(cls, crawler):
    return cls(
      mongo_uri=crawler.settings.get('MONGO_URI'),
      mongo_db=crawler.settings.get('MONGODB_DATABASE', 'shops')
    )
  def open_spider(self, spider):
    self.client = pymongo.MongoClient(self.mongo_uri)
    self.db = self.client[self.mongo_db]

  def close_spider(self, spider):
    self.client.close()

  def process_item(self, item, spider):
    if (len(item) == 14):
      print('saving to database', dict(item))
      self.db[self.collection_name].insert(dict(item))
      return item
