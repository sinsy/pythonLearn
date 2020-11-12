# coding: utf-8

##### 下方代码为 IDE 运行必备代码 #####

if __name__ == '__main__':
    import jqsdk
    params = {
        # 'token': '677b04dfe55fbca9e267fe5ed546d3a9',  # 公司，在客户端系统设置中找，字符串格式，例如 'asdf...'
        'token': '88784e95a723fa39416797f0db60e900',  #家， 在客户端系统设置中找，字符串格式，例如 'asdf...'
        'algorithmId': 8,  # 在客户端我的策略中，整数型，例如：1；回测结束后在客户端此ID策略的回测列表中找对应的回测结果
        'baseCapital': 1000000,
        'frequency': 'day',
        'startTime': '2011-12-15',
        'endTime': '2019-08-01',
        'name': "Test1",
    }
    jqsdk.run(params)

##### 下面是策略代码编辑部分 #####

import jqdata
from jqdata import jy 
def initialize(context):
    #股票代码
    g.security = "512000.XSHE"  
    #设置基准 沪深300
    set_benchmark('000300.XSHG')
    #设置佣金/印花税 买入时万分之0.6,卖出时万分之0.6
    set_order_cost(OrderCost(open_tax=0, close_tax=0, open_commission=0.00006, close_commission=0.00006, close_today_commission=0, min_commission=0), type='fund')
    # 设置滑点 价格的一个百分比(比如0.2%, 交易时加减当时价格的0.1%)
    set_slippage(PriceRelatedSlippage(0.002),type='fund')
    # 设置动态复权(真实价格)模式
    set_option('use_real_price', True)
    log.info('initialize run only once')
    run_daily(market_open, time='open')
    run_weekly(week_market_open, weekday=4, time='open')

def week_market_open(context):
    if context.portfolio.available_cash>2000:
        order_value(g.security, 2000)

def market_open(context):
    # 输出开盘时间
    log.info('(market_open):' + str(context.current_dt.time()))

def on_strategy_end(context):
    print(df2)
    # 策略运行结束时调用(可选)
    print('回测结束') 