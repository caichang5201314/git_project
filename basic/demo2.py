# -*- coding: utf-8 -*-

# 1.赋值运算符:  =  
# 2.算术运算符:  + ， - ， * ， / ， // ， % ， **
#     // 返回商的整数部分 
#     % 返回余数  取模 mod
#     **幂运算 
# 3.关系运算符:  >，<， ==， >=，<=，!= (多用在判断中)
# 4.逻辑运算符:  and，or，not (多用在判断中)

chang = 20
kuan = 5

mianji = chang * kuan
print(mianji)

months_sal=10000+200


print(9/3) #3.0 浮点数(小数)
print(9//3) #3
print(10//3) #3
print(10%3) #1,注意读法 10模3


print(10**3) #1000

sal=3000
if sal>2000:
    print('好厉害哟！')


sal=5000
comm=400
if sal>2000 or comm>=300:
    print('好厉害哟！')
    
    


if not sal<=4000: #sal>4000
    print('ok')
