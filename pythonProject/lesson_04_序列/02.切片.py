# 切片
# 切片指从现有列表中，获取一个子列表
# 创建一个列表，一般创建列表时，变量的名字会使用复数
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# 列表的索引可以是负数
# 如果索引是负数，则从后向前获取元素，-1表示倒数第一个，-2表示倒数第二个 以此类推
print(stus[-2])

# 通过切片来获取指定的元素
# 语法：列表[起始:结束]
#   通过切片获取元素时，会包括起始位置的元素，不会包括结束位置的元素
#   做切片操作时，总会返回一个新的列表，不会影响原来的列表
#   起始和结束位置的索引都可以省略不写
#   如果省略结束位置，则会一直截取到最后
#   如果省略起始位置，则会从第一个元素开始截取
#   如果起始位置和结束位置全部省略，则相当于创建了一个列表的副本
print(stus[1:])
print(stus[:3])
print(stus[:])
print(stus)

# 语法：列表[起始:结束:步长] 
# 步长表示，每次获取元素的间隔，默认值是1
# print(stus[0:5:3])
# 步长不能是0，但是可以是负数
# print(stus[::0]) ValueError: slice step cannot be zero
# 如果是负数，则会从列表的后部向前边取元素
print(stus[::-1])
