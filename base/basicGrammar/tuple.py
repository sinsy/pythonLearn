#!/usr/bin/python3

#元组知识点

tup1 = (50)
print(type(tup1)) # 不加逗号，类型为整型

tup1 = (50,)
print(type(tup1))    # 加上逗号，类型为元组

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

#列表转换元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)

#元组的元素不允许修改，但我们可以对元组进行连接组合
tup3 = tup1 + tup2
print(tup3)

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup3
print(tup3)

