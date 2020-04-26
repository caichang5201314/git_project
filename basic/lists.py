# -*- coding: utf-8 -*-

#列表  有序（他有自己独有的方法）     链表

#定义

#访问

#遍历

#这3个和元组的玩法一模一样，只是把[]改为[]


userinfo1=[]
userinfo2=[1,'张飞','涿郡',20,100000,None]
userinfo3=[
        [1,'张飞','涿郡',20,100000,None],
        [2,'刘备','长安',28,1000,'甘夫人'],
        [3,'关羽','河北谢良',25,2000,None]
        ]


userinfo2=[1,'张飞','涿郡',20,100000,None]
print(userinfo2[2])
print(userinfo2[-4])
print(userinfo2[0:3]) #从0开始切到3但不包含3   [0,3)   工作中多见于这种场景
print(userinfo2[-3:-1])

userinfo2=[1,'张飞','涿郡',20,100000,None]
for i in range(len(userinfo2)):
    print(userinfo2[i])

userinfo3=[
        [1,'张飞','涿郡',20,100000,None],
        [2,'刘备','长安',28,1000,'甘夫人'],
        [3,'关羽','河北谢良',25,2000,None]
        ]

for i in range(len(userinfo3)):
    for j in range(len(userinfo3[i])):  #注意这里的写法
        print(userinfo3[i][j])


#独有的方法(超级重点)
userinfo2=[1,'张飞','涿郡',20,100000,None]
userinfo2.append('丈八蛇矛')

print(userinfo2)
userinfo2.append((1,2,3,4,5))
print(userinfo2)
userinfo2.append(['caichang','caibao','roubao'])
print(userinfo2)

userinfo2.insert(2,'狂魔')
print(userinfo2)

#删除
userinfo2.pop()
print(userinfo2)

userinfo2.pop(2)
print(userinfo2)

# userinfo2.pop(8)
# print(userinfo2)

userinfo2.remove('丈八蛇矛')
print(userinfo2)

# userinfo2.remove('丈八蛇矛')
# print(userinfo2)

userinfo2.clear()
print(userinfo2)

# userinfo1=[2,'刘备','长安',28,1000,'甘夫人']
# userinfo2=[1,'张飞','涿郡',20,100000,None]
# userinfo1=userinfo2.copy()
# print(userinfo1)

#排序
userinfo4=[3,43214,13,4,315,4325,434,3214,324]
userinfo4.sort(key=None, reverse=False)
print(userinfo4)

userinfo4.reverse()
print(userinfo4)


#自己玩 copy,count,extend,index



