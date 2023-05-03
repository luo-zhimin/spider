import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型 6个属性
# requests.models.Response
print(type(response))
# 设置编码格式
response.encoding = 'utf-8'
# string data -> http
print(response.text)
# 返回url地址
print(response.url)
# binary data
print(response.content)
# response code
print(response.status_code)
# headers
print(response.headers)
