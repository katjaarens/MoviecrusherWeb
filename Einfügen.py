# 'import sqlite3



# conn = sqlite3.connect("moviecrusher.db")

# cursor = conn.cursor()



# cursor.executescript("""

# INSERT INTO movies (title, genre, release_year) VALUES

# ('Goodfellas', 'Crime', 1990),

# ('Pretty Woman', 'Romance', 1990),

# ('Terminator 2: Judgment Day', 'Action', 1991),

# ('The Silence of the Lambs', 'Thriller', 1991),

# ('Reservoir Dogs', 'Crime', 1992),

# ('Aladdin', 'Animation', 1992),

# ('Jurassic Park', 'Adventure', 1993),

# ('Schindler''s List', 'Drama', 1993),

# ('The Lion King', 'Animation', 1994),

# ('Forrest Gump', 'Drama', 1994),

# ('Se7en', 'Thriller', 1995),

# ('Toy Story', 'Animation', 1995),

# ('Heat', 'Crime', 1995),

# ('Independence Day', 'Sci-Fi', 1996),

# ('Fargo', 'Crime', 1996),

# ('The Fifth Element', 'Sci-Fi', 1997),

# ('Good Will Hunting', 'Drama', 1997),

# ('Saving Private Ryan', 'War', 1998),

# ('The Truman Show', 'Drama', 1998),

# ('The Big Lebowski', 'Comedy', 1998),

# ('Fight Club', 'Drama', 1999),

# ('The Green Mile', 'Drama', 1999),

# ('American Beauty', 'Drama', 1999),

# ('Gladiator', 'Action', 2000),

# ('Memento', 'Thriller', 2000),

# ('Requiem for a Dream', 'Drama', 2000),

# ('The Lord of the Rings: The Fellowship of the Ring', 'Fantasy', 2001),

# ('Donnie Darko', 'Drama', 2001),

# ('Shrek', 'Animation', 2001),

# ('The Lord of the Rings: The Two Towers', 'Fantasy', 2002),

# ('City of God', 'Crime', 2002),

# ('Spider-Man', 'Action', 2002),

# ('The Lord of the Rings: The Return of the King', 'Fantasy', 2003),

# ('Kill Bill: Vol. 1', 'Action', 2003),

# ('Lost in Translation', 'Drama', 2003),

# ('Eternal Sunshine of the Spotless Mind', 'Drama', 2004),

# ('The Incredibles', 'Animation', 2004),

# ('Batman Begins', 'Action', 2005),

# ('Sin City', 'Crime', 2005),

# ('Brokeback Mountain', 'Drama', 2005),

# ('The Departed', 'Crime', 2006),

# ('Pan''s Labyrinth', 'Fantasy', 2006),

# ('Casino Royale', 'Action', 2006),

# ('No Country for Old Men', 'Thriller', 2007),

# ('Ratatouille', 'Animation', 2007),

# ('There Will Be Blood', 'Drama', 2007),

# ('The Dark Knight', 'Action', 2008),

# ('WALL-E', 'Animation', 2008),

# ('Slumdog Millionaire', 'Drama', 2008),

# ('Avatar', 'Sci-Fi', 2009),

# ('Inglourious Basterds', 'War', 2009),

# ('Up', 'Animation', 2009),

# ('Shutter Island', 'Thriller', 2010),

# ('Inception', 'Sci-Fi', 2010),

# ('The Social Network', 'Drama', 2010);

# """)



# conn.commit()

# conn.close()'


import sqlite3

conn = sqlite3.connect("moviecrusher.db")
cursor = conn.cursor()

movies = [
    ("Schatten über Auria", "Sci-Fi", 2031,
     "In der futuristischen Stadt Auria entdeckt eine Ingenieurin ein geheimes Erinnerungsprojekt."),
    
    ("Der letzte Funke", "Drama", 2028,
     "Nach einem globalen Energieausfall kämpft eine Gruppe darum, eine Forschungsstation zu reaktivieren."),
    
    ("Nebelpfad", "Thriller", 2024,
     "Ein Ermittler kehrt zurück, um das Verschwinden eines Kindes im Küstennebel aufzuklären."),
    
    ("Herz aus Stahl", "Action", 2030,
     "Eine Pilotin muss in einer Eliteeinheit gigantische Kampfmaschinen steuern."),
    
    ("Die verlorene Melodie", "Drama", 2022,
     "Eine Musikerin verliert ihr Gehör und entdeckt neue Wege, Musik zu fühlen."),
    
    ("Jenseits der Sterne", "Sci-Fi", 2035,
     "Ein Astronaut strandet auf einem Planeten, der der Erde erstaunlich ähnelt."),
    
    ("Code der Vergangenheit", "Thriller", 2027,
     "Ein Hacker stößt auf Hinweise zu einem vertuschten Regierungsprojekt."),
    
    ("Die Farben des Windes", "Fantasy", 2023,
     "Eine Malerin trifft einen Jungen, der die Natur beeinflussen kann."),
    
    ("Nachtläufer", "Action", 2026,
     "Ein Ex-Dieb wird zu nächtlichen Geheimoperationen gezwungen und beginnt zu rebellieren."),
    
    ("Der Mechaniker von Morgen", "Sci-Fi", 2032,
     "Ein Mechaniker entdeckt einen Roboter mit eigenem Bewusstsein.")
]

sql = """
INSERT INTO movies (title, genre, release_year, shorty)
VALUES (?, ?, ?, ?)
"""

cursor.executemany(sql, movies)
conn.commit()
conn.close()

print("Filme erfolgreich eingefügt!")
