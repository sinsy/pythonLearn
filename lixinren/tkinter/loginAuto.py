#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox
import requests
import json
###########################################################
HOST = 'www.lixinger.com'
cookieFilename = 'stock/cookie.txt' #cookie文件存储
cookie = open(cookieFilename, 'r').read()
print('cookie%s'%cookie)
Headers = { #请求头
    "Cookie":cookie,
    "Host":HOST,
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}
global frame
def login():
    data = {}  # 用户信息
    res = requests.post("https://www.lixinger.com/api/login/by-account", data)
    print("%s" % (res.text))
    print("%s" % (res))
    if res.status_code == 200:
        m_cookie = res.headers["Set-Cookie"].split(';')[0]
        f = open(cookieFilename, 'w')
        f.write(m_cookie)
        print(m_cookie)
        Headers["Cookie"] = m_cookie
        print(Headers["Cookie"])

    else:
        print("登录连接不成功%s" % (res.status_code))

def getROICData():
    # arr = frame.entry1.get().split(',')
    # print(frame)
    p = {
        "stockIds":[300146, 639],
        "startDate":"2010-06-08T16:00:00.000Z",
        "endDate":"2019-06-08T16:00:00.000Z",
        "granularities":["y"],
        "metricNames":["profitStatement.fe","profitStatement.tp","balanceSheet.tca","balanceSheet.fa","balanceSheet.cip","balanceSheet.cabb","balanceSheet.lwi","cashFlow.ncffoa","metrics.fcf"],
        "expressionCaculateTypes":["t","t_o","t_y2y","t_c2c","c","c_o","c_y2y","c_c2c","c_2y","ttm","ttm_y2y","ttm_c2c"]
    }
    r = requests.post('https://www.lixinger.com/api/analyt/company/fs-metrics/list', json=p, headers=Headers)
    print("%s" % (r))
    print("%s" % (r.text))
    if r.status_code == 200:
        tkinter.messagebox.showinfo("messagebox", '数据获取成功')
        data = json.loads(r.text)
        with open('json.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
    elif r.status_code == 401:
        login()
    else:
        tkinter.messagebox.showinfo("messagebox", r.status_code)

class MainWindow:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.geometry("500x500")
        self.label1 = tkinter.Label(self.top, text="股票代码:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tkinter.Entry(self.top)
        self.entry1.grid(row=0, column=1)
        self.B = tkinter.Button(self.top, text="获取数据", command=getROICData)
        self.B.grid(row=3, column=0)
        self.top.mainloop()

getROICData()

frame = MainWindow()