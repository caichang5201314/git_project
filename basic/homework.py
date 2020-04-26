# -*- coding: utf-8 -*-

total = 0
for i in range(1, 101):
    total = total + i
 
print(total)

lists = []
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        lists.append(i)
print('能被3整除但不能被5整除的数有:', lists)

# #[expression for iter_val in iterable if cond_expr]
# lists=[i for i in range(101) if i%3==0 and i%5!=0]
# print('能被3整除但不能被5整除的数有:',lists)
# 
# print([i for i in range(101) if i%3==0 and i%5!=0])
# 
# 
# print([(x,y) for x in range(1,100) for y in range(5,20)])
# print([(x,y) for x in range(1,100) for y in range(5,20) if x>=5 if y<=9])

# 思考：
# 1、一个小的编程思维
# 2、列表解析
# 3、字符串、格式化
# 4、函数

