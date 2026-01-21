# #### Task 1: Create a Library Management System with Custom Exceptions
# 1. Create a Python program to manage a small library system.
# 2. Define custom exceptions for specific scenarios:
#    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
#    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
#    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# 3. Implement classes for:
#    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
#    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
#    - **`Library`**: Manages books and members, including borrowing and returning books.
# 4. Test your program with the following scenarios:
#    - Adding books and members.
#    - Borrowing and returning books.
#    - Handling exceptions when rules are violated.

# ---


from dataclasses import dataclass, field

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

@dataclass
class Book:
    title: str
    author: str
    is_borrowed: bool


@dataclass
class Member:
    name: str
    borrowed_books: list[Book] = field(default=[],compare=False)

class Library:
    membersList: list[Member]
    booksList: list[Book]
    borrowedBooksList: list[Book]

    def __init__(self,  membersList: list[Member], booksList: list[Book], borrowedList: list[Book]):
        self.membersList = membersList
        self.booksList = booksList
        self.borrowedBooksList = borrowedList


    def addMember(self, member: Member):
        self.membersList.append(member)


    def addBook(self, book: Book):
        self.booksList.append(book)


    def borrowBook(self, book: Book, member: Member):

        try:
            if len(member.borrowed_books) == 3:
                raise MemberLimitExceededException("Members can not borrow more than 3 books!")
            elif book not in self.booksList and book not in self.borrowedBooksList:
                raise BookNotFoundException("Book not found!")
            elif book not in self.booksList:
                raise BookAlreadyBorrowedException("Book already borrowed!")
            else:
                self.borrowedBooksList.append(book)
                indexOfBook = self.booksList.index(book)
                self.booksList.pop(indexOfBook)

                for i in range(len(self.membersList)):
                    if self.membersList[i].name == member.name:
                        self.membersList[i].borrowed_books.append(book)
                        break
        except (MemberLimitExceededException, BookNotFoundException, BookAlreadyBorrowedException) as e:
            print(e)


    def returnBook(self, member: Member, book: Book):
        self.booksList.append(book)
        indexOfBook = self.borrowedBooksList.index(book)
        self.borrowedBooksList.pop(indexOfBook)

        for i in range(len(self.membersList)):
            if self.membersList[i].name == member.name:
                memberBookIndex = self.membersList[i].borrowed_books.index(book)
                self.membersList[i].borrowed_books.pop(memberBookIndex)
                break


