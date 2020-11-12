#! /usr/bin/python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.escape import json_encode
from lixinrenClass import Lixinren
from danjuanClass import Danjuan
from eastmoneyClass import EastMoney
from chinaBondClass import ChinaBond
from mongodbClass import MongoDB


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """get请求"""
        a = self.get_argument("a")
        b = self.get_argument("b")
        c = int(a) + int(b)
        self.write("c=" + str(c))


class loginHandler(tornado.web.RequestHandler):
    def get(self):
        # name = self.get_argument("name")
        # password = self.get_argument("password")
        result = lixinren.login()
        self.write(json_encode(result))


def getIndexData():
    result = {
        "type_pb": [],
        "type_pe_pb": [],
        "type_ep": [],
        "type_danjuan": []
    }
    result1 = lixinren.getIndexData()
    result2 = danjuan.getIndexData()
    if result1['code'] == 0:
        result = result1['data'].copy()
    if result2['code'] == 0:
        for i in result:
            result[i].extend(result2['data'][i])
    result["type_pe_pb"].sort(
        key=lambda x: float(x["temperature"]))
    result["type_ep"].sort(key=lambda x: float(
        x["ep"].strip('%')), reverse=True)
    result["type_pb"].sort(key=lambda x: float(x["pb"]))
    result["type_danjuan"].sort(key=lambda x: float(x["target"]))
    return {'code': result1['code'], 'data': result}


class getIndexDataHandle(tornado.web.RequestHandler):
    def get(self):
        result = getIndexData()
        self.write(json_encode(result))


class getBankDataHandle(tornado.web.RequestHandler):
    def get(self):
        result = lixinren.getBankData()
        self.write(json_encode(result))


class getConBondDataHandle(tornado.web.RequestHandler):
    def get(self):
        result = eastMoney.getConBondData()
        self.write(json_encode(result))


class getChinaBondDataHandle(tornado.web.RequestHandler):
    def get(self):
        result = chinaBond.getChinaBondData()
        self.write(json_encode(result))


class getInvestRecordDataHandle(tornado.web.RequestHandler):
    def get(self):
        sort = self.get_argument("sort")
        result = mongoDB.getInvestRecord({'sort': sort})
        self.write(json_encode({'code': 0, 'data': result}))


mongoDB = MongoDB()
lixinren = Lixinren(mongoDB)
danjuan = Danjuan(mongoDB)
eastMoney = EastMoney()
chinaBond = ChinaBond()
application = tornado.web.Application(
    [
        (r"/add", MainHandler),  # 测试
        (r"/login", loginHandler),  # 登录
        (r"/getIndexData", getIndexDataHandle),  # 指数数据
        (r"/getConBondData", getConBondDataHandle),  # 可转债债数据
        (r"/getChinaBondData", getChinaBondDataHandle),  # 十年国债收益率
        (r"/getBankData", getBankDataHandle),  # 银行数据
        # 定投记录的获取 {sort:'date or name'}
        (r"/getInvestRecordData", getInvestRecordDataHandle),
    ]
)


if __name__ == "__main__":
    application.listen(8868)
    tornado.ioloop.IOLoop.instance().start()
