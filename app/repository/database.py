import psycopg2
from ..settings import DB_CONFIG

conn = psycopg2.connect(user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        port=DB_CONFIG['port'],
                        host=DB_CONFIG['host'],
                        dbname=DB_CONFIG['dbname'])

class BaseRepo():
    def __get_cursor(cls):
        return conn.cursor()
    def ping_tables(cls):
        # cur = cls.__get_cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cats")
        print(cur.fetchall())
    def get_cats():
        cur = conn.cursor()
        cur.execute("SELECT * FROM cats")
        print(cur.fetchall())


    def create_cat(name, color, tail_length, whiskers_length):
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO cats(name, color, tail_length, whiskers_length) VALUES (%s, %s, %s, %s)', 
                (name, color, tail_length, whiskers_length)
            )
            conn.commit()  # Не забываем коммитить изменения

    def delete_cat(name):
        cur = conn.cursor()
        cur.execute('DELETE FROM cats WHERE name=(%s,)', (name))

    @classmethod
    def update_cat(cls, name, new_tail_length):
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE cats SET tail_length = %s WHERE name = %s", 
                (new_tail_length, name)
            )
            conn.commit()


baseRepo = BaseRepo()
baseRepo.update_cat(name='Musya', new_tail_length=1123123)
