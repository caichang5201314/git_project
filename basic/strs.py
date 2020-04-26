# -*- coding: utf-8 -*-

# 字符串
# 1、可单引号，也可以双引号
# 2、可以\ 转义，建议字符串用双引号能规避\转义等
# 3、字符串前面带r表示里面的内容原样输出
# 总结：我以后写字符串都双引号且前面都带个r
# 4、格式化输出(java、c)，还可以加,但比较来比较去，c这种是更好的
# 5、可以把字符串想成元组，一个元素一个下标,元组怎么玩字符串就可以怎么玩
# 6、字符串有很多独有的方法，下来后慢慢学习摸索(重点)，以后你写代码这些方法就非常有用



name = 'caichang'
name = "caichang"

# str='i'm ok'
strs1 = "i'm ok"
strs2 = 'i\'m ok'

print(strs1)
print(strs2)

path = "d:\nideo\python\01.txt"
print(path)

path = r"d:\nideo\python\01.txt"
print(path)

print('你的路径为：' + path)  # java
print('你的路径为：', path)  # ,会多一个空格
print('你的路径为：%s' % path)  # c

name = '蔡昶'
month = 3
money = 102.05

print("我的名字叫蔡昶,我3月份的电费为102.05元")

print("我的名字叫" + name + ",我" + str(month) + "月份的电费为" + str(money) + "元")  # java

# %s %d %.2f  ===>%s
print("我的名字叫%s,我%d月份的电费为%.2f元" % (name, month, money))  # c
print("我的名字叫%s,我%s月份的电费为%s元" % (name, month, money))  # c (不推荐)

name = 'caichang'
print(name[2])
print(len(name))
print(name[2:5])

for i in range(len(name)):
    print(name[i])

print(name.upper())
print(name.capitalize())

