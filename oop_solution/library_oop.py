
class Book:
    """Represents an individual book and tracks its circulation."""

    def __init__(self, book_id, title, author, total_copies):
        if total_copies < 0:
            raise ValueError("total_copies cannot be negative")

        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        """Attempt to borrow a copy of the book."""
        if self.available_copies <= 0:
            return False
        self.available_copies -= 1
        return True

    def return_back(self):
        """Return a copy if the shelf is not already full."""
        if self.available_copies >= self.total_copies:
            return False
        self.available_copies += 1
        return True

class Member:
    """Tracks a member's profile and which books they hold."""

    MAX_BORROWED = 3

    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book_id):
        """Register a borrowed book by id."""
        if len(self.borrowed_books) >= Member.MAX_BORROWED:
            return False
        if book_id in self.borrowed_books:
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self, book_id):
        """Remove a borrowed book when returned."""
        if book_id not in self.borrowed_books:
            return False
        self.borrowed_books.remove(book_id)
        return True


class Library:
    """Coordinates books and members for library operations."""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """Add or replace a book record."""
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully!")

    def add_member(self, member):
        """Register or replace a member entry."""
        self.members[member.id] = member
        print(f"Member '{member.name}' registered successfully!")

    def find_book(self, book_id):
        return self.books.get(book_id)

    def find_member(self, member_id):
        return self.members.get(member_id)

    def display_available_books(self):
        print("\n=== Available Books ===")
        available = False
        for book in self.books.values():
            if book.available_copies > 0:
                available = True
                print(
                    f"{book.title} by {book.author} - {book.available_copies} copies available"
                )
        if not available:
            print("No books currently available")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
            return

        for book_id in member.borrowed_books:
            book = self.find_book(book_id)
            if book:
                print(f"- {book.title} by {book.author}")

    def borrow(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return False

        book = self.find_book(book_id)
        if not book:
            print("Error: Book not found!")
            return False

        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False

        if len(member.borrowed_books) >= Member.MAX_BORROWED:
            print("Error: Member has reached borrowing limit!")
            return False

        if book_id in member.borrowed_books:
            print("Error: Member already borrowed this book!")
            return False

        # Process borrowing
        book.borrow()
        member.borrow_book(book_id)
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if not member.return_book(book_id):
            print("Error: This member hasn't borrowed this book!")
            return False

        book.return_back()
        print(f"{member.name} returned '{book.title}'")
        return True
