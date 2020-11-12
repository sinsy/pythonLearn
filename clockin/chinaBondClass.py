# 东方财富api
import requests
import json
from bs4 import BeautifulSoup


class ChinaBond:
    Headers = {  # 请求头部
        # "Cookie": COOKIE,
        "Host": "yield.chinabond.com.cn",
        "Content-Type": "application/json;charset=UTF-8",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }
    # 获取十年国债数据

    def getChinaBondData(self):
        print("获取十年国债数据")
        url = "http://yield.chinabond.com.cn/cbweb-mn/yc/ycDetail?ycDefIds=2c9081e50a2f9606010a3068cae70001&&zblx=txy&&workTime=&&dxbj=&&qxlx=&&yqqxN=&&yqqxK=&&wrjxCBFlag=0&locale=zh_CN"
        r = requests.post(url, headers=self.Headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            json = {}
            for i in soup.select('.tablelist>tr'):
                td = i.find_all('td')
                if len(td) == 2:
                    json[td[0].text] = td[1].text
            return {"code": 0, "data": json.get('10.0y', 3.25)}
        else:
            return {"code": -1, "msg": r}


# c = ChinaBond()
# c.getChinaBondData()
