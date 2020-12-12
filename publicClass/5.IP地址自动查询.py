import requests

url = "https://www.ip.cn/api/index?ip=www.baidu.com&type=1"
r = requests.get(url)
print(r.text)
