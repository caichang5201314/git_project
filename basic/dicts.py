# -*- coding: utf-8 -*-

#字典 dict dictionary  无序   dict<--->json
# get 、keys ，values，items
userinfo = {
    "resultcode": "200",
    "reason": "Return Success!",
    "result": {
        "province": "重庆",
        "city": "",
        "areacode": "023",
        "zip": "404100",
        "company": "联通",
        "card": ""
    },
    "error_code": 0
}

# print(userinfo.get('reason'))
# print(userinfo.get('caichang','hehe'))
# 
# print(userinfo.keys())
# print(type(userinfo.keys()))
# 
# print(userinfo.values())
# print(type(userinfo.values()))


# for key,value in userinfo.items():
#     print(key,value)
#     print(type(key),type(value))


print(userinfo.get('result').get('company'))
