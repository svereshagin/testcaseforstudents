import psycopg2
from ..settings import DB_CONFIG

conn = psycopg2.connect(user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        port=DB_CONFIG['port'],
                        host=DB_CONFIG['host'],
                        dbname=DB_CONFIG['dbname'])

cur = conn.cursor()

cur.execute("SELECT * FROM students")
records = cur.fetchall()   
print(records)