#!/usr/bin/python3

#集合知识点

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能

a = set('abracadabra')
b = set('alacazam')
print('a:  ',a)
print('b:  ',b)
# 集合a中包含而集合b中不包含的元素
print('a-b: ', a-b)

# 集合a或b中包含的所有元素
print('a|b: ', a|b)

# 集合a和b中都包含了的元素
print('a&b: ', a&b)

# 不同时包含于a和b的元素
print('a^b: ', a^b)

# 集合支持集合推导式
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

#添加元素：列表，元组，字典
s = set(("Google", "Runoob", "Taobao"))
s.add('Facebook')
print(s)

s.update({1,3})
print(s)

s.update([1,4],[5,6])
print(s)

#删除元素
s.remove(1)
print(s)

s.discard(1)
print(s)