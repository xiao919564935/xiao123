'''
数据库操作
1、数据库从mysql换成sqlite,脚本层不用改动，只需要改动caw里面的MySqlOp.py以及这个文件
2、这部分访问到业务的数据库，所以放到baw中
'''
from ZongHe.caw import MySqlOp


def deleteUser(db, phone):
    '''
    根据手机号删除用户
    :param db: 一个字点，存储数据库信息
    :param phone: 手机号
    :return:
    '''
    conn = MySqlOp.connect(db)
    MySqlOp.execute(conn, f'delete from Member where MobilePhone ={phone};')
    MySqlOp.disconnect(conn)






