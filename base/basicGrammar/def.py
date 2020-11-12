


#函数

# 计算面积函数
def area(width, height):
    return width * height
print(area(3,10))

def hello():
    print('hello world', area(3,10))
hello()


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")


# 可写函数说明---不定长参数
def printinfo1(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)
# 调用printinfo 函数
printinfo1(70, 60, 50)


# 可写函数说明
def printinfo3(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)
# 调用printinfo 函数
printinfo3(1, a=2, b=3)


#匿名函数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


#全局变量和局部变量
total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)


#修改嵌套作用域
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明（enclosing 作用域，外层非全局作用域）
        num = 100
        print(num)
    inner()
    print(num)
outer()

