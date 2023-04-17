import urllib.request
import urllib.error

url = 'https://blog.csdn.net/youhebuke225/article/details/1250473821'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}
try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print("系统正在升级....")
except urllib.error.URLError:
    print('系统正在升级....')
