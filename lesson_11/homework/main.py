import sqlite3

with sqlite3.connect('roster.db') as conn:
    c = conn.cursor()
    
    c.execute('CREATE TABLE Roster (Name TEXT, Species TEXT, Age INTEGER)')
    
    c.executemany('INSERT INTO Roster VALUES (?, ?, ?)', [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ])
    
    c.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    
    print("Bajoran characters:")
    for row in c.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"):
        print(row)
    
    c.execute('DELETE FROM Roster WHERE Age > 100')
    
    c.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
    
    c.executemany('UPDATE Roster SET Rank = ? WHERE Name = ?', [
        ('Captain', 'Benjamin Sisko'),
        ('Lieutenant', 'Ezri Dax'),
        ('Major', 'Kira Nerys')
    ])
    
    print("\nAll characters by age (descending):")
    for row in c.execute('SELECT * FROM Roster ORDER BY Age DESC'):
        print(row)

with sqlite3.connect('library.db') as conn:
    c = conn.cursor()
    
    c.execute('CREATE TABLE Books (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)')
    
    c.executemany('INSERT INTO Books VALUES (?, ?, ?, ?)', [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ])
    
    c.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    
    print("\nDystopian books:")
    for row in c.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"):
        print(row)
    
    c.execute('DELETE FROM Books WHERE Year_Published < 1950')
    
    c.execute('ALTER TABLE Books ADD COLUMN Rating REAL')
    
    c.executemany('UPDATE Books SET Rating = ? WHERE Title = ?', [
        (4.8, 'To Kill a Mockingbird'),
        (4.7, '1984'),
        (4.5, 'The Great Gatsby')
    ])
    
    print("\nAll books by year (ascending):")
    for row in c.execute('SELECT * FROM Books ORDER BY Year_Published ASC'):
        print(row)