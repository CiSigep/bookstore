import sqlite3


class Database:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, "
            "isbn INTEGER)")
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books(title, author, year, isbn) VALUES(?,?,?,?)", (title, author, year, isbn))

    def view_all(self):
        self.cursor.execute("SELECT * FROM books")
        results = self.cursor.fetchall()
        return results

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
                            (title, author, year, isbn))
        results = self.cursor.fetchall()
        return results

    def delete(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.connection.commit()

    def update(self, book_id, title, author, year, isbn):
        self.cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
                            (title, author, year, isbn, book_id))
        self.connection.commit()
