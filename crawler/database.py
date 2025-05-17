"""
    crawler/database.py
    This module contains functions to interact with the SQLite database.
"""

import sqlite3

def init_db():
    conn = sqlite3.connect('crawler_data.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS pages (
                        url TEXT PRIMARY KEY,
                        title TEXT,
                        summary TEXT
                    )''')
    conn.commit()

    return conn

def insert_page(conn, url: str, title: str, summary: str):
    """
    Insert a page into the database.

    Inputs:
        conn (sqlite3.Connection): The SQLite connection object.
        url (str): The URL of the page.
        title (str): The title of the page.
        summary (str): The summary of the page.
    """
    try:
        conn.execute("INSERT OR IGNORE INTO pages (url, title, summary) VALUES (?, ?, ?)", (url, title, summary))
        conn.commit()
    except:
        pass
