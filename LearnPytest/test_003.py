"""
比较灵活的测试前置和后置。fixture
1.不受setup、teardown命名限制
2.使用灵活
"""
import pytest


# 测试前置,使用fixture来修饰
@pytest.fixture(scope='module')  # 作用域：module级别，首次调用这个fixture的地方执行前置全部用例执行完，执行后置。
def login():
    print("系统登录")  # yield之前是前置
    yield
    print("退出登录")  # yield之后是后置


@pytest.fixture(autouse=True)
def db_op():
    print("连接数据库成功")
    yield
    print("断开数据库连接")


def test_001():
    print("用例1：查询操作，不需要登录")


# 使用方法1：将测试前置login作为参数传入（常用）
def test_002(login):
    print("用例2：添加操作，需要登录")


# 使用方法2：usefixtures使用前置login
@pytest.mark.usefixtures('login')
def test_003():
    print("用例3：删除操作，需要登录")
