import csv
import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class NotEnoughCredentialsException(Exception):
    pass

class NameErrorException(Exception):
    pass

class MemberNotFoundException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"Book({self.title}, {self.author})"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, title, author):
        if not title:
            raise NotEnoughCredentialsException("Title not found")

        if not author:
            raise NotEnoughCredentialsException("Author not found")
        book = Book(title, author)
        available = "Available" if not book.is_borrowed else "Not available"
        # new_book = [book.title, book.author, book.is_borrowed]
        self.books.append(book)
        # print(f"Book successfully added!: {new_book[0]}, {new_book[1]}, {new_book[2]}")
        print(f"Book successfully added!: {book.title}, {book.author}, {available}\n")

    def add_member(self, name):
        if not name:
            raise NameErrorException("Name not found")
        member = Member(name)
        self.members[name] = member
        print(f"Member added: {name}\n")
    def borrow_book(self, member_name, title):
        if member_name not in self.members:
            raise MemberNotFoundException("Member not found")
        member = self.members[member_name]

        book = self.find_book(title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")

        if not member.can_borrow():
            raise MemberLimitExceededException("Member has reached the borrowing limit")

        book.is_borrowed = True
        member.borrowed_books.append(book.title)
        print(f"{member_name}, successfully borrowed '{book.title}'\n")


    def return_book(self, member_name, title):
        if member_name not in self.members:
            raise MemberNotFoundException("Member not found")
        member = self.members[member_name]

        titles_lower = [t.lower() for t in member.borrowed_books]
        if title.lower() not in titles_lower:
            raise BookNotFoundException("User does not have this book")

        index = titles_lower.index(title.lower())
        actual_title = member.borrowed_books[index]

        book = self.find_book(actual_title)
        book.is_borrowed = False
        member.borrowed_books.remove(actual_title)
        print(f"{member_name}, successfully returned '{book.title}'\n")

    def view_all(self):
        if not self.books:
            raise BookNotFoundException("Books not found")
        else:
            for book in self.books:
                available = "Available" if not book.is_borrowed else "Not available"
                print(f"{book.title}, {book.author}, {available}")

    def find_book(self, title):
        books = self.books
        for book in books:
            available = "Available" if not book.is_borrowed else "Not available"
            if book.title.lower() == title.lower():
                print(f"{book.title}, {book.author}, {available}")
                return book
        raise BookNotFoundException("Book not found")        
    def save(self):
        columns = ["Title", "Author", "Status"]
        data = self.books
        if not self.books:
            print("Books not found\n")
            return
        with open('library.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows([b.title, b.author, b.is_borrowed] for b in data)
        print("Successfully saved\n")

    def load(self):
        self.books = []
        try:
            with open('library.csv', 'rt') as file:
                reader = csv.reader(file)
                columns = next(reader)
                for row in reader:
                    book = Book(row[0], row[1])
                    book.is_borrowed = (row[2] == "True")
                    self.books.append(book)
            print("Successfully loaded\n")
        except FileNotFoundError:
            print("No saved file found, starting fresh.\n")

    def save_members(self):
        if not self.members:
            print("No members to save\n")
            return
        data = {}
        for name, member in self.members.items():
            data[name] = member.borrowed_books
        with open('members.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("Members saved successfully\n")

    def load_members(self):
        self.members = {}
        try:
            with open('members.json', 'r') as f:
                data = json.load(f)
            for name, borrowed_books in data.items():
                member = Member(name)
                member.borrowed_books = borrowed_books
                self.members[name] = member
            print("Members loaded successfully\n")
        except FileNotFoundError:
            print("No saved members file found, starting fresh.\n")

    def run(self):
        self.load()
        self.load_members()
        while True:
            print(f"1. Add book\n2. Add member\n3. Borrow book\n4. Return book\n5. View all books\n6. Find a book\n7. Save\n8. Load\n9. Exit")
            choice = input("Select: ")
            if choice not in ['1','2','3','4','5','6','7','8','9']:
                print(f"Not command found with {choice}")
                continue
            try:
                if choice == "9":
                    break
                elif choice == "1":
                    title = input("Title: ")
                    author = input("Author: ")
                    self.add_book(title, author)
                elif choice == "2":
                    member = input("Member name: ")
                    self.add_member(member)
                elif choice == "3":
                    member = input("Member name: ")
                    title = input("Title name: ")
                    self.borrow_book(member, title)
                elif choice == "4":
                    member = input("Member name: ")
                    title = input("Title name: ")
                    self.return_book(member, title)
                elif choice == "5":
                    self.view_all()
                elif choice == "6":
                    title = input("Searching title: ")
                    self.find_book(title)
                elif choice == "7":
                    self.save()
                    self.save_members()
                elif choice == "8":
                    self.load()
                    self.load_members()
            except (BookNotFoundException, NotEnoughCredentialsException, NameErrorException, MemberNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
                print(f"Error: {e}\n")
            print('\n')

manager_library = Library()
manager_library.run()
