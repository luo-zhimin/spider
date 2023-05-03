import requests
import json

url = "https://fanyi.baidu.com/sug"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

data = {
    'kw': 'requests'
}

# post 请求不需要编解码 请求参数是data 不需要请求对象的定制
response = requests.post(url=url, headers=headers, data=data)
content = response.text
content = json.loads(content)
print(content)
