import requests
from bs4 import BeautifulSoup
import chaojiying

# 古诗文网
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

# __VIEWSTATE: myO2Kg7JZABnPtj3rBgZmtz0b0alhZgs9ppx5kf0Qy9LTBsQDa1+LdvNKoo6XibpZ/Uji3h9gIOoLUpnIeQgGATERwITCG4Mh8CGmwuvK8SZ42iiYasoHZ1eDkRvylKjyi/NgOBewTVbZRF7Lpy11/KWEdg=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 1798677862@qq.com
# pwd: 231231231321
# code: nzkh
# denglu: 登录

# 变化
# __VIEWSTATE __VIEWSTATEGENERATOR code 变量
# 难点 1 __VIEWSTATE __VIEWSTATEGENERATOR 一般看不到的数据 在页面源码中
# 在源码中 hidden 获取页面源码 进行解析
# 验证码 code

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

response = requests.get(url=login_url, headers=headers)
# 获取网页源码
content = response.text

# 解析页面源码 获取对应的值
soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenraor = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(__VIEWSTATE)
# print(__VIEWSTATEGENERATOR)

# 验证码
# code url https://so.gushiwen.cn/RandCode.ashx imgCode
code = soup.select("#imgCode")[0].attrs.get('src')
code = fr'https://so.gushiwen.cn{code}'
# 获取验证码的图片验证 下载图片 手动输入
# 有坑 请求了俩次
# imgResponse = requests.get(code)
# requests 里面有个方法session()
session = requests.session()
imgResponse = session.get(code)
# 要使用二进制数据 图片是二进制
imgContent = imgResponse.content
with open('code.png', 'wb') as wp:
    wp.write(imgContent)

# 打码平台
cjy = chaojiying.Chaojiying_Client('1798677862', 'S8MfXe8eRg2ju2.', '948060')
im = open('code.png', 'rb').read()
code_name = cjy.PostPic(im, 1902).get('pic_str')
# 后续可以进行图像识别 ocr
# code_name = input("请输入你的验证码: ")
# print(code)
# print(code_name)

# 组装data 请求参数
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenraor,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1798677862@qq.com',
    'pwd': '2020.0.l',
    'code': code_name,
    'denglu': '登录'
}

# 这里也需要使用session 请求是同一个
login_response = session.post(url=url, headers=headers, data=data)
login_content = login_response.text

with open('login.html', 'w', encoding='utf-8') as fp:
    fp.write(login_content)
    fp.close()

# 难点 隐藏域问题 验证码 必须是同一请求 session
