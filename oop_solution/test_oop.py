import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from library_oop import Book , Member


def test_book_class():
    print("=" * 60)
    print("BOOK CLASS TEST - COMMIT #2")
    print("=" * 60)

    # Create Book
    print("\n--- TEST 1: Creating Book ---")
    b = Book(1, "Python Crash Course", "Eric Matthes", 3)
    print(f"Created book: {b.title} by {b.author}")
    print(f"Total copies: {b.total_copies}")
    print(f"Available copies: {b.available_copies}")

    # Borrow Book
    print("\n--- TEST 2: Borrowing Books ---")
    print("Borrow 1:", b.borrow())
    print("Borrow 2:", b.borrow())
    print("Borrow 3:", b.borrow())
    print("Borrow when no copies left:", b.borrow()) 

    # Return Book
    print("\n--- TEST 3: Returning Books ---")
    print("Return 1:", b.return_back())
    print("Return 2:", b.return_back())
    print("Return 3:", b.return_back())
    print("Return when full:", b.return_back())      

    print("\nFinal available copies:", b.available_copies)

    print("\n" + "=" * 60)
    print("BOOK CLASS TEST COMPLETE")
    print("=" * 60)

def test_member_class():
    print("=" * 60)
    print("MEMBER CLASS TEST - COMMIT #3")
    print("=" * 60)

    m = Member(101, "Alice", "alice@email.com")

    print("\n--- TEST 1: Member Info ---")
    print(m.id, m.name, m.email)

    print("\n--- TEST 2: Borrow Books ---")
    print("Borrow 1:", m.borrow_book(1))
    print("Borrow 2:", m.borrow_book(2))
    print("Borrow 3:", m.borrow_book(3))
    print("Try Borrow 4 (should fail):", m.borrow_book(4))  # cannot borrow more than 3

    print("\n--- TEST 3: Returning Books ---")
    print("Return 2:", m.return_book(2))
    print("Return 4 (not borrowed):", m.return_book(4))

    print("\nRemaining borrowed books:", m.borrowed_books)

    print("=" * 60)
    print("MEMBER TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
    test_member_class()
