import urllib.request

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url=url)
content = response.read().decode('utf-8')
# print(content)

# use selenium
# 导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建浏览器操作对象
# myChrome version is 112.0.5615.137
path = './chromedriver_mac_arm64/chromedriver'
service = Service(path)
browser = webdriver.Chrome(service=service)

# 访问网站
browser.get(url=url)

# 获取网页源码
content = browser.page_source
print(content)
