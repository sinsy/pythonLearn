#!/usr/bin/python3

list1 = ['a', 'b', 'c', 1999, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print('list1[0]', list1[0])
print('list2[1:5]', list2[1:5])

#修改元素
list2[3] = 1000
print('list2', list2)

#删除元素
del list2[3]
print('删除第4个元素', list2)

#获取长度
print('list2长度', len(list2))

#组合
list3 = list1 + list2
print('list3 = list1 + list2, ', list3)

#重复
print("['Hi!'] * 4,	", ['Hi!'] * 4	)

#元素是否位于列表中
print('3 in [1,2,3]', 3 in [1,2,3])

#读取倒数第二个元素
print('读取倒数第二个元素list1', list1[-2])

print('list1', list1)
#输出从第二个元素开始后的所有元素
print('输出从第二个元素开始后的所有元素', list1[1:])

#追加元素
list1.append('abao')
print('追加元素', list1)

#统计元素出现的次数
print ("1999元素个数 : ", list1.count(1999))

#扩展元素
list3 = list(range(5))
list1.extend(list3)
print ("扩展后的列表：", list1)

#从列表中找出某个值第一个匹配项的索引位置
print('list.index(obj):', list1.index(1))

#插入
list1.insert(0, '2019')
print('插入2019在第一个元素', list1)

#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1.pop(0)
print('移除列表中的一个元素（默认最后一个元素），并且返回该元素的值', list1)

#移除列表中某个值的第一个匹配项
list1.remove('abao')
print('移除列表中某个值的第一个匹配项', list1)

#反向列表中元素
list1.reverse()
print('反向列表中元素', list1)

#对原列表进行排序
list2.sort(reverse=True)
print('对原列表进行降序排序', list2)

#清空列表
list2.clear()
print('清空列表', list2)

#复制列表
list4 = list1.copy()
print('复制列表', list4)
