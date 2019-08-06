import requests
from lxml import etree
from selenium import webdriver
from urllib import parse
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

browser = webdriver.Chrome(chrome_options=chrome_options,
                           executable_path='/home/rain/my_soft/chromedriver')


search_path = '//div[@class="title clearflaot"]/a[2]/@href'
detail_path = '//div[@class="hq-data tab-pane1 fl"]//tbody'


def create_browser(url):
    browser.get(url)
#     print('页面')
    return browser.page_source


def run(url):
    detail_html_tree = etree.HTML(create_browser(url))
    detail_items = detail_html_tree.xpath(detail_path)
    for item in detail_items:
        label = item.xpath('./tr/td/label/text()')
        # print(label)
        span = item.xpath('./tr/td/span/text()')
        a = str(dict(zip(label,span)))
        a = re.sub('{|}','',a)
        return a


def gupiao_main(query):
    url = 'http://so.eastmoney.com/web/s?keyword='+parse.quote(query)
    search_html_tree = etree.HTML(create_browser(url))
    detail_url = search_html_tree.xpath(search_path)[0]
#     print(detail_url)
    if detail_url:
        return run(detail_url)
    else:
        return '该股票不存在'
        

if __name__ == "__main__":
    query = str(input('请输入股票代码或名称：'))
    gupiao_main(query)