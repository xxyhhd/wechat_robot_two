import requests
from lxml import etree
from urllib import parse


def get_response(rubbish):
    url = 'https://lajifenleiapp.com/sk/'+parse.quote(rubbish)
    return requests.get(url).text


def parse_response(rubbish):
    html = get_response(rubbish)
    html_tree = etree.HTML(html)
    try:
        rubbish_type = html_tree.xpath('//div[@class="col-md-12 col-xs-12"]/h1/span[3]/text()')[0]
        return rubbish+'属于'+rubbish_type
    except:
        return '没有查到{}的垃圾分类'.format(rubbish)


if __name__ == "__main__":
    rubbish = str(input('请输入要查询的垃圾'))
    return parse_response(rubbish)