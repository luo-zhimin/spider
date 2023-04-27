# 元素定位
from selenium import webdriver
import time

url = 'https://www.baidu.com'

# safari
# path = '/usr/bin/safaridriver'
# browser = webdriver.Safari(executable_path=path)
path = './chromedriver_mac_arm64/chromedriver'
browser = webdriver.Chrome(executable_path=path)

browser.get(url=url)

# input = browser.find_element(by='id', value='su')

# 获取标签的属性
# print(input.get_attribute('class'))
# # 百度一下
# print(input.get_attribute('value'))
# # input 获取标签的名字
# print(input.tag_name)
# # element text <xxx>
# a = browser.find_element(by='link text', value='新闻')
# print(a.text)

# 进行交互
# 获取文本框的对象
input_text = browser.find_element(by='id', value='kw')
time.sleep(2)
# 文本框中 发送关键字
input_text.send_keys('刘亦菲')
time.sleep(2)
# 获取百度一下按钮
# 检索
button = browser.find_element(by='id', value='su')
button.click()
time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)

# 进行下一页操作
next_page = browser.find_element(by='xpath', value='//a[@class="n"]')
# 点击下一页
next_page.click()
time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)

# 回到第二页
browser.forward()

time.sleep(3)

# 退出
browser.quit()
