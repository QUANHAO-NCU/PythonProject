import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('create table test (id varchar (10) primary  key,name varchar (20))')
# cursor.execute('insert into test(id,name) values (\'4\',\'赵六\')')
conn.commit()
lines = list(cursor.execute('select count(*) from test'))[0][0]
onerecord = cursor.execute('select id,name from test where id =2')
word = list(onerecord)[0][1]
print(word)
print(lines)