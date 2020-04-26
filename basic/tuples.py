# -*- coding: utf-8 -*-


#元组：无序  tuple    取值时心中有沟壑         java---数组 工作后，你掌握2维基本上能解决很多问题

#1、定义(好懂)
userinfo1=()
userinfo2=(1,'张飞','涿郡',20,100000,None) #一维    DB:插入，更新、批量删除、查出一行数据
userinfo3=(
        (1,'张飞','涿郡',20,100000,None),
        (2,'刘备','长安',28,1000,'甘夫人'),
        (3,'关羽','河北谢良',25,2000,None)
        )#二维

#n维 userinfo4=(((),(),(),()),(),())


#2、访问 下标从0开始
#正、反、切片
userinfo2=(1,'张飞','涿郡',20,100000,None)
print(userinfo2[2])
print(userinfo2[-4])

#切片(一定要掌握)
print(userinfo2[0:3]) #从0开始切到3但不包含3   [0,3)   工作中多见于这种场景
print(userinfo2[-3:-1])

#幺蛾子
#如果是头或尾，可以不写
print(userinfo2[:3])
print(userinfo2[-3:])
print(userinfo2[:])

#可以混合
print(userinfo2[2:-2])

#左边定好以后，一定是向右取（右值），左切一定是空元组
print(userinfo2[-2:2]) #()



#3、遍历(一定要掌握)
userinfo2=(1,'张飞','涿郡',20,100000,None)
print(userinfo2[0])
print(userinfo2[1])
print(userinfo2[2])
print(userinfo2[3])
print(userinfo2[4])
print(userinfo2[5])


#预备知识
for i in range(6):
    print(i)

print(len(userinfo2)) #length

#改造
for i in range(6):
    print(userinfo2[i])

#2次改造(最终方案)
#一维遍历
for i in range(len(userinfo2)):
    print(userinfo2[i])
    
    
userinfo3=(
        (1,'张飞','涿郡',20,100000,None),
        (2,'刘备','长安',28,1000,'甘夫人'),
        (3,'关羽','河北谢良',25,2000,None)
        )
# print(userinfo3[1][1])
# 
# print(userinfo3[0][5])
# print(userinfo3[1][5])


#二维遍历
for i in range(len(userinfo3)):
    #print(userinfo3[i])  #userinfo3[0]  userinfo3[1]   userinfo3[2]
    for j in range(len(userinfo3[i])):  #注意这里的写法
        print(userinfo3[i][j])


