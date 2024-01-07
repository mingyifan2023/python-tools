# -*- coding: utf-8 -*-
import sqlite3
"""
文章来源：https://mp.weixin.qq.com/s/ANRGdO-gcX5plOef5qE0nQ

详细介绍，请参阅原文！

"""

class sqliteTools():
    def __init__(self, name):
        self.db_name = name

    @property
    def connect(self):
        # 连接到数据库（如果不存在，则会自动创建）
        conn = sqlite3.connect(self.db_name)
        # 创建一个游标对象
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def connect_close(conn, cursor):
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

    def create_table(self, sql):
        """
        创建表
        :param sql: 创建表的sql
        :return:
        """
        conn, cursor = self.connect
        cursor.execute(sql)
        self.connect_close(conn, cursor)

    def insert(self, sql):
        """
        插入
        :param sql: sql语句
        :return:
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.execute(sql).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def insert_many(self, sql, values):
        """
        批量插入数据
        :param sql: sql语句
        :param values: 插入的数据
        :return: 返回插入数据量
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.executemany(sql, values).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def delete(self, sql):
        """
        删除数据
        :param sql: sql语句
        :return: 返回删除的数量
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.execute(sql).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def delete_many(self, sql, values):
        """
        批量删除数据
        :param sql: sql语句
        :param values: 删除数据的集合
        :return: 返回删除的数量
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.executemany(sql, values).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def update(self, sql):
        """
        更新数据
        :param sql: sql语句
        :return: 返回更新的数量
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.execute(sql).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def update_many(self, sql, values):
        """
        批量更新数据
        :param sql: sql语句
        :param values: 参数
        :return: 返回更新的数量
        """
        conn, cursor = self.connect
        try:
            row_count = cursor.executemany(sql, values).rowcount
            conn.commit()
        except:
            row_count = 0
            conn.rollback()
        finally:
            self.connect_close(conn, cursor)
        return row_count

    def select(self, sql):
        """
        单条查询
        :param sql: 查询语句
        :return: 返回查询结果
        """
        conn, cursor = self.connect
        try:
            cursor.execute(sql)
            row_data = cursor.fetchone()
        finally:
            self.connect_close(conn, cursor)
        return row_data

    def select_many(self, sql):
        """
        批量查询
        :param sql: 查询语句
        :return: 返回查询结果
        """
        conn, cursor = self.connect
        try:
            cursor.execute(sql)
            row_data = cursor.fetchall()
        finally:
            self.connect_close(conn, cursor)
        return row_data

    def select_define_data(self, sql, num):
        """
        自定义查询前xxx条数据
        :param sql: 查询sql语句
        :param num: 查询的条数
        :return: 返回查询结果
        """
        conn, cursor = self.connect
        try:
            cursor.execute(sql)
            result = cursor.fetchmany(num)
        finally:
            self.connect_close(conn, cursor)
        return result


