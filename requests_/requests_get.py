import urllib.request

import requests

# urllib

url = "https://www.baidu.com/s"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

data = {
    'wd': '上海'
}

# url = > 请求路径 中的?号可以加也可以不加
# args => 字典
# params => 参数 无需 unlencode编码 不需要请求对象定制 requests
response = requests.get(url=url, params=data, headers=headers)

print(response.text)

# ret = urllib.request.Request(headers=headers, url=url)
#
# response = urllib.request.urlopen(ret)
#
# print(response.read().decode('utf-8'))
