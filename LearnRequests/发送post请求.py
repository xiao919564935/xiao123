"""
发送 post 请求
    1.使用 data 传表单格式的参数
    2.使用 json 传 json 格式的参数
    3.带请求头使用 headers
"""
import requests
# 发送post请求，带参数时，可以使用data或json来传参，具体使用那个要看系统怎么实现的。
# 上一步注册成功的手机号，验证登录，登录使用post
#
# url = "http://jy001:8081/futureloan/mvc/api/member/login?mobilephone=18123121242&pwd=123456"
# r = requests.post(url)
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cans = {"mobilephone": "18123121242", "pwd": "123456"}
# r = requests.post(url,params =cans) # params 也支持post传参
# print(r.text)
r = requests.post(url, data=cans)  # data，表单格式传参
print(r.text)
r = requests.post(url, json=cans)  # json，金融系统不支持json方式传参。
print(r.text)

# 发送请求到 httpbin，观察区别
r = requests.post("http://www.httpbin.org/post", data=cans)  # "Content-Type": "application/x-www-form-urlencoded"
print(r.text)
r = requests.post("http://www.httpbin.org/post", json=cans)  # "Content-Type": "application/json"
print(r.text)
