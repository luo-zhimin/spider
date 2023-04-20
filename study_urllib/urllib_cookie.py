# 微博Cookie登陆 数据采集得时候 绕过登陆 进入采集

import urllib.request
import urllib.error

# 替换成您自己的Cookie
cookie = 'SUB=_2A25JOssBDeRhGeNG4lcQ9yzLwjqIHXVqxNVJrDV6PUJbkdANLUGnkW1NSuKXQn7TgkzBofpYhHuMoAZ8XrC3QZSy; ' \
         '_T_WM=57799680770; MLOGIN=1; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=luicode=20000174&uicode=20000174; ' \
         'XSRF-TOKEN=9dd710; mweibo_short_token=4487276b72'

# 替换成您自己的用户ID
user_id = '5895172796'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    'referer': 'https://m.weibo.cn/profile/5895172796',
    'X-XSRF-TOKEN': '9dd710',
    'cookie': cookie,
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same - origin'
}

# 构造请求URL
url = f'https://m.weibo.cn/profile/info?uid={user_id}'

request = urllib.request.Request(url=url, headers=headers)

try:
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    urllib.request.urlretrieve(url=url, filename='weibo.html')
    print(content)
except urllib.error.HTTPError as e:
    print(e)
