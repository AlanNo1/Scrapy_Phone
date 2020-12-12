#-*-coding:utf-8-*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from phone_excel.items import PhoneExcelItem
import pandas as pd
import re
#导入模块

class HotSalesSpider(Spider):
    #定义爬虫名称
    df = pd.read_excel(r'测试号码.xlsx',usecols="A")
    name = 'phone'
    current_page = 0#设置当前页，起始为1
    #获取初始Request
    def start_requests(self):
        url = f"http://www.sjgsd.com/n/{self.df.loc[self.current_page].values[0]}"
        #生成请求对象，设置url，headers，callback
        yield Request(url,callback=self.phone_parse)
    # 解析数据
    def phone_parse(self, response):
        #使用xpath定位到号码信息，保存到列表中
        phinenumber = self.df.loc[self.current_page].values[0]
        #获取归属省份
        sf = re.search('<span class="green">归属地：</span>(.*)<br />',response.text).group(1).split()[0]     
        #获取归属地市
        city = re.search('<span class="green">归属地：</span>(.*)<br />',response.text).group(1).split()[-1]            
        #获取运营商名称
        yys = re.search('<span class="green">运营商：</span>(.*)<br />',response.text).group(1).split()[0]
        #获取区号
        quhao = re.search('<span class="green">区号：</span>(.*)<br />',response.text).group(1)
        #将爬取到的手机信息保存到item中
        item = PhoneExcelItem() 
        item["phinenumber"] = phinenumber
        item["sf"] = sf
        item["city"] = city
        item["yys"] = yys
        item["quhao"] = quhao
        #使用yield返回item
        yield item
        #获取下一页URL，并生成Request请求，提交给引擎
        #1.获取下一页URL
        self.current_page+=1
        if self.current_page<len(self.df):
            next_url = f"http://www.sjgsd.com/n/{self.df.loc[self.current_page].values[0]}"
            #2.根据URL生成Request，使用yield返回给引擎


            yield Request(next_url,callback=self.phone_parse)
