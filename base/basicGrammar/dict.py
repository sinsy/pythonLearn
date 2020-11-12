#!/usr/bin/python3

#字典知识点

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

#修改
dict['Age'] = '88'
print("dict['Age']: ", dict['Age'])

del dict['Name'] # 删除键 'Name'
print("dict", dict)


#fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict))

print ("字典所有值为 : ",  list(dict.values()))
