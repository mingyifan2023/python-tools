import pymysql

import random
import string


class Mock_DB_dt():
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))


    

    def init_db_cursor(self,host,user,password,database):
        #             连接到数据库
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4'
        )
        cur = conn.cursor()

        return  cur,conn


    def insert_db(self,dbname,tlname,column_list):



        cursor,conn = self.init_db_cursor(host='127.0.0.1',user='root',password='123456',database=dbname)
        # 获取表的结构信息
        cursor.execute(f"DESCRIBE {tlname}")
        columns = [row[0] for row in cursor.fetchall()]

        # 生成模拟的INSERT语句
        insert_values = []
        for column in column_list:
            if column == "aaa":
                insert_values.append("aaa")
            elif column == "aaa":
                insert_values.append(random.choice(["192.168.56.139","192.168.56.84"]))
            else:
                insert_values.append(self.generate_random_string(10))

        # 构建INSERT语句
        columns_str = ', '.join(column_list)
        values_str = ', '.join(['%s'] * len(insert_values))
        insert_statement = f"INSERT INTO {tlname} ({columns_str}) VALUES ({values_str})"

        # 执行插入动作
        cursor.execute(insert_statement, insert_values)
        conn.commit()

        cursor.close()


if __name__=="__main__":
    column_list = ["abc"]
    mock_db_tl = Mock_DB_dt()
    for item in range(20):
        mock_db_tl.insert_db('abc',"dd",column_list)
