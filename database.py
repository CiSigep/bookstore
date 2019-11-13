import sqlite3


def connect():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, "
                   "isbn INTEGER)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books(title, author, year, isbn) VALUES(?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def view_all():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    connection.close()
    return results


def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
                   (title, author, year, isbn))
    results = cursor.fetchall()
    connection.close()
    return results


def delete(book_id):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()


def update(book_id, title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
                   (title, author, year, isbn, book_id))
    connection.commit()
    connection.close()


connect()
