# xpath lxml
# 解析
from lxml import etree
import urllib.request

# 解析 1.本地文件
# tree = etree.parse('../pageStructure.html')
# 基本语法
# tree.xpath(xpath路径)

# 查找ul>li
# li_list = tree.xpath('//ul/li')
# print(len(li_list))
# print(li_list)

# 查找所有有id的属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')
# print(li_list)

# 找到id为first的标签 todo 注意引号问题
# li_list = tree.xpath('//ul/li[@id="first"]/text()')
# print(li_list)

# 查找到id为first的li标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="first"]/@class')
# print(li_list)

# 模糊查询 查询id中包含r的标签
# li_list = tree.xpath('//ul/li[contains(@id,"r")]/text()')
# print(li_list)

# starts-with 查询id中已t开头的
# li_list = tree.xpath('//ul/li[starts-with(@id,"s")]/text()')
# print(li_list)

# 逻辑运算

# print(tree)

# 解析 2.服务器响应的数据 response.read().decode('utf-8') etree.html()
# 获取百度网站的百度一下
# 获取百度首页的源码
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url=url)
tree = etree.HTML(response.read().decode('utf-8'))
# class="btn self-btn bg s_btn"
h_input = tree.xpath('//div[@id="head_wrapper"]/div/div/form//input[@id="su"]/@value')
print(len(h_input))
print(h_input)
# print(tree)
