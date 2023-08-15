#first line edited

"""1.3.1 算术计算"""
x1 = 1 - 2
print("1 + 2 = ", x1)
# 乘法中如果有一个数据是float则全部的都是float
x2 = 4 * 5
print("4 * 5 = ", x2)
print("1.2 * 8 = ", 1.2 * 8)
# 默认除法是float；pyton3.x中如是，但是在2.x中是除完四舍五入
x3 = 8 / 2
print("8 / 2 = ", x3)
print("3 ** 2 = ", 3 ** 2)


"""1.3.2 数据类型"""
# type (data)
# print 中可以通过‘  , ’ 来分割出来不同的接续的数据类型
print("10的数据类型是", type(10))
print("1.2的数据类型是", type(1.2))
print('"string"的数据类型是', type("string"))


"""1.3.3 变量"""
x = 10  # 初始化
print(x)
x = 11  # 赋值


"""1.3.4 列表"""
my_list = [1, 2, 3, 4, 8]  # 初始化
print(my_list)
# len()来统计list的长度
print("my_list 的长度是：", len(my_list))
print(my_list[1])
my_list[4] = 99  # 元素赋值
print(my_list)

# 从index 0 取到index 2
slice1 = my_list[0:2]
print(slice1)
# 从index 1 开始取到结束
slice2 = my_list[1:]
print(slice2)
# 从头开始取到index 3
slice3 = my_list[:3]
print(slice3)
# 从头开始取到最后一个
slice4 = my_list[:-1]
print(slice4)
# 从index 1 开始取到最后，间隔一个取一次
slice5 = my_list[1::2]
print(slice5)


"""1.3.5 字典"""
# 定义形式：{key : value}
my_dict = {"height": 188}  # 生成字典
print(my_dict["height"])  # 通过key来访问value
my_dict["weight"] = 99  # 添加新的key，并且赋值
print(my_dict)


"""1.3.6 布尔类型"""
sleepy = True
angry = False

print("BOOL: ", type(sleepy))

print(sleepy and angry)  # 与门
print(sleepy or angry)  # 或门
print(not angry)  # 非门


"""1.3.7 if语句"""
hungry = True
if hungry:
    print("I am hungry!")
elif not angry:
    print("I am angry!")
else:
    print('Nothin.')


"""1.3.8 for语句"""
for i in [1, 2, 3, 4, 5]:
    print(i)


"""1.3.9 函数"""


def hello():
    print("Hello Isaac")


hello()
