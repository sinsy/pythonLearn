import re

# 全局搜索
match = re.search(r"[1-9]\d{5}", "BT100081")
if match:
    print(match.group(0))

# match 从头部开始匹配
match = re.match(r"[1-9]\d{5}", "BT100081")
print(match)

match = re.match(r"[1-9]\d{5}", "100081BT")
print(match)

# findall 找到所有匹配字符串
match = re.findall(r"[1-9]\d{5}", "100081BT 516400BT")
print(match)

# split 分割并替换符合的字符串为空
match = re.split(r"[1-9]\d{5}", "100081BT 516400BT")
print(match)

# split maxsplit 匹配多少个
match = re.split(r"[1-9]\d{5}", "100081BT 516400BT", maxsplit=1)
print(match)

# sub 替换
match = re.sub(r"[1-9]\d{5}", "zipcode:", "100081BT 516400BT")
print(match)

# 贪婪匹配 , 输出匹配的最长长度
match = re.search(r"PY.*N", "PYANNCNDN")
print(match.group(0))

# 最小匹配
match = re.search(r"PY.*?N", "PYANNCNDN")
print(match.group(0))
