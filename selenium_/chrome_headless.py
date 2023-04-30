from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 封装handlers
def share_browser():
    # todo 不可以有特色符号  ->source error [/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome]
    path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    chrome_options.binary_location = path
    return webdriver.Chrome(chrome_options=chrome_options)


browser = share_browser()
url = 'https://www.baidu.com'
browser.get(url=url)

browser.save_screenshot("baidu.png")
