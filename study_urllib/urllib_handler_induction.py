# 使用handler 访问百度
import urllib.request

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
}

request = urllib.request.Request(url=url, headers=headers)
# 老版本
# response = urllib.request.urlopen(url=url)
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')
#
# print(content)

# 新版本
# handle build_opener open
# 获取handle对象
handle = urllib.request.HTTPHandler()

# 获取opener
opener = urllib.request.build_opener(handle)

# 调用open
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
