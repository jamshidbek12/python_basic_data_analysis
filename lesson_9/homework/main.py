# Custom exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def can_borrow(self):
        return len(self.borrowed_books) < 3

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"'{title}' topilmadi")
    
    def borrow_book(self, member, title):
        book = self.find_book(title)
        
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{title}' allaqachon olingan")
        
        if not member.can_borrow():
            raise MemberLimitExceededException(f"{member.name} 3 tadan ko'p kitob ololmaydi")
        
        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member.name} '{title}' kitobini oldi")
    
    def return_book(self, member, title):
        book = self.find_book(title)
        
        if book in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            print(f"{member.name} '{title}' kitobini qaytardi")
        else:
            print(f"{member.name} bu kitobni olmagan")

# Test
library = Library()

# Kitoblar qo'shish
library.add_book(Book("O'tkan kunlar", "Abdulla Qodiriy"))
library.add_book(Book("Mehrobdan chayon", "Abdulla Qahhor"))
library.add_book(Book("Ikki eshik orasi", "O'tkir Hoshimov"))
library.add_book(Book("Dunyoning ishlari", "O'tkir Hoshimov"))

# A'zolar qo'shish
ali = Member("Ali")
vali = Member("Vali")
library.add_member(ali)
library.add_member(vali)

# Test 1
try:
    library.borrow_book(ali, "O'tkan kunlar")
    library.borrow_book(ali, "Mehrobdan chayon")
    library.return_book(ali, "O'tkan kunlar")
except Exception as e:
    print(f"Xato: {e}")

# Test 2
try:
    library.borrow_book(vali, "Mehrobdan chayon")
except BookAlreadyBorrowedException as e:
    print(f"Xato: {e}")

# Test 3
try:
    library.borrow_book(ali, "O'tkan kunlar")
    library.borrow_book(ali, "Ikki eshik orasi")
    library.borrow_book(ali, "Dunyoning ishlari")  # 3-chi kitob
    library.borrow_book(ali, "Yangi kitob")  # 4-chi kitob - xato
except MemberLimitExceededException as e:
    print(f"Xato: {e}")

# Test 4
try:
    library.borrow_book(vali, "Mavjud emas")
except BookNotFoundException as e:
    print(f"Xato: {e}")

print(f"\n{ali.name}ning kitoblari: {[b.title for b in ali.borrowed_books]}")