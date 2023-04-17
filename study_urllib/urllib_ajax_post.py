# KFC
import urllib.request
import urllib.parse
import json
import math

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    # "Accept": '*/*',
}


# post
def create_request(page=1):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '上海',
        # 动态
        'pageIndex': page,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    return urllib.request.Request(url=url, data=data, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def download(content):
    if content is not None:
        file = open('kfc.json', 'w', encoding='utf-8')
        file.write(content)
        file.close()


def get_page():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '上海',
        # 动态
        'pageIndex': 1,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    r = urllib.request.Request(url=url, data=data, headers=headers)
    rs = urllib.request.urlopen(r)
    con = rs.read().decode('utf-8')
    # print(con)
    return math.ceil(json.loads(con)['Table'][0]['rowcount'] / 10)


if __name__ == '__main__':
    # 正常来说先计算 页 在进行选择
    kfc_address_list = []
    for number in range(1, get_page() + 1):
        request = create_request(number)
        content = get_content(request)
        # print(content)
        # print(json.loads(content))
        kfc_address_list.append(json.loads(content))

    # print(json.dumps(kfc_address_list, ensure_ascii=False))
    download(json.dumps(kfc_address_list, ensure_ascii=False))

    # get_page()
