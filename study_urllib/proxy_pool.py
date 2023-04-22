# 代理池
import random
import urllib.request

proxies_pool = [
    {
        'http': '183.236.232.160:8080'
    }, {
        'http': '116.9.163.205:58080'
    }, {
        'http': '117.114.149.66:55443'
    }, {
        'http': '61.164.39.68:53281'
    },
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

url = 'https://www.baidu.com/s?wd=ip'

proxies = random.choice(proxies_pool)

# 定制对象
request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

# 保存到本地
with open('proxy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(proxies)
