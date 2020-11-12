#!/usr/bin/python3

#面向对象 类
class MyClass:
    """一个简单的类实例"""
    i=12345
    def __init__(self): #类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
        self.r = 'ahahaha'
    def f(self):
        return 'hello world'

x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的属性 r 为：", x.r)
print("MyClass 类的方法 f 输出为：", x.f())


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()
