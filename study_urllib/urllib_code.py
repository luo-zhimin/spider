"""
    编码集 Unicode
"""
import urllib.request
import urllib.parse
import json

# 获取源码 https://www.baidu.com/s?wd=%E5%88%98%E4%BA%A6%E8%8F%B2
# url = 'https://www.baidu.com/s?wd=' + urllib.parse.quote('刘亦菲')
# https://m.baidu.com/ssid=c008c2e4b6fec7a7e7f4g9f1401000000/s?word=%E5%88%98%E4%BA%A6%E8%8F%B2
# quote
# url = 'https://m.baidu.com/ssid=c008c2e4b6fec7a7e7f4g9f1401000000/s?word=' + urllib.parse.quote('刘亦菲')

# urlencode
# data = {
#     'wd': "刘亦菲",
#     'sex': '女',
#     'location': '美国'
# }
#
# url = 'https://m.baidu.com/ssid=c008c2e4b6fec7a7e7f4g9f1401000000/s?' + urllib.parse.urlencode(data)
# name = urllib.parse.quote('刘亦菲')
# print(name)
# url = url + name
# print(urllib.parse.urlencode(data))

# post
# 百度翻译 transform
url = 'https://fanyi.baidu.com/sug'
# url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

# 请求对象定制
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
}

data = {
    'kw': 'different'
}
# post请求参数必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)

# 定制
# get
# request = urllib.request.Request(url=url, headers=headers)
# post
request = urllib.request.Request(url=url, data=data, headers=headers)
# todo 请求 如果是定制请求 urlopen需要把定制的request传入进去
# response = urllib.request.urlopen(url=url)
response = urllib.request.urlopen(request)
print(url)
# 百度安全验证 需要进行反爬
content = response.read().decode('utf-8')
# str -> json
content = json.loads(content)
# print(type(content))
print(content)
