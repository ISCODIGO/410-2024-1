import sqlite3


class Database:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def open(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create(self, sql: str, data: tuple):
        self.open()
        self.cursor.execute(sql, data)
        self.connection.commit()
        self.connection.close()

    def read(self, sql: str, data: tuple):
        self.open()
        self.cursor.execute(sql, data)
        data = self.cursor.fetchone()
        self.connection.close()
        return data

    def update(self, sql: str, data: tuple):
        self.open()
        self.cursor.execute(sql, data)
        self.connection.commit()
        self.connection.close()

    def delete(self, sql: str, data: tuple):
        self.open()
        self.cursor.execute(sql, data)
        self.connection.commit()
        self.connection.close()
