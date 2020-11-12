# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from lixinrenClass import Lixinren
from danjuanClass import Danjuan
from eastmoneyClass import EastMoney
from mongodbClass import MongoDB


def getIndexData():
    result = []
    result1 = lixinren.getIndexData()
    result2 = danjuan.getIndexData()

    if result1['code'] == 0:
        for i in result1['data']:
            result.extend(result1['data'][i])
    if result2['code'] == 0:
        for i in result2['data']:
            result.extend(result2['data'][i])
    for i in result:
        i['date'] = date
    return {'code': result1['code'], 'data': result}


def aps_byday():
    print(date, '开始')
    result = getIndexData()
    if(result.get('code') == 0):
        mongoDB.updateIndexDataByDay(result.get('data'))
        print(date, '插入数据---->开始')
    else:
        print(date, '获取数据---->失败')


date = datetime.datetime.now().strftime('%Y-%m-%d')
mongoDB = MongoDB()
lixinren = Lixinren(mongoDB)
danjuan = Danjuan(mongoDB)

scheduler = BlockingScheduler()
scheduler.add_job(aps_byday,  'cron', minute=2,
                  hour=23, second=0)
# scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
scheduler.start()
