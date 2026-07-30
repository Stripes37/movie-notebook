import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).resolve().parent.parent  # Gets the project root directory
    / "data"
    / "movie_notebook.db"
)


# Database connection function
def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)  # Opens or creates the database
    connection.row_factory = sqlite3.Row  # Allows access by column name

    return connection


# Initialize the database
def initialize_database() -> None:
    connection = get_connection()

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS films (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.commit()
    finally:
        connection.close()

# Function to add a film
def add_film(title: str, release_year: int) -> int:
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO films (title, release_year)
            VALUES (?,?)
            """,
            (title, release_year)
        )
        connection.commit()

        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a film ID.")

        return cursor.lastrowid

    finally:
        connection.close()

# Function to retrieve film
def get_films() -> list[dict[str, object]]:
    connection = get_connection()

    try:
        rows = connection.execute(
            """
            SELECT id, title, release_year, created_at
            FROM films
            ORDER BY title ASC, release_year ASC
            """
        ).fetchall()

        return [dict(row) for row in rows]

    finally: 
        connection.close()