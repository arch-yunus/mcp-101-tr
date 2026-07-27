import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "local_data.db"

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    summary TEXT NOT NULL
)
"""

SAMPLE_DATA = [
    ("MCP Nedir?", "Model Context Protocol, yapay zekanın dış kaynaklarla çalışmasını standartlaştırır."),
    ("Python ve MCP", "Python, MCP sunucuları için hızlı prototip geliştirmeye uygundur."),
]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    with conn:
        conn.execute(CREATE_SQL)
        conn.executemany("INSERT INTO articles (title, summary) VALUES (?, ?)", SAMPLE_DATA)
    conn.close()


def read_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT id, title, summary FROM articles")
    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    for article in read_articles():
        print(f"ID: {article[0]}\nBaşlık: {article[1]}\nÖzet: {article[2]}\n---")
