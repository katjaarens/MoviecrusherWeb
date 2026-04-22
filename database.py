import sqlite3

class Database:
    def __init__(self, db_name="moviecrusher.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                alter_ INTEGER NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                shorty TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                movie_id INTEGER NOT NULL,
                rating REAL NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS watchlist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                movie_id INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_user(self, name, email, alter_):
        self.cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        existing = self.cursor.fetchone()
        if existing:
            return existing[0]
        self.cursor.execute(
            "INSERT INTO users (name, email, alter_) VALUES (?, ?, ?)",
            (name, email, alter_)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def login(self, email):
        self.cursor.execute(
            "SELECT id, name, email, alter_ FROM users WHERE email = ?",
            (email,)
        )
        return self.cursor.fetchone()

    def add_movie(self, title, genre, release_year):
        self.cursor.execute(
            "INSERT INTO movies (title, genre, release_year) VALUES (?, ?, ?)",
            (title, genre, release_year)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def search_movies(self, keyword):
        self.cursor.execute("""
            SELECT movies.id, movies.title, movies.genre, movies.release_year, avg(ratings.rating)
            FROM movies
            LEFT JOIN ratings ON movies.id = ratings.movie_id
            WHERE movies.title LIKE ? OR movies.genre LIKE ?
            GROUP BY movies.id
        """, (f"%{keyword}%", f"%{keyword}%"))
        return self.cursor.fetchall()

    def get_movie_description(self, movie_id):
        self.cursor.execute("SELECT shorty FROM movies WHERE id = ?", (movie_id,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def get_all_titles(self):
        self.cursor.execute("SELECT title FROM movies")
        return [row[0] for row in self.cursor.fetchall()]

    def add_rating(self, user_id, movie_id, rating):
        self.cursor.execute(
            "INSERT INTO ratings (user_id, movie_id, rating) VALUES (?, ?, ?)",
            (user_id, movie_id, rating)
        )
        self.conn.commit()

    def add_to_watchlist(self, user_id, movie_id):
        self.cursor.execute(
            "INSERT INTO watchlist (user_id, movie_id) VALUES (?, ?)",
            (user_id, movie_id)
        )
        self.conn.commit()

    def get_watchlist(self, user_id):
        self.cursor.execute("""
            SELECT movies.id, movies.title, movies.genre, movies.release_year
            FROM movies
            JOIN watchlist ON movies.id = watchlist.movie_id
            WHERE watchlist.user_id = ?
        """, (user_id,))
        return self.cursor.fetchall()

    def get_stats(self, user_id):
        self.cursor.execute("SELECT COUNT(*) FROM movies")
        total_movies = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM ratings WHERE user_id = ?", (user_id,))
        user_ratings = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM watchlist WHERE user_id = ?", (user_id,))
        watchlist_size = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT AVG(rating) FROM ratings WHERE user_id = ?", (user_id,))
        avg_rating = self.cursor.fetchone()[0] or 0.0

        return {
            "total_movies": total_movies,
            "user_ratings": user_ratings,
            "watchlist_size": watchlist_size,
            "avg_rating": round(avg_rating, 1)
        }

    def add_description(self, movie_id, description):
        self.cursor.execute(
            "UPDATE movies SET shorty = ? WHERE id = ?",
            (description, movie_id)
        )
        self.conn.commit()
