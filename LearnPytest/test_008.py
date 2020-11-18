"""取现接口"""
from unittest import mock
import requests


class JinRong:
    def chongzhi(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data).json()
        return r

    def quxian(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data).json()
        return r


class TestJinRONG:
    def test_quxian(self):
        # 对要模拟的类创建一个对象
        jinrong = JinRong()
        c = {"mobilephone": 18012345678, "amount": 1000}
        r = jinrong.chongzhi(c)
        print(r)
        assert r['msg'] == "充值成功"
        assert r['status'] == 1
        assert r['code'] == str(10001)

        # {'status':0,'code':'20102','data':None,'msg':'服务器异常'}
        jinrong.quxian = mock.Mock(return_value={'status': 1, 'code': '10001', 'data': None, 'msg': '取现成功'})
        data = {"mobilephone": 18012345678, "amount": 100}
        r = jinrong.quxian(data)
        print(r)
        assert r['msg'] == "取现成功"
        assert r['status'] == 1
        assert r['code'] == str(10001)










