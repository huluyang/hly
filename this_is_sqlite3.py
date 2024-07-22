import sqlite3

"""

python自带的小型数据库，可以用来做简单的数据存储

"""

conn = sqlite3.connect("aaa.db")
c = conn.cursor()
# 创建表
sql = """create table File(path char(10000) PRIMARY KEY NOT NULL)"""
c.execute(sql)
conn.commit()
conn.close()
print("数据表创建成功")

# 插入一条数据
# sql = """insert into File (path) values ('{}')"""
# c.execute(sql.format(r"aaaaaaa"))
# conn.commit()
# conn.close()

# 查询一条数据
# sql = """select 1 from File where path ='{}'"""
# c.execute(sql.format(r"aaaaaaa"))
# a = c.fetchall()
# print(a)
# if a:
#     print("ok")
# else:
#     print("no")
# conn.commit()
# conn.close()
