"""
    urllib 一个类型 6个方法
"""
from urllib import request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = request.urlopen(url)

# 一个类型6个方法
# <class 'http.client.HTTPResponse'>
# print(type(response))

# 按照一个字节字节的读取
# content = response.read()
# print(content)

# read(number) -> 读取多少个字节
# response.read(5)

# 按照行读取 读取一行
# content = response.readline()
# print(content)

# 读取全部行
# content = response.readlines()
# print(content)

# response.getcode() 获取返回状态码 200->ok
# print(response.getcode())

# response.geturl() 返回的url地址 读取
# print(response.geturl())

# response.getheaders() 获取请求头
print(response.getheaders())
