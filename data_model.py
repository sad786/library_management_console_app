import sqlite3
from datetime import datetime

class Database:
    # here database setup 
    def setup_database(self):
        conn = sqlite3.connect('library.db')
        cur = conn.cursor()

        # Users Table is here 
        cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL)
                    """)
        
        # books table is here
        cur.execute("""
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    available INTEGER DEFAULT 1)
                """)
        
        # borrow request table
        cur.execute("""
                CREATE TABLE IF NOT EXISTS borrow_requests(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    book_id INTEGER NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    FOREIGN KEY(user_id)
                    REFERENCES users(id),
                    FOREIGN KEY(book_id)
                    REFERENCES books(id))
                    """)
        
        # Borrow History table 
        cur.execute("""
                CREATE TABLE IF NOT EXISTS
                    borrow_history(
                    user_id INTEGER NOT NULL,
                    book_id INTEGER NOT NULL,
                    borrowed_date TEXT NOT NULL,
                    returned_date TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(book_id) REFERENCES books(id))
                    """)
        conn.commit() #executing database instructions
        conn.close() #closing connection of database
