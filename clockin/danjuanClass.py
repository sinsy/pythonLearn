# 蛋卷基金api
import requests
import json


class Danjuan:
    def __init__(self, db):
        self.db = db
        self.Headers = {  # 请求头部
            # "Cookie": COOKIE,
            "Host": "danjuanapp.com",
            "Content-Type": "application/json;charset=UTF-8",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        }

    # 获取蛋卷基金指数数据
    def getIndexData(self):
        try:
            url = "https://danjuanapp.com/djapi/index_eva/dj"
            r = requests.get(url, headers=self.Headers)

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
                items = data.get("data", {'item': []}).get('items', {})
                for i in items:
                    code = i["index_code"]
                    # 只返回用户自身保存的指数
                    if code in arr:
                        index = arr.index(code)
                        result["type_"+indexCode[index]["type"]].append(
                            {
                                "name": i["name"],
                                "code": code,
                                "inStock": indexCode[index]['inStock'],
                                "outStock": indexCode[index]['outStock'],
                                "dyr": "{:.2%}".format(i["yeild"]),
                                "ep": "{:.2%}".format(1/i["pe"]),
                                "pe": "{:.2f}".format(i["pe"]),
                                "pe_pos": "{:.2%}".format(
                                    i["pe_percentile"]
                                ),
                                "pb": "{:.2f}".format(i["pb"]),
                                "pb_pos": "{:.2%}".format(
                                    i["pb_percentile"]
                                ),
                                "temperature": "{:.2f}".format(
                                    (i["pb_percentile"] +
                                     i["pe_percentile"])/2*100
                                ),
                                "target": i['eva_type_int']
                            }
                        )
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
# d = Danjuan()
# d.getIndexData()
