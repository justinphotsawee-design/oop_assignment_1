
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
