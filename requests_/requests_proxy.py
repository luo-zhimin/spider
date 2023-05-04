import requests

url = 'http://ip234.in/ip.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
}

# params = {
#     'wd': 'ip'
# }

# proxy = {
#     'http': '104.26.14.126:80'
# }

response = requests.get(url=url, headers=headers)
content = response.text

with open('proxy.html', 'w', encoding='utf-8') as f:
    f.write(content)
    f.close()

print(content)
