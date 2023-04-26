# exercise 解析星巴克数据
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')
# xpath -> //ul/li/a/strong name
# //ul/li/a[@class="thumbnail"]/@href
name_list = soup.select('ul li a strong')
for name in name_list:
    print(name.get_text())
# print(name_list)
img_list = soup.select('ul li a[class="thumbnail"]')
# print(img_list)
for img in img_list:
    print(img['href'])
# print(soup)

# print(content)
