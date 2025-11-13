import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from library_oop import Book , Member , Library

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
    print("Try Borrow 4 (should fail):", m.borrow_book(4))  

    print("\n--- TEST 3: Returning Books ---")
    print("Return 2:", m.return_book(2))
    print("Return 4 (not borrowed):", m.return_book(4))

    print("\nRemaining borrowed books:", m.borrowed_books)

    print("=" * 60)
    print("MEMBER TEST COMPLETE")
    print("=" * 60)

def test_library_class():
    print("=" * 60)
    print("LIBRARY CLASS TEST - COMMIT #4")
    print("=" * 60)

    lib = Library()

    # Add books
    lib.add_book(Book(1, "Python Crash Course", "Eric Matthes", 3))
    lib.add_book(Book(2, "Clean Code", "Robert Martin", 2))
    lib.add_book(Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1))

    # Add members
    lib.add_member(Member(101, "Alice", "alice@mail.com"))
    lib.add_member(Member(102, "Bob", "bob@mail.com"))

    print("\n--- TEST: Display Books ---")
    lib.display_available_books()

    print("\n--- TEST: Borrow Books ---")
    lib.borrow(101, 1)
    lib.borrow(101, 2)
    lib.borrow(102, 1)
    lib.borrow(102, 3)
    lib.borrow(101, 3)  # Should fail (no copies)

    print("\n--- TEST: Display Member Books ---")
    lib.display_member_books(101)
    lib.display_member_books(102)

    print("\n--- TEST: Return Books ---")
    lib.return_book(101, 1)
    lib.return_book(102, 1)
    lib.return_book(102, 99)  # invalid

    print("\n--- TEST: Error Handling ---")
    lib.borrow(999, 1)
    lib.borrow(101, 999)
    lib.return_book(999, 1)

    print("=" * 60)
    print("LIBRARY TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
    test_member_class()
    test_library_class()
