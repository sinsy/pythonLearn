# 东方财富api
import requests
import json


class EastMoney:
    Headers = {  # 请求头部
        # "Cookie": COOKIE,
        "Host": "33.push2.eastmoney.com",
        "Content-Type": "application/json;charset=UTF-8",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }
    # 获取可转债数据

    def getConBondData(self):
        try:
            print("获取可转债数据")
            """
            pn:页码第几页
            pz:每页数量
            fid:按什么排序
            po:升序或降序 0 or 1
            """
            url = "http://33.push2.eastmoney.com/api/qt/clist/get?cb=&pn=1&pz=50&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f2&fs=b:MK0354&fields=f1,f152,f2,f3,f12,f13,f14,f227,f228,f229,f230,f231,f232,f233,f234,f235,f236,f237,f238,f239,f240,f241,f242,f26,f243&_=1582171649500"
            r = requests.get(url, headers=self.Headers)
            print(r)
            if r.status_code == 200:
                data = json.loads(r.text)
                result = []
                arr = data.get('data', {}).get('diff', [])
                for i in arr:
                    if i.get('f2') != '-':
                        result.append({
                            'name': i.get('f14'),  # 债券名称
                            'code': i.get('f12'),  # 债券代码
                            'price': i.get('f2'),  # 债券价格
                            'rate': i.get('f3'),  # 涨跌幅度
                            'soldBackPrice': i.get('f239'),  # 回售触发价
                            'buyBackPrice': i.get('f240'),  # 强赎触发价
                            'expireBuyBackPrice': i.get('f241'),  # 到期赎回价
                            'changeStockPrice': i.get('f235'),  # 转股价
                            # 转股价值=正股价/转股价 * 100
                            'changeStockValue': "{:.2f}".format(i.get('f236')),
                            # 转股价值=正股价/转股价 * 100
                            'changeStockValueRate': i.get('f237'),
                            'changeStockDate': i.get('f242'),  # 开始转股日期
                            'pubDate': i.get('f26'),  # 上市日期
                            'stockName': i.get('f234'),  # 股票名称
                            'stockCode': i.get('f232'),  # 股票代码
                            'stockPrice': i.get('f229'),  # 股票价格
                            'stockRate': i.get('f230'),  # 股票涨跌幅

                        })
                return {"code": 0, "data": result}
            else:
                return {"code": -1, "msg": r}
        except requests.exceptions.ConnectionError:
            return {'code': 500, 'msg': '网络连接失败'}
        except requests.exceptions.ConnectTimeout:
            return {'code': 500, 'msg': '连接超时'}
        except requests.exceptions.InvalidURL:
            return {'code': 404, 'msg': '请求链接失效'}
        except:
            return {'code': 500, 'msg': '服务器出错'}
