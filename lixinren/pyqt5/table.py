#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time,datetime
import requests
import json
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QGridLayout, QApplication, QTableWidget, QHeaderView, QTableWidgetItem, QHBoxLayout,
                             QVBoxLayout, QDateEdit, QComboBox )
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtCore import QDate
HOST = 'www.lixinger.com'
cookieFilename = 'lixinren/cookie.txt'  # cookie文件存储
cookie = open(cookieFilename, 'r').read()
print('cookie%s' % cookie)

Headers = {  # 请求头
    "Cookie": cookie,
    "Host": HOST,
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}
yearArr = [5,6,7,8,9,10,11,12,13,14,15]

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.hightingColor = QColor(255, 202, 0)
        self.blueColor = QColor(0, 186, 255)
        self.greenColor = QColor(0, 147, 44)
        self.redColor = QColor(255, 0, 0)
        self.setGeometry(100, 100, 1250, 800)
        self.setWindowTitle('宝大爷神器')
        self.show()
        self.mainUI()
        self.getUserInfo()
        # self.clearUI()
        # self.loginUI()

    def mainUI(self):
        self.box = QVBoxLayout()
        self.box.setSpacing(5)
        self.setLayout(self.box)

    def dataUI(self):
        self.box1 = QHBoxLayout()
        self.code = QLabel('股票代码')
        self.box1.addWidget(self.code)
        self.codeEdit = QLineEdit()
        self.codeEdit.setText('600519')
        self.box1.addWidget(self.codeEdit)

        self.year = QLabel('回报年限')
        self.yearEdit = QComboBox()
        for i in yearArr:
            self.yearEdit.addItem(str(i))
        self.yearEdit.setCurrentIndex(5)
        self.box1.addWidget(self.year)
        self.box1.addWidget(self.yearEdit)

        # 同行年限
        self.peerYear = QLabel('同行年限')
        self.peerYearEdit = QComboBox()
        for i in yearArr:
            self.peerYearEdit .addItem(str(i))
        self.peerYearEdit.setCurrentIndex(2)
        self.box1.addWidget(self.peerYear)
        self.box1.addWidget(self.peerYearEdit)

        #开始日期
        self.date = QLabel('开始日期')
        self.box1.addWidget(self.date)
        self.dateEdit = QDateEdit(QDate.currentDate().addDays(-365*10), self)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.box1.addWidget(self.dateEdit)

        #结束日期
        self.dateEnd = QLabel('结束日期')
        self.box1.addWidget(self.dateEnd)
        self.dateEditEnd = QDateEdit(QDate.currentDate(), self)
        self.dateEditEnd.setCalendarPopup(True)
        self.dateEditEnd.setDisplayFormat("yyyy-MM-dd")
        self.box1.addWidget(self.dateEditEnd)

        self.searchButton = QPushButton("估值")
        self.searchButton.clicked.connect(self.searchEvent)
        self.box1.addWidget(self.searchButton)


        self.peerButton = QPushButton("同行对比")
        self.peerButton.clicked.connect(self.searchPeerEvent)
        self.box1.addWidget(self.peerButton)
        self.box.addLayout(self.box1)

        self.box2 = QHBoxLayout()
        self.tips = QLabel('例子：以逗号隔开（000123,000333,000345）')
        self.box2.addWidget(self.tips)
        self.stockInfo = QLabel('')
        self.box2.addWidget(self.stockInfo)
        self.box.addLayout(self.box2)


        self.table = QTableWidget(30, 15)
        self.table.setStyleSheet(
            "QHeaderView::section {background-color:#f3f3f3;color: black;padding-left: 4px;border: 1px dotted #dddddd;}");  # 设置表头字体，颜色，模式
        self.box.addWidget(self.table)
        self.tipsUI()
    def loginUI(self):
        self.username = QLabel('账号')
        self.usernameEdit = QLineEdit()
        self.password = QLabel('密码')
        self.passwordEidt = QLineEdit()
        self.okButton = QPushButton("登录")
        self.grid = QGridLayout()
        self.grid.addWidget(self.username, 1, 0)
        self.grid.addWidget(self.usernameEdit, 1, 1)
        self.grid.addWidget(self.password, 2, 0)
        self.grid.addWidget(self.passwordEidt, 2, 1)
        self.grid.addWidget(self.okButton, 3, 1)
        self.box.addLayout(self.grid)
        self.okButton.clicked.connect(self.loginEvent)

    def tipsUI(self):
        self.boxTips = QVBoxLayout()
        self.boxTips.setSpacing(3)
        self.box.addLayout(self.boxTips)
        tipsData = [
            '估值方法：',
            '小熊基本值=5年自由现金流之和/5年资本开支之和',
            '回本年限默认10年，N=10+护城河（-1/0/1/2）+成长性（-1/0/1/2）',
            '十年EBIT增长=(2003年EBIT-2012年EBIT)/2012年EBIT',
            '有形资本汇报率ROIC=(净利润+税+利息)/(流动资产+固定资产+在建工程)=税前息利润EBIT/有形资产合计----------- >15%',
            '理杏仁中的ROTA对应长投的ROIC,有形资产比他更加详细',
            'EV/EQ=(总市值+有息负债-多余现金)/(流动资产+固定资产)=(总市值+有息负债-多余现金)/有形资产合计,   EV/EQ=回报年限*ROIC',
            'EV=总市值+有息负债-多余现金',
            '总市值：红色为高估，绿色为低估'
        ]
        for item in tipsData:
            self.boxTips.addWidget(QLabel(item))

    def tableUI(self, jsonData):
        self.table.clear()
        colData = [{
            'label': '财务费用(累计)',
            'value': 'profitStatement-fe'
        }, {
            'label': '利润总额(累计)',
            'value': 'profitStatement-tp'
        }, {
            'label': '流动资产合计(累计)',
            'value': 'balanceSheet-tca'
        }, {
            'label': '固定资产(累计)',
            'value': 'balanceSheet-fa'
        }, {
            'label': '在建工程(累计)',
            'value': 'balanceSheet-cip'
        }, {
            'label': 'EBIT',
        }, {
            'label': '有形资产合计',
        }, {
            'label': 'ROIC',
        }, {
            'label': 'EBIT同比增长率',
        }, {
            'label': '经营活动产生的现金流量净额(累计)',
            'value': 'cashFlow-ncffoa'
        }, {
            'label': '自由现金流量(累计)',
            'value': 'metrics-fcf'
        }, {
            'label': '资本开支',
        }, {
            'label': '货币资金(累计)',
            'value': 'balanceSheet-cabb'
        }, {
            'label': '有息负债(累计)',
            'value': 'balanceSheet-lwi'
        }, {
            'label': '小熊基本值',
        }, {
            'label': '十年EBIT增长',
        }, {
            'label': 'ROIC平均值',
        }, {
            'label': '回报年限',
        }, {
            'label': 'EQ=有形资产合计',
        }, {
            'label': 'EV=EQ*(回本年限*ROIC)',
        }, {
            'label': '估值总市值',
        }, {
            'label': '当前总市值',
        }, {
            'label': '当前每股股价',
        }, {
            'label': '总股本',
        }, {
            'label': '估值每股股价',
        }]

        stockData = []
        print(222222, jsonData)
        for item in jsonData['fsMetricsList']:
            stockData.append(item)
        tableHeader = []  # 表头名字数据
        tableColData = []  # 表列名字
        self.table.setColumnCount(len(stockData))
        self.table.setRowCount(len(colData))

        print('roic数据的长度', len(stockData))
        for index, item in enumerate(stockData):
            tableHeader.append(item['date'].split('T')[0])
            self.table.setColumnWidth(index, 170)
            data = item['y']
            for jIndex, jItem in enumerate(colData):
                if ('value' in jItem):
                    attr = jItem['value'].split('-')
                    newItem = QTableWidgetItem(str(data[attr[0]].get(attr[1], {'t': 0})['t']))
                    self.table.setItem(jIndex, index, newItem)
                    item[attr[1]] =data[attr[0]].get(attr[1], {'t': 0})['t']  # 赋值最简值到该元素，方便后续的计算
                elif jItem['label'] == 'EBIT':
                    # EBIT = 财务费用+利润总额
                    newItem = QTableWidgetItem('{:.2f}'.format(item['fe'] + item['tp']))
                    newItem.setBackground(self.hightingColor)
                    self.table.setItem(jIndex, index, newItem)
                    item['EBIT'] = item['fe'] + item['tp']
                elif jItem['label'] == '有形资产合计':
                    # 有形资产合计 = 流动资产合计+固定资产+在建工程
                    newItem = QTableWidgetItem('{:.2f}'.format(item['tca'] + item['fa'] + item['cip']))
                    newItem.setBackground(self.hightingColor)
                    self.table.setItem(jIndex, index, newItem)
                    item['EQ'] = item['tca'] + item['fa'] + item['cip']
                elif jItem['label'] == 'ROIC':
                    # ROIC = EBIT/有形资产合计
                    newItem = QTableWidgetItem(str('{:.2%}'.format(item['EBIT'] / item['EQ'])))
                    newItem.setBackground(self.hightingColor)
                    self.table.setItem(jIndex, index, newItem)
                    item['ROIC'] = item['EBIT'] / item['EQ']
                elif jItem['label'] == 'EBIT同比增长率':
                    if index != 0:
                        ebit = (stockData[index - 1]['EBIT'] - item['EBIT']) / item['EBIT']
                        newItem = QTableWidgetItem('{:.2%}'.format(ebit))
                        newItem.setBackground(self.hightingColor)
                        self.table.setItem(jIndex, index - 1, newItem)
                elif jItem['label'] == '资本开支':
                    # 资本开支 = 经营活动产生的现金流量净额-自由现金流量
                    newItem = QTableWidgetItem(str(item['ncffoa'] - item['fcf']))
                    newItem.setBackground(self.hightingColor)
                    self.table.setItem(jIndex, index, newItem)
                    item['CAPEX'] = item['ncffoa'] + item['fcf']

        calData = self.getCalData(stockData)
        for index, item in enumerate(colData):
            tableColData.append(item['label'])
            if item['label'] == '小熊基本值':
                newItem = QTableWidgetItem(calData['BaseValue'])
                newItem.setBackground(self.blueColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == '十年EBIT增长':
                stockLen = len(stockData)
                EBITValue = (stockData[0]['EBIT'] - stockData[stockLen - 1]['EBIT']) / \
                            stockData[stockLen - 1]['EBIT']
                newItem = QTableWidgetItem(str('{:.2f}'.format(EBITValue)) + '倍')
                newItem.setBackground(self.blueColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == 'ROIC平均值':
                newItem = QTableWidgetItem(calData['ROICAVG'])
                newItem.setBackground(self.blueColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == 'EQ=有形资产合计':
                newItem = QTableWidgetItem(str(calData['EQ']))
                newItem.setBackground(self.blueColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == '回报年限':
                newItem = QTableWidgetItem(self.yearEdit.currentText())
                newItem.setForeground(QBrush(QColor(255, 0, 0)))
                self.table.setItem(index, 0, newItem)
            elif item['label'] == 'EV=EQ*(回本年限*ROIC)':
                yearRoic = int(self.yearEdit.currentText()) * float(calData['ROICAVG'].strip('%')) / 100
                global EV
                EV = calData['EQ'] * yearRoic
                newItem = QTableWidgetItem('{:.0f}'.format(EV))
                newItem.setBackground(self.blueColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == '估值总市值':
                price = EV - calData['lwi'] + calData['cabb']
                self.price_pre = price
                newItem = QTableWidgetItem('{:.0f}'.format(price))
                if price < calData['mc']:
                    newItem.setBackground(self.redColor)
                else:
                    newItem.setBackground(self.greenColor)
                self.table.setItem(index, 0, newItem)
            elif item['label'] == '当前总市值':
                price = calData['mc']
                newItem = QTableWidgetItem(str(price))
                self.table.setItem(index, 0, newItem)            
            elif item['label'] == '当前每股股价':
                price = self.price_sp
                newItem = QTableWidgetItem(str(price))
                self.table.setItem(index, 0, newItem)            
            elif item['label'] == '总股本':
                price = self.price_num
                newItem = QTableWidgetItem(str(price))
                self.table.setItem(index, 0, newItem)            
            elif item['label'] == '估值每股股价':
                price = self.price_pre / self.price_num
                newItem = QTableWidgetItem(str(price))
                self.table.setItem(index, 0, newItem)
        print(tableColData)
        print(tableHeader)
        self.table.setHorizontalHeaderLabels(tableHeader)  # 设置表头数据
        self.table.setVerticalHeaderLabels(tableColData)  # 设置表列数据

    # 同行对比表格
    def peerTable(self, jsonData, stockIdArr):
        self.table.clear()
        colData = []
        stockData = {}
        for item in jsonData['fsMetricsList']:
            id = item['stockId']
            if (id in stockData):
                stockData[id].append(item)
            else:
                stockData[id] = []
                stockData[id].append(item)
        tableHeader = []  # 表头名字数据
        tableColData = []  # 表列名字

        # 遍历股票代码数组，同行对比
        idStrArr = self.stockIdArr

        #遍历行表头 start
        colData.append({'label': '归属母公司加权ROE'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'ROE', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value': 'avg', 'type':'ROE'})

        colData.append({'label': '归属母公司扣非ROE'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'ROE_A', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value': 'avg', 'type':'ROE_A'})

        colData.append({'label': 'ROIC'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'ROIC', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value': 'avg', 'type':'ROIC'})

        colData.append({'label': '毛利率GM'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'GM', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value':'avg', 'type':'GM'})

        colData.append({'label': '净营业周期'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'ROUND', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value': 'avg', 'type':'ROUND'})

        colData.append({'label': '三费占比'})
        for jItem in idStrArr:
            colData.append({'label': self.stockNameData[jItem], 'value': 'FEE', 'id': int(jItem)})
        colData.append({'label': str(len(idStrArr)) + '家均值', 'value': 'avg', 'type':'FEE'})
        # 遍历行表头 end

        # 遍历表列名
        for index, item in enumerate(colData):
            tableColData.append(item['label'])

        #找出行业数据中长度最小的，以防下面遍历出错
        stockDataLen = []
        for key in stockData:
            stockDataLen.append(len(stockData[key]))
        stockDataLen.sort()
        print('找出行业数据中长度最小的，以防下面遍历出错%s' %stockDataLen[0])
        # 平均值对象
        avgData={
            'ROE': [],
            'ROE_A':[],
            'ROIC':[],
            'GM': [],
            'ROUND': [],
            'FEE': []
        }
        year = int(self.peerYearEdit.currentText())
        tablePerDataLen = stockDataLen[0]-1>year and year or stockDataLen[0]-1# 净营业周期需要计算期初和期末，len-1
        print('同行对比年数：',tablePerDataLen)
        self.table.setColumnCount(tablePerDataLen+1)
        self.table.setRowCount(len(colData))
        # 遍历表头,遍历表格内容,
        for index in range(tablePerDataLen):
            tableHeader.append(stockData[stockIdArr[0]][index]['date'].split('T')[0])
            self.table.setColumnWidth(index, 100)
            for jIndex, jItem in enumerate(colData):
                color = self.blueColor
                if 'value' in jItem:
                    dItem = 'id' in jItem and stockData[jItem['id']] or {}
                    d = ''
                    if jItem['value'] == 'ROE':
                        d = dItem[index]['y']['metrics'].get('wroe', {'t': 0})['t']
                        d = '{:.2%}'.format(d)
                        dItem[index]['ROE'] = d
                    elif jItem['value'] == 'ROE_A':
                        d = dItem[index]['y']['metrics'].get('roe_adnrpatoshaopc', {'t': 0})['t']
                        d = '{:.2%}'.format(d)
                        dItem[index]['ROE_A'] = d
                    elif jItem['value'] == 'ROIC':
                        d = dItem[index]['y']['metrics'].get('rota', {'t': 0})['t']
                        d = '{:.2%}'.format(d)
                        dItem[index]['ROIC'] = d
                    elif jItem['value'] == 'GM':
                        d = dItem[index]['y']['profitStatement']['gp_m']['t']
                        d = '{:.2%}'.format(d)
                        dItem[index]['GM'] = d
                    elif jItem['value'] == 'ROUND':
                        # 净营业周期=存货周转天数+应收账款周转天数-应付账款周转天数
                        # 应收账款周转天数
                        arAvg = (dItem[index]['y']['balanceSheet']['ar']['t'] +
                                 dItem[index + 1]['y']['balanceSheet']['ar']['t']) / 2
                        ar = arAvg > 0 and 360 / (
                                    stockData[jItem['id']][index]['y']['profitStatement']['oi']['t'] / arAvg) or 0
                        # 应付账款周转天数
                        apAvg = (dItem[index]['y']['balanceSheet']['ap']['t'] +
                                 dItem[index + 1]['y']['balanceSheet']['ap']['t']) / 2
                        ap = apAvg > 0 and 360 / (
                                    stockData[jItem['id']][index]['y']['profitStatement']['oc']['t'] / apAvg) or 0
                        i_ds = stockData[jItem['id']][index]['y']['metrics']['i_ds']['t']
                        d = i_ds + ar - ap
                        d = '{:.2f}'.format(d)
                        dItem[index]['ROUND'] = d
                        print(i_ds, ar, ap)
                    elif jItem['value'] == 'FEE':
                        d = stockData[jItem['id']][index]['y']['profitStatement']['te_r']['t']
                        d = '{:.2%}'.format(d)
                        dItem[index]['FEE'] = d
                    elif jItem['value'] == 'avg': #平均值
                        count = 0
                        for key in stockData:
                            v = stockData[key][index][jItem['type']]
                            vfloat = float('%' in v and v.strip('%') or v)
                            count += vfloat
                        d = count/len(stockData)
                        d = '%' in v and '{:.2%}'.format(d/100) or '{:.2f}'.format(d)
                        avgData[jItem['type']].append(d)
                        color = self.hightingColor
                    newItem = QTableWidgetItem(str(d))
                    newItem.setBackground(color)
                    self.table.setItem(jIndex, index, newItem)
        #每一行求平均值
        tableHeader.append('平均值')
        for jIndex, jItem in enumerate(colData):
            if 'value' in jItem:
                d = 0
                color = self.greenColor
                for index in range(tablePerDataLen):
                    if jItem['value'] == 'avg':  # 平均值
                        v = avgData[jItem['type']][index]
                    else:
                        v = stockData[jItem['id']][index][jItem['value']]
                    vfloat = float('%' in v and v.strip('%') or v)
                    d += vfloat
                d = d/tablePerDataLen
                d = '%' in v and '{:.2%}'.format(d / 100) or '{:.2f}'.format(d)
                newItem = QTableWidgetItem(str(d))
                newItem.setBackground(color)
                self.table.setItem(jIndex, tablePerDataLen, newItem)

        self.table.setHorizontalHeaderLabels(tableHeader)  # 设置表头数据
        self.table.setVerticalHeaderLabels(tableColData)  # 设置表列数据

    # 获取统计数据
    def getCalData(self, data):
        CAPEXSum = 0  # 5年资本开支之和
        FCFSum = 0  # 5年自由现金流之和
        ROICAVG = 0  # roic平均值
        EQ = data[0]['EQ']  # 有形资产合计
        lwi = data[0]['lwi']  # 有息负债
        cabb = data[0]['cabb']  # 货币资金--多余现金
        mc = self.price_mc  # 总市值
        for jIndex, jItem in enumerate(data):
            if (jIndex < 5):
                CAPEXSum += jItem['CAPEX']
                FCFSum += jItem['fcf']
            ROICAVG += jItem['ROIC']
        return {
            'BaseValue': '{:.2}'.format(FCFSum / CAPEXSum),
            'ROICAVG': '{:.2%}'.format(ROICAVG / len(data)),
            'EQ': EQ,
            'lwi': lwi,
            'cabb': cabb,
            'mc': mc
        }

    def clearUI(self):
        for i in range(self.box.count()):
            boxChild = self.box.itemAt(i)
            for j in range(boxChild.count()):
                boxChild.itemAt(j).widget().deleteLater()

    def getUserInfo(self):
        self.clearUI()
        res = requests.get("https://www.lixinger.com/api/user/users/current", headers=Headers)
        if res.status_code == 200:
            self.dataUI()
        else:
            self.loginUI()

    def loginEvent(self):
        data = {'uniqueName': self.usernameEdit.text(), 'password': self.passwordEidt.text()}  # 用户信息
        res = requests.post("https://www.lixinger.com/api/login/by-account", data)
        if res.status_code == 200:
            m_cookie = res.headers["Set-Cookie"].split(';')[0]
            Headers["Cookie"] = m_cookie
            f = open(cookieFilename, 'w')
            f.write(m_cookie)
            print(Headers["Cookie"])
            self.getUserInfo()
        else:
            print("登录连接不成功%s" % (res.status_code))

    # 查询按钮事件
    def searchEvent(self, type):
        self.getStockInfo()
        self.getROICData()

    def searchPeerEvent(self, type):
        self.getStockInfo()
        self.getPeerData()

    # 获取股票的详细信息
    def getStockInfo(self):
        arr = self.codeEdit.text().split(',')
        self.stockIdArr = []
        detailStr = ''
        noSearchId = []
        self.stockNameData = {}
        for item in arr:
            url = 'https://www.lixinger.com/api/stock/stocks/stock/'
            if '60' == item[0:2]:
                url += 'sh/' + item+'/'+item
            else:
                url += 'sz/' + item+'/'+item

            res = requests.get(url, headers=Headers)
            if res.status_code == 200:
                data = json.loads(res.text)
                self.stockIdArr.append(item)
                detailStr += item + ': ' + data['name'] + '   '
                self.stockNameData[item] = data['name']
                self.price_mc = data['priceMetrics']['mc']#当前总市值
                self.price_sp = data['priceMetrics']['sp']#每股股价
                self.price_num = data['priceMetrics']['mc']/data['priceMetrics']['sp'] #股本
            elif res.status_code == 401:
                self.loginEvent()
            else:
                print('没有'+item+'股票')
                noSearchId.append(item)
        print(noSearchId)
        if len(noSearchId) > 0:
            noSearchStr = ','.join(noSearchId)
            detailStr += '(没有找到股票：' + noSearchStr + ')'
        self.stockInfo.setText(detailStr)
        print(self.stockNameData)
        print(self.stockIdArr)

    # 获取roic数据
    def getROICData(self):
        if len(self.stockIdArr) > 0:
            print(self.dateEdit.text(), self.dateEditEnd.text())
            p = {
                "stockIds": [int(self.stockIdArr[0])],
                "startDate": self.dateEdit.text(),
                "endDate": self.dateEditEnd.text(),
                "granularities": ["y"],
                "metricNames": ["profitStatement.fe", "profitStatement.tp", "balanceSheet.tca", "balanceSheet.fa",
                                "balanceSheet.cip", "balanceSheet.cabb", "balanceSheet.lwi", "cashFlow.ncffoa",
                                "metrics.fcf"],
                "expressionCaculateTypes": ["t", "t_o", "t_y2y", "t_c2c", "c", "c_o", "c_y2y", "c_c2c", "c_2y", "ttm",
                                            "ttm_y2y", "ttm_c2c"]
            }
            r = requests.post('https://www.lixinger.com/api/analyt/company/fs-metrics/list-info', json=p, headers=Headers)
            if r.status_code == 200:
                self.tableUI(json.loads(r.text))
            elif r.status_code == 401:
                self.loginEvent()

    # 获取同行数据
    def getPeerData(self):
        idsArr = []
        time = datetime.datetime.strptime(self.dateEdit.text(), "%Y-%m-%d").date()
        dateStart = time + datetime.timedelta(days=-365)
        for val in self.stockIdArr:
            idsArr.append(int(val))
        p = {
            "stockIds": idsArr,
            "startDate": str(dateStart),
            "endDate": self.dateEditEnd.text(),
            "granularities": ["y"],
            "metricNames": ["profitStatement.gp_m", "profitStatement.te_r", "profitStatement.oi", "profitStatement.oc",
                            "metrics.wroe", "metrics.roe_adnrpatoshaopc", "metrics.rota", "metrics.i_ds", "balanceSheet.ar", "balanceSheet.ap"],
            "expressionCaculateTypes": ["t", "t_o", "t_y2y", "t_c2c", "c", "c_o", "c_y2y", "c_c2c", "c_2y", "ttm",
                                        "ttm_y2y", "ttm_c2c"]
        }
        r = requests.post('https://www.lixinger.com/api/analyt/company/fs-metrics/list-info', json=p, headers=Headers)
        if r.status_code == 200:
            self.peerTable(json.loads(r.text), idsArr)
        elif r.status_code == 401:
            self.loginEvent()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
