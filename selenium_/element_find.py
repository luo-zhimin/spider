# 元素定位
from selenium import webdriver

url = 'https://www.baidu.com'

path = './chromedriver_mac_arm64/chromedriver'
log_path = './chromeLog/log'
browser = webdriver.Chrome(executable_path=path, service_log_path=log_path)

browser.get(url=url)

# content = browser.page_source
# print(content)

# 元素定位
# by='id'：使用id属性查找元素
# by='name'：使用name属性查找元素
# by='xpath'：使用XPath表达式查找元素
# by='link text'：使用链接文本查找元素
# by='partial link text'：使用部分链接文本查找元素

# 通过id寻找
# button = browser.find_element(by='id', value="su")
# print(button)

# 通过name寻找
# button = browser.find_element(by='name', value="wd")
# print(button)

# xpath 获取对象
# string
# button = browser.find_element(by='xpath', value="//input[@id='su']")
# array
# button = browser.find_elements(by='xpath', value="//input[@id='su']")
# print(button)

# 标签名字 获取对象
# button = browser.find_elements(by='tag name', value="input")
# print(button)

# button = browser.find_elements(by='css selector', value="#su")
# print(button)

# 使用链接文本查找元素 超链接
button = browser.find_elements(by='link text', value="地图")
print(button)
