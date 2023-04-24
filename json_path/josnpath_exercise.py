import urllib.request
import jsonpath
import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1682346623766_108&jsoncallback=jsonp109&action' \
      '=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    'referer': 'https://dianying.taobao.com/',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 替换 读取 -->可以直接进行split 或者 index
content = content.replace('jsonp109(', ' ')
content = content.replace(');', ' ')
content = content.strip()
print(content)
# 下载到本地
with open('city.json', 'w', encoding='utf-8') as f:
    f.write(content)
    f.close()

# 进行读取
cities = json.load(open('city.json', 'r', encoding='utf-8'))
# print(cities)

# 取 regionName
names = jsonpath.jsonpath(cities, '$.returnValue..regionName')
print(names)
