# ajax get
import urllib.request
import urllib.parse

# 获取豆瓣电影的第一页数据 并且存储起来
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
url = 'https://movie.douban.com/j/chart/top_list?'
# 构建data 多参数
query_data = {
    'type': 5,
    'interval_id': '100:90',
    # 'action': '',
    'start': 0,
    'limit': 20,
}

url = url + urllib.parse.urlencode(query_data)

print(f"really download url={url}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 写入文件 进行保存
f = open('first_douban_movie_page.json', 'w', encoding='utf-8')
f.write(content)
f.close()

print(type(content))
print(content)
