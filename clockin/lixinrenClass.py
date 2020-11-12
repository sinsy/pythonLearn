import json
import requests


class Lixinren:
    def __init__(self, db):
        self.db = db
        self.HOST = "www.lixinger.com"
        params = self.db.getAccount()
        self.COOKIE = params["cookie"]
        self.Headers = {  # 请求头部
            "Cookie": self.COOKIE,
            "Host": self.HOST,
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        }
    # 登录函数

    def login(self):
        try:
            params = self.db.getAccount()
            data = {"uniqueName": params["name"],
                    "password": params["password"]}  # 用户信息
            res = requests.post(
                "https://www.lixinger.com/api/login/by-account", data)
            if res.status_code == 200:
                m_cookie = res.headers["Set-Cookie"].split(";")[0]
                self.Headers["Cookie"] = m_cookie
                self.db.updateAccount({"type": "lixinren", "cookie": m_cookie})
                return {"code": 0, "data": {"cookie": m_cookie}}
            else:
                msg = "登录连接不成功%s" % (res.status_code)
                return {"code": -1, "msg": msg}
        except requests.exceptions.ConnectionError:
            return {'code': 500, 'msg': '网络连接失败'}
        except requests.exceptions.ConnectTimeout:
            return {'code': 500, 'msg': '连接超时'}
        except requests.exceptions.InvalidURL:
            return {'code': 404, 'msg': '请求链接失效'}
        except:
            return {'code': 500, 'msg': '服务器出错'}
    # 指数信息函数

    def getIndexData(self):
        try:
            year = "y_10"
            p = {
                "metricNames": ["pe_ttm", "pb", "ps_ttm", "dyr", "cpc"],
                "granularities": [year],
                "metricTypes": ["weightedAvg"],
                "source": "all",
                "series": "all",
                "stockFollowedType": "all",
            }
            r = requests.post(
                "https://www.lixinger.com/api/analyt/stock-collection/price-metrics/indices/latest",
                json=p,
                headers=self.Headers,
            )
            if r.status_code == 200:
                result = {
                    "type_pb": [],
                    "type_pe_pb": [],
                    "type_ep": [],
                    "type_danjuan": []
                }
                data = json.loads(r.text)
                # 获取用户的默认指数代码
                indexCode = self.db.getDefaultSetting()["indexCode"]
                arr = []
                for i in indexCode:
                    arr.append(i["code"])
                for i in data:
                    code = i["stockCode"] + "." + i["exchange"]
                    # 只返回用户自身保存的指数
                    if code in arr:
                        index = arr.index(code)
                        result["type_"+indexCode[index]["type"]].append(
                            {
                                "name": i["name"],
                                "code": code,
                                "inStock": indexCode[index]['inStock'],
                                "outStock": indexCode[index]['outStock'],
                                "dyr": "{:.2%}".format(i["dyr"]["weightedAvg"]),
                                "ep": "{:.2%}".format(1/i["pe_ttm"]["weightedAvg"]),
                                "pe": "{:.2f}".format(i["pe_ttm"]["weightedAvg"]),
                                "pe_pos": "{:.2%}".format(
                                    i["pe_ttm"][year]["weightedAvg"]["latestValPos"]
                                ),
                                "pb": "{:.2f}".format(i["pb"]["weightedAvg"]),
                                "pb_pos": "{:.2%}".format(
                                    i["pb"][year]["weightedAvg"]["latestValPos"]
                                ),
                                "temperature": "{:.2f}".format(
                                    (i["pb"][year]["weightedAvg"]["latestValPos"] +
                                     i["pe_ttm"][year]["weightedAvg"]["latestValPos"])/2*100
                                )
                            }
                        )

                return {"code": 0, "data": result}
            elif r.status_code == 401:
                msg = "登录连接不成功%s" % (r.status_code)
                return {"code": 401, "msg": msg}
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
    # 银行数据信息

    def getBankData(self):
        p = {"areaCode": "cn", "fsTableType": "bank", "fsQuarterDate": "latest", "stockId": 2000000070101,
             "pageIndex": 0, "pageSize": 100, "sortName": "latest_metrics.stockPriceMetrics.dyr", "sortOrder": "desc"}
        try:
            r = requests.post(
                "https://www.lixinger.com/api/analyt/stock-collection/constituents/default-metrics",
                json=p,
                headers=self.Headers,
            )
            print(r)
            if r.status_code == 200:
                data = json.loads(r.text)
                arr = data.get('metricsTableData', {}).get('items', [])
                result = []
                for i in arr:
                    latest_metrics = i.get('latest_metrics', {}).get(
                        'stockPriceMetrics', {})
                    result.append({
                        'name': i.get('name', ''),
                        "code": i.get('stockCode', ''),
                        "pe": "{:.2f}".format(latest_metrics.get('d_pe_ttm', '')),
                        'pb': "{:.2f}".format(latest_metrics.get('pb_wo_gw', '')),
                        'dyr': "{:.2%}".format(latest_metrics.get('dyr', '')),
                        'price': "{:.2f}".format(latest_metrics.get('sp', '')),


                    })
                return {"code": 0, "data": result}
            elif r.status_code == 401:
                msg = "登录连接不成功%s" % (r.status_code)
                return {"code": 401, "msg": msg}
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
