import psycopg2
from ..settings import DB_CONFIG


class BaseRepo():
    def __init__(self):
        self.conn = psycopg2.connect(user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        port=DB_CONFIG['port'],
                        host=DB_CONFIG['host'],
                        dbname=DB_CONFIG['dbname'])
        self.curr = self.conn.cursor()

    def ping_tables(self):
        self.curr.execute("SELECT * FROM cats")
        print(self.curr.fetchall())

    def get_cats(self):
        self.curr.execute("SELECT * FROM cats")
        print(self.curr.fetchall())


    def create_cat(self,name, color, tail_length, whiskers_length):
        with self.conn.cursor() as cur:
            cur.execute(
                'INSERT INTO cats(name, color, tail_length, whiskers_length) VALUES (%s, %s, %s, %s)',  #INSERT INTO - добавить в #cats - таблица в скобках к таблице идут поля в которые 
                                                                                                        #мы вносим данные.после VALUES #где %s %s %s %s - "экранирование слов". 
                (name, color, tail_length, whiskers_length)                                             # аргументы которые будут подставлены(мы их передаём в функцию/метод)
            )                                                                                           # подтвердить изменения
            self.conn.commit()                                                                          # подтверждаем, нужно при изменении данных
            
    def delete_cat(self,name):
        self.curr.execute('DELETE FROM cats WHERE name=%s', (name,))

    def update_cat(self, name, new_tail_length):
        self.curr.execute(
            "UPDATE cats SET tail_length = %s WHERE name = %s", 
            (new_tail_length, name)
        )
        self.conn.commit()


baseRepo = BaseRepo()
baseRepo.ping_tables()
baseRepo.update_cat(name='Vika', new_tail_length=123)