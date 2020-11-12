import requests
import json
import pandas as pd

###########################################################
HOST = "www.lixinger.com"
cookieFilename = "lixinren/cookie.txt"  # cookie文件存储

cookie = open(cookieFilename, "r").read()
print("cookie%s" % cookie)
Headers = {  # 请求头
    "Cookie": cookie,
    "Host": HOST,
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}


def login():
    data = {}  # 用户信息
    res = requests.post("https://www.lixinger.com/api/login/by-account", data)
    print("%s" % (res.text))
    print("%s" % (res))
    if res.status_code == 200:
        m_cookie = res.headers["Set-Cookie"].split(";")[0]
        f = open(cookieFilename, "w")
        f.write(m_cookie)
        print(m_cookie)
        Headers["Cookie"] = m_cookie
        print(Headers["Cookie"])

    else:
        print("登录连接不成功%s" % (res.status_code))


def getData():
    p = {
        "metricNames": ["pe_ttm", "pb", "ps_ttm", "dyr", "cpc"],
        "granularities": ["y_20"],
        "metricTypes": ["weightedAvg"],
        "source": "all",
        "series": "all",
        "stockFollowedType": "all",
    }
    r = requests.post(
        "https://www.lixinger.com/api/analyt/stock-collection/price-metrics/indices/latest",
        json=p,
        headers=Headers,
    )
    if r.status_code == 200:
        data = json.loads(r.text)
        # print(data)

        df = pd.DataFrame(data)
        print(df)
    elif r.status_code == 401:
        print("未登录")
    else:
        print(r)


def getUserInfo():
    res = requests.get(
        "https://www.lixinger.com/api/user/users/current", headers=Headers
    )
    if res.status_code == 200:
        getData()
    else:
        print("失败")


if __name__ == "__main__":
    getUserInfo()

