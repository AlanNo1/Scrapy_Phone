# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneExcelItem(scrapy.Item):
    # define the fields for your item here like:
    phinenumber = scrapy.Field() #手机号码
    sf = scrapy.Field() #归属省份
    city = scrapy.Field() #归属地市
    yys = scrapy.Field() #运营商
    quhao = scrapy.Field() #区号


