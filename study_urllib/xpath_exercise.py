# 下载图片
import urllib.request
from lxml import etree
import os
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36'
}


def create_request(page):
    # url = None
    if page == 1:
        url = f'https://sc.chinaz.com/tupian/richutupian.html'
    else:
        url = f'https://sc.chinaz.com/tupian/richutupian_{page}.html'
    print(url)
    # 最好进行代理 使用多个ip pool 进行下载 不然会连接失败
    request = urllib.request.Request(url=url, headers=headers)
    return urllib.request.urlopen(request)


def get_tree(response):
    return etree.HTML(response.read().decode('utf-8'))


def tree_xpath(tree):
    return tree.xpath('//div[@class="tupian-list com-img-txt-list"]//img/@data-original')


def tree_xpath_alt(tree):
    return tree.xpath('//div[@class="tupian-list com-img-txt-list"]//img/@alt')


l = "./study_urllib"


def down_load(img_result):
    # 创建文件夹
    i = 0
    for im in img_result:
        url = im.get('url')
        title = im.get('title')
        # print(url)
        urllib.request.urlretrieve(url=url, filename='../study_urllib/..img/' + str(i) + "_" + title + '.jpg')
        i += 1


def creat_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print(f"{path}已经存在")


img_result = []
if __name__ == '__main__':
    for page in range(1, 11):
        response = create_request(page)
        tree = get_tree(response)
        img_list = tree_xpath(tree)
        art_list = tree_xpath_alt(tree)
        if len(img_list) > 0:
            i = 0
            for img in img_list:
                # d = {"url": f'"https://"{img}', 'title': art_list[i]}
                img_result.append({"url": f'https:{img}', 'title': art_list[i]})
                i += 0

creat_directory('../study_urllib/../img')
print(len(img_result))
# print(img_result)
down_load(img_result)
