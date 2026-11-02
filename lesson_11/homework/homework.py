import sqlite3

def task_1_roster():
    # 1. Create database and table
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS Roster (
                Name TEXT,
                Species TEXT,
                Age INTEGER
            )
        """
        cursor.execute(query)

    # 2. Insert data
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        data = [
            ("Benjamin Sisko", "Human", 40),
            ("Jadzia Dax", "Trill", 300),
            ("Kira Nerys", "Bajoran", 29),
        ]
        cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", data)
 
    # 3. Update data: rename Jadzia Dax -> Ezri Dax
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax'
        """
        cursor.execute(query)

    # 4. Query data: Name and Age where Species is Bajoran
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            SELECT Name, Age FROM Roster WHERE Species='Bajoran'
        """
        data = cursor.execute(query)
        print("Bajoran characters (Name, Age):", data.fetchall())

    # 5. Delete data: remove characters aged over 100
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            DELETE FROM Roster WHERE Age > 100
        """
        cursor.execute(query)

    # 6. Bonus: Add Rank column and populate it
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            ALTER TABLE Roster ADD COLUMN Rank TEXT
        """
        cursor.execute(query)

    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko';
            UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax';
            UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys';
        """
        cursor.executescript(query)

    # 7. Advanced query: all characters sorted by Age descending
    with sqlite3.connect('roster.db') as conn:
        cursor = conn.cursor()
        query = """
            SELECT * FROM Roster ORDER BY Age DESC;
        """
        data = cursor.execute(query)
        print("Roster sorted by Age (desc):", data.fetchall())


def task_2_library():
    # 1. Create database and table
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS Books (
                Title TEXT,
                Author TEXT,
                Year_Published INTEGER,
                Genre TEXT
            )
        """
        cursor.execute(query)

    # 2. Insert data
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        data = [
            ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
            ('1984', 'George Orwell', 1949, 'Dystopian'),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic'),
        ]
        cursor.executemany("INSERT INTO Books VALUES(?, ?, ?, ?);", data)

    # 3. Update data: fix publication year of 1984
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            UPDATE Books SET Year_Published=1950 WHERE Title='1984'
        """
        cursor.execute(query)

    # 4. Query data: Title and Author where Genre is Dystopian
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            SELECT Title, Author FROM Books WHERE Genre='Dystopian'
        """
        data = cursor.execute(query)
        print("Dystopian books (Title, Author):", data.fetchall())

    # 5. Delete data: remove books published before 1950
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            DELETE FROM Books WHERE Year_Published < 1950
        """
        cursor.execute(query)

    # 6. Bonus: Add Rating column and populate it
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            ALTER TABLE Books ADD COLUMN Rating TEXT
        """
        cursor.execute(query)

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird';
            UPDATE Books SET Rating=4.7 WHERE Title='1984';
            UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby';
        """
        cursor.executescript(query)

    # 7. Advanced query: all books sorted by Year_Published ascending
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = """
            SELECT * FROM Books ORDER BY Year_Published
        """
        data = cursor.execute(query)
        print("Books sorted by Year_Published (asc):", data.fetchall())


if __name__ == "__main__":
    print("=== Task 1: Roster ===")
    task_1_roster()

    print("\n=== Task 2: Library ===")
    task_2_library()