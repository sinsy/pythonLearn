import requests

url = "http://www.baidu.com"

try:
    kv = {"user-agent": "Mozilla/5.0"}
    params = {"wd": "Python"}
    r = requests.get(url, headers=kv, params=params)
    r.raise_for_status()  # 对返回状态抛出异常
    r.encoding = r.apparent_encoding
    print(len(r.text))
    # print(r.text)
except:
    print("爬取失败")
