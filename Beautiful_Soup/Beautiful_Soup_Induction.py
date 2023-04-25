# induction
from bs4 import BeautifulSoup

# 创建对象
soup = BeautifulSoup(open('beautifulSoup.html'), 'lxml')

# 根据标签名查找节点
# 找到是第一个符合条件的数据
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的函数
# find
# 找到是第一个符合条件的数据
# print(soup.find('a'))
# title find
# print(soup.find('a', title='baidu'))
# class_ find html class because class is keywords in python
# print(soup.find('a', class_='shop'))

# find_all
# find all return list
# print(soup.find_all('a'))
# find any element need potting array
# print(soup.find_all(['a', 'span']))
# find limit number
# print(soup.find_all('li', limit=2))

# select(推荐)
# return array
print(soup.select('a'))
# 可以通过 . 代表class 类选择器
print(soup.select('.shop'))
# id -> #xx
print(soup.select('#zs'))
# 属性选择器 li[id] -> 找到li里面有id的
print(soup.select('li[id]'))
# li[id="ls"] id=>xx find
print(soup.select('li[id="ls"]'))
# 层级选择器
# 后代选择
print(soup.select('div li'))
# 子代选择
# 注意：bs4中可以不加空格
print(soup.select('div > ul > li'))
