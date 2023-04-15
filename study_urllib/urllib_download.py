"""
    spider download
"""
from urllib import request
import urllib

# 下载网页
url_page = 'http://www.baidu.com'
# urlretrieve() url -> 下载的路径 filename文件名字
request.urlretrieve(url=url_page, filename='baidu.html')
# 下载图片
url_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrmjig8ck_45Xvv0ahPOThcseYczNG8KXv5g&usqp=CAU'
request.urlretrieve(url=url_image, filename='LiuYiFei.jpg')
# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mfuf163rfmkn36i7/sc/cae_h264_nowatermark/1624963807340099361/mda' \
            '-mfuf163rfmkn36i7.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1681549832-0-0' \
            '-e4b326f8997c4dbb81ed64bddf1bfb72&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=2432200863&vid' \
            '=10554454971571011271&abtest=107353_1-109159_2&klogid=2432200863'
request.urlretrieve(url=url_video, filename='video.mp4')

# 请求对象的定制
url = 'https://baidu.com'

# url https==>ssl

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36'
}
# 请求对象定制 因为urlopen里面不可使用字典
# 因为参数顺序问题 不可以直接写 需要关键字传参
request = request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
