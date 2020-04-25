# -*- coding: utf-8 -*-

# for  break  continue

userinfo = [1, '张飞', '涿郡', 20, 100000, None]

for i in range(2, 20, 3):
    print(i)
 
for i in [1, '张飞', '涿郡', 20, 100000, None]:
    print(i)
    
for i in userinfo:
    print(i)

# break:结束本层循环，整个for全部都不看了
# continue:结束本次循环，继续走下一次循环
    
for i in range(20):
    if i >= 6:
        print(i)
        continue
    print('hehe')
