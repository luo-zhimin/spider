"""
    初识 urllib
"""

# 使用urllib获取百度首页源码
import urllib.request

# 定义一个url 你需要访问的地址·
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(url=url)

# 获取响应的源码
# read 返回的是字节形式的二进制数据
# 将二进制数据转换为字符串 二进制->字符串 [解码] decode('编码格式')
content = response.read().decode('utf-8')

# 打印数据
print(content)
