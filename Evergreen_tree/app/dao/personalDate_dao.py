# 导入连接池  用连接池创建链接
from app.dao.__init__ import POOL
import pymysql
from app.dao.sql.sql_personal_Date import sql_personal_date
import json





def get_personal_date(user_id):
    try:
        client=POOL.connection()#链接池创建链接
        res_data = None#定义返回值
        cursor = client.cursor(cursor=pymysql.cursors.DictCursor)#游标 操作数据和获取数据库结果都要通过游标来操作
        sql = sql_personal_date.get('get_personal_date').format(user_id=user_id['user_id'])#sql语句
        cursor.execute(sql)#执行sql语句
        res_data = cursor.fetchone()#获取返回的数据  只取一条
        client.commit()#链接提交事务  还有游标结束
    except Exception as ex:
        client.rollback()#出错的话  链接回滚
    finally:
        client.close()#结束链接  返回结果给服务层
        return res_data

if __name__ == '__main__':
    a={"telephone":18792031925}
    get_order_detail(a)