import sqlite3
from pathlib import Path
from typing import Iterator, Tuple

DB_PATH = Path('.planning/tracer.db')

def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        photo_path TEXT,
        dimensions TEXT,
        category TEXT,
        tag TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS costs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        item_id INTEGER,
        quote_pdf_path TEXT,
        paid INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(item_id) REFERENCES items(id)
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS milestones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        due_date TEXT,
        complete INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def iter_items() -> Iterator[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM items ORDER BY id'):
        yield row
    conn.close()

def insert_item(name, photo_path=None, dimensions=None, category=None, tag=None) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name, photo_path, dimensions, category, tag) VALUES (?,?,?,?,?)',
                (name, photo_path, dimensions, category, tag))
    conn.commit()
    id_ = cur.lastrowid
    conn.close()
    return id_

def insert_cost(description, amount, category=None, item_id=None, quote_pdf_path=None, paid=False) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO costs (description, amount, category, item_id, quote_pdf_path, paid) VALUES (?,?,?,?,?,?)',
                (description, float(amount), category, item_id, quote_pdf_path, int(bool(paid))))
    conn.commit()
    id_ = cur.lastrowid
    conn.close()
    return id_

def insert_milestone(title, due_date=None) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO milestones (title, due_date) VALUES (?,?)', (title, due_date))
    conn.commit()
    id_ = cur.lastrowid
    conn.close()
    return id_

def list_costs() -> Iterator[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM costs ORDER BY id'):
        yield row
    conn.close()

def list_milestones() -> Iterator[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM milestones ORDER BY id'):
        yield row
    conn.close()
