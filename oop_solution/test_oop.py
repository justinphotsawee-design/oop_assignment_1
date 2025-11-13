import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from library_oop import Book


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
    print("Borrow when no copies left:", b.borrow())   # Should be False

    # Return Book
    print("\n--- TEST 3: Returning Books ---")
    print("Return 1:", b.return_back())
    print("Return 2:", b.return_back())
    print("Return 3:", b.return_back())
    print("Return when full:", b.return_back())        # Should be False

    print("\nFinal available copies:", b.available_copies)

    print("\n" + "=" * 60)
    print("BOOK CLASS TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
