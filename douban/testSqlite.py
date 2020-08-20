import sqlite3

# conn = sqlite3.connect('test.db')
# print('connect successfully')

conn = sqlite3.connect('test.db')
print('open successfully')
c = conn.cursor()
sql = '''
    create table user 
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
c.execute(sql)
conn.commit()
conn.close()
print("创建成功")