# 下载前10页
import json
import math
import urllib.request
import urllib.parse

# page 1 2 3 4....
# start 0 20 40 60....
# (page-1)*20

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
}


def creat_request(start):
    base_url = 'https://movie.douban.com/j/chart/top_list?'
    query_data = {
        'type': 5,
        'interval_id': '100:90',
        # start 动态
        'start': start,
        'limit': 20,
    }
    url = base_url + urllib.parse.urlencode(query_data)
    print(f'url={url}')
    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def download(content, url_content):
    download_content(content)
    print(url_content is not None)
    download_url(url_content)


def download_content(content):
    if content is not None:
        f = open(f'first_douban_movie.json', 'w', encoding='utf-8')
        f.write(content)
        f.close()


def download_url(url_content):
    if url_content is not None:
        f = open(f'first_douban_url_title.json', 'w', encoding='utf-8')
        f.write(url_content)
        f.close()


# page 动态获取
def get_page() -> int:
    count_url = 'https://movie.douban.com/j/chart/top_list_count?type=5&interval_id=100%3A90'
    count_request = urllib.request.Request(url=count_url, headers=headers)
    count_response = urllib.request.urlopen(count_request)
    count_count = count_response.read().decode('utf-8')
    print(f'total = {json.loads(count_count)["total"]}')
    return math.ceil(int(json.loads(count_count)['total']) / 20)


result = []
url_list = []
for p in range(1, get_page() + 1):
    # for p in range(1, 2):
    print(f"当前第{p}页")
    request = creat_request((p - 1) * 20)
    content = get_content(request)
    # 准备组装url_title dict list
    content_list = json.loads(content)
    for cl in content_list:
        url_list.append({'title': cl['title'], 'url': cl['url']})
    # print(json.loads(content))
    # 组装大的json对象
    result.append(json.loads(content))
    # 写入文件 进行保存
    # download(content, p)

result = json.dumps(result, ensure_ascii=False)
url_list = json.dumps(url_list, ensure_ascii=False)
# print(result)
# print(url_list)
# write
download(result, url_list)

if __name__ == '__main__':
    pass
    # print(get_page())
    # print(math.ceil(18.9))
