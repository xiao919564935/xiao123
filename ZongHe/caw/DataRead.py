"""
读文件的公共方法
"""
import configparser
import os

import yaml


def getProjectPath():
    '''
    获取当前工程路径
    :return:
    '''
    current__file__path = os.path.realpath(__file__)  # 当前文件路径
    # print(current__file__path)
    dir_name = os.path.dirname(current__file__path)  # 文件所在的目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)  # 上一级目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name)  # 上一级目录
    return dir_name + "\\"


def readini(filePath, key):
    '''
    读取ini文件
    :param filePath: 文件路径
    :param key: ini中的关键字
    :return: key对应的value
    '''
    real_path = getProjectPath() + filePath
    # 调用configparser来解析配置文件
    config = configparser.ConfigParser()
    # 读文件
    config.read(real_path)
    #  env表示section，根据key在对应的section中取value
    value = config.get("env", key)
    return value


def readyaml(filePath):
    '''
    读取yaml文件
    :param filePath:
    :param key:
    :return:
    '''
    real_path = getProjectPath() + filePath  # 拼接完整路径
    with open(real_path, "r", encoding="utf-8")as f:  # 打开文件
        content = yaml.load(f, Loader=yaml.FullLoader)  # 读取文件内容，放到变量content中
        return content


# 测试代码，用完可以删除
if __name__ == '__main__':
    # 逾期返回 D:\Lenovo\ApiAutoTest\
    print(getProjectPath())
    # 逾期返回http://jy001:8081/
    # print(readini(r"\ZongHe\data_env\env.ini", "url"))
    # print(readini(r"\ZongHe\data_env\env.ini", "db"))
    content = readyaml(r"\ZongHe\data_case\register_fail.yaml")
    print(content)

