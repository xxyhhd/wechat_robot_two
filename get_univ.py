import requests
import bs4
from bs4 import BeautifulSoup


# 获取网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


# 提取内容到列表
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


# 展示排名
def printUnivList(ulist, num, strlist=[]):
    reply = ''
    # print('{0:^4}\t{1:{3}^8}\t{2:^5}'.format('排名', '学校名称', '平均成绩', chr(12288))) #chr(12288)是中文空格的编码字符，用中文空格对中文进行填充
    for suc in ulist[0:num]:
        a = ('{0:^5}\t{1:{3}^10}\t{2:^8}'.format(suc[0], suc[1], suc[2], chr(12288)))
        strlist.append(a)
    reply = '\n'.join(strlist)
    return reply

def main(uinfo=[]):
    # print(1)
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    if html:
        fillUnivList(uinfo, html)
        title = '{0:^5}\t{1:{3}^10}\t{2:^5}'.format('排名', '学校名称', '平均成绩', chr(12288))
        info = printUnivList(uinfo, 5)  # 展示前5所学校
        return title + '\n' + info
    else:
        return '爬取失败'


if __name__=='__main__':
    main()

# print(main())


