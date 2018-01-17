from lab6.models import *

#
# db = MySQLdb.connect(host="localhost", user="kirill",
#                      password="1234", db="lab6_db")
# cur = db.cursor()
#
# cur.execute("INSERT INTO books (name, description) VALUES ('Stoik', 'Draizer');")
# db.commit()
# cur.execute('SELECT * FROM books;')
# entries = cur.fetchall()
#
# for e in entries:
#     print(e)
#
# cur.close()
# db.close()
import MySQLdb


class Connection:
    def __init__(self, user, password, db, host="localhost"):
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Book:

    def __init__(self, db_con, name, descr):
        self.db_con = db_con.connection
        self.name = name
        self.descr = descr

    def save(self):
        c = self.db_con.cursor()
        c.execute("INSERT INTO books (name, description) VALUES (%s, %s);",
                  (self.name, self.descr))
        self.db_con.commit()
        c.close()


conect = Connection("kirill", "1234", "lab6_db")

with conect:
    book = Book(conect,'New', "New description of book")
    book.save()
