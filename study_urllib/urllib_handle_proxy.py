import urllib.request

# url = 'https://whoer.net/zh'
url = 'https://www.baidu.com/s?wd=ip'
# url = 'https://www.ez2o.com/App/Net/IP'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# response = urllib.request.urlopen(request)
# handler
# get handler
# handler = urllib.request.HTTPHandler()
proxies = {
    'http': '183.236.232.160:8080'
}
handler = urllib.request.ProxyHandler(proxies=proxies)
# get opener
opener = urllib.request.build_opener(handler)
# open
response = opener.open(request)

content = response.read().decode('utf-8')

# 保存到本地
with open('proxy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(content)
