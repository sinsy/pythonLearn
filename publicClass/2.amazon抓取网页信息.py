import requests

url = "https://www.amazon.com/-/zh/dp/B00WR23X5I/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=55ca1a29-07df-438e-9133-82fa08d479b7&pf_rd_r=1YR4B4QRD1822HB7P90E&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1487012920&rnid=16225007011&s=computers-intl-ship&sr=1-1"
# r = requests.get(url)
# print(r.status_code)

# 模拟浏览器对亚马逊发出请求
try:
    kv = {"user-agent": "Mozilla/5.0"}
    r = requests.get(url, headers=kv)
    r.raise_for_status()  # 对返回状态抛出异常
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
