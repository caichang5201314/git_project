# -*- coding: utf-8 -*-

# if

# 语法1：
# if ....:
#     ......
# else:
#     .......
 
# age = int(input('请输入你的年龄：'))
# if age > 18 :
#     print('ok')
# else:
#     print('fail')    

# 语法2：
# if ....:
#     ......
# elif ....:
#     .....
# else:
#     .......

# age = int(input('请输入你的年龄：'))
# if age > 18 :
#     print('ok')
# elif age > 10:
#     print('hehe')
# else:
#     print('fail') 

#单if
# ......
# .....
# if ....:
#     .....
# .....
# .....

#并排if 查询
# .....
# if....:
#     ......
# if.....:
#     .....
# if.....:
#     .....
# .....



#嵌套 根据具体的业务来写代码
# if ...:
#     if .....:
#         .......
#     elif .....:
#         ......
#     else:
#         ......
# elif .....:
#     if ....:
#         .....
#     ......
# else:
#     ......



# 连接数据库
# rs  = select username,pwd,status from users where username='你传过来的username'
# 
# if rs['username']:
#     if rs['pwd']==md5('你传过来的pwd'):
#             登录成功等。。。。
#     else：
#             抛出用户名或密码不正确            
# 
# else：
#     if status==0：
#             抛出用户被禁用等信息
#     else:
#             用户不存在    
    
