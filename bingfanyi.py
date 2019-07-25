import requests


def check_chinese(query):
    for ch in query:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def fanyi_main(query):
    post_url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=B8917D88F08946B3B2E59191AF2156D9&IID=translator.5028.4'

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie': '_EDGE_V=1; MUID=1C332E1A621D673A2E5823956333661A; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=10B713BC0506411887ABFECB2FB1C692&dmnchg=1; MUIDB=1C332E1A621D673A2E5823956333661A; _tarLang=default=en; _EDGE_S=SID=294018E5848C60360633157885A261BE; SNRHOP=I=&TS=; SRCHUSR=DOB=20190704&T=1563429442000; SRCHHPGUSR=CW=1853&CH=932&DPR=1&UTC=480&WTS=63699026242; MSCC=1; MSTC=ST=1; _SS=SID=294018E5848C60360633157885A261BE&HV=1563429482',
    }
    to = "en" if check_chinese(query) else 'zh-Hans'
    data = {
        'fromLang': 'auto-detect',
        'text': query,
        'to': to
    }
    response = requests.post(url=post_url, headers=headers, data=data)
    res = response.json()[0]["translations"][0]['text']
    # print(res)
    return res


if __name__ == '__main__':
    query = str(input('请输入翻译的句子：'))
    fanyi_main(query)
