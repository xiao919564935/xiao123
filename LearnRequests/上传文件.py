'''
上传文件，一般都是post接口，用files参数上传
'''

import requests

url = "http://www.httpbin.org/post"

'''
files参数，字典的格式，'name'：file-tuple
file-tuple可以是2-tuple('filename',fileobj)、3-tuple('filename',fileobj,'content_type')、4-tuple
'''
with open("D:/Lenovo/test.txt", encoding='utf-8') as f:
    # "text/plain" 如果上传的是一个文本文件，可以去掉content_type,，默认文件类型是文本文件。
    file = {"file1": ("test.txt", f, "text/plain")}  # MIME类型：text/plain、image/png、image/gif、application/json
    r = requests.post(url, files=file)
    print(r.text)
    # \u4e2d\u6587\u5b57  unicode编码的，网上有unicode转中文/中文转unicode的小工具，可以在线转。

# 上传一个图片文件，100K以内网速不好越小越好
with open("D:\\360SoftMgrGame\\1.jpg", mode='rb') as f:
    file = {"file1": ("1.jpg", f, "image/jpg")}
    r = requests.post(url, files=file)
    print(r.text)

# 可以一次上传多个文件
with open("D:/Lenovo/test.txt", encoding='utf-8')as f1:
    with open("D:/Lenovo/test1.txt", encoding='utf-8')as f2:
        with open("D:/360SoftMgrGame/1.jpg", mode='rb')as f3:
            file = {
                "file3": ("1.jpg", f3, "image/jpg"),
                "file1": ("test.txt", f1),
                "file2": ("test1.txt", f2)
            }
            r = requests.post(url, files=file)
            print(r.text)
