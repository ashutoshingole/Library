import MySQLdb as MS

db1 = MS.connect(host="localhost",user="root",passwd="")
cursor = db1.cursor()
# sql = 'CREATE DATABASE IF NOT EXISTS Library'
# cursor.execute(sql)
cursor.execute("""USE Library""")
sql_1 = '''CREATE TABLE Books(
       title TEXT,
       author TEXT, 
       genre Text, 
       rating REAL, 
       ISBN Text,
       price INTEGER,
       info Text
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1
       '''
cursor.execute(sql_1)

sql_2 = '''CREATE TABLE Authors(
       name TEXT,
       info TEXT
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1
       '''
cursor.execute(sql_2)

db1.commit()
db1.close()