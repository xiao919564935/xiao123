"""
Pytest命名规则：
1.测试文件以test_开头或结尾
2.测试类以Test开头
3.测试方法以test_开头
"""
import json

import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone": 137123456789, "pwd": 123456, "regname": "aaa"}
    # 预期结果
    expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    print(json.dumps(expect))  # 字典转json
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


# 手机号不能为空
def test_register_002():
    # 测试数据
    data = {"pwd": "123456abc", "regname": "aaa"}
    # 预期结果
    expect = {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


# 手机号码已被注册
def test_register_003():
    # 测试数据
    data = {"mobilephone": "13745241111", "pwd": "123456abc", "regname": "aaa"}
    # 预期结果
    expect = {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


# 注册成功
def test_register_004():
    # 测试数据
    data = {"mobilephone": "13745441242", "pwd": "123456789012345678", "regname": "aaa"}
    # 预期结果
    expect = {"status": "1", "code": "10001", "msg": "注册成功"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


# 登录成功
def test_register_005():
    # 测试数据
    data = {"mobilephone": "13745241111", "pwd": "123456abc"}
    # 预期结果
    expect = {"status": 1, "code": "20110", "data": None, "msg": "登录成功"}
    # 测试步骤
    real = register(data)
    # 检查结果
    # # assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
