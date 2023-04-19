# 微博Cookie登陆 数据采集得时候 绕过登陆 进入采集

import urllib.request
import urllib.parse
import urllib.error

url = 'https://m.weibo.cn/profile/info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
    'cookie': 'WEIBOCN_FROM=1110006030; SUB=_2A25JOssBDeRhGeNG4lcQ9yzLwjqIHXVqxNVJrDV6PUJbkdANLUGnkW1NSuKXQn7TgkzBofpYhHuMoAZ8XrC3QZSy; _T_WM=57799680770; MLOGIN=1; XSRF-TOKEN=d582e8; mweibo_short_token=a65fb62c77; M_WEIBOCN_PARAMS=luicode=20000174&uicode=20000174'
}

request = urllib.request.Request(url=url, headers=headers)

try:
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    urllib.request.urlretrieve(url=url, filename='weibo.html')
    print(content)
except urllib.error.HTTPError as e:
    print(e)
