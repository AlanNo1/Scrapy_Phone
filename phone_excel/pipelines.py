# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
from scrapy.exceptions import DropItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PhoneExcelPipeline:
    def process_item(self, item, spider):
        if item["sf"] == "未知":
            pass
            #raise DropItem("查找到不确定的省份: %s"%item)   
        item['yys'] = item['yys'][-2:]        
        return item

class SaveToExclePipeline(object):
    def open_spider(self,spider):
        self.df_list = []

    #数据处理
    def process_item(self, item, spider):
        self.df_list.append(dict(item))
        return item
    def close_spider(self,spider):

    	df_all = pd.DataFrame(self.df_list).to_excel(f"匹配后的号码运营商地市等信息.xlsx",index=False)

        
