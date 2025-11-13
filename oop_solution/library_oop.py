
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
