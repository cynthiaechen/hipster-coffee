# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CoffeeShopItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    hipster = Field()
    wood = Field()
    natural_lighting = Field()
    almond_milk = Field()
    pour_over = Field()
    single_origin = Field()
    macbook = Field()
    fixie = Field()
    artisan = Field()
    mason_jar = Field()
    instagram = Field()
    ironic = Field()
    skinny_jeans = Field()
