# 测试前置：获取测试数据，数据是列表，通过readyaml读取出来
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("/ZongHe/data_case/register_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param


# 注册成功
def register(pass_data, url, db, baserequests):
    # 发送请求
    phone = pass_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    r = Member.register(url, baserequests, pass_data['casedata'])
    DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml("/ZongHe/data_case/login_setup.yaml"))
def pass_data(request):  # 固定写法
    return request.param


# 登录成功
def test_login_pass(register, pass_data, url, baserequests):
    # 发送请求
    r = Member.login(url, baserequests, pass_data['casedata'])
    # 1、检查响应的结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])

