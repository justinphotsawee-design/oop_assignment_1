import sys
import os

# Make Python see library_oop.py
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from library_oop import Book, Member, Library


def test_integration():
    print("=" * 60)
    print("OOP LIBRARY MANAGEMENT SYSTEM - FULL INTEGRATION TEST (COMMIT #5)")
    print("=" * 60)

    lib = Library()

    # TEST 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(Book(1, "Python Crash Course", "Eric Matthes", 3))
    lib.add_book(Book(2, "Clean Code", "Robert Martin", 2))
    lib.add_book(Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1))
    lib.add_book(Book(4, "Design Patterns", "Gang of Four", 2))

    # TEST 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(Member(101, "Alice Smith", "alice@email.com"))
    lib.add_member(Member(102, "Bob Jones", "bob@email.com"))
    lib.add_member(Member(103, "Carol White", "carol@email.com"))

    # TEST 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()

    # TEST 4: Successful Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow(101, 1)  
    lib.borrow(101, 2)
    lib.borrow(102, 1)

    # TEST 5: Member Books
    print("\n--- TEST 5: Display Member Books ---")
    lib.display_member_books(101)
    lib.display_member_books(102)
    lib.display_member_books(103)

    # TEST 6: After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib.display_available_books()

    # TEST 7: Borrow Last Copy
    print("\n--- TEST 7: Borrow Last Copy ---")
    lib.borrow(103, 3)  
    lib.display_available_books()

    # TEST 8: Borrow Unavailable Book
    print("\n--- TEST 8: Attempt Borrow Unavailable ---")
    lib.borrow(102, 3)

    # TEST 9: Member Limit
    print("\n--- TEST 9: Borrow Limit ---")
    lib.borrow(101, 4)
    lib.display_member_books(101)
    lib.borrow(101, 3)  

    # TEST 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    lib.return_book(101, 1)
    lib.return_book(102, 1)
    lib.display_member_books(101)
    lib.display_available_books()

    # TEST 11: Return Invalid
    print("\n--- TEST 11: Returning Invalid Book ---")
    lib.return_book(102, 2)

    # TEST 12: Return and Borrow Again
    print("\n--- TEST 12: Return + Reborrow ---")
    lib.return_book(103, 3)
    lib.borrow(102, 3)
    lib.display_member_books(102)

    # TEST 13: Non-existent Inputs
    print("\n--- TEST 13: Error Handling Cases ---")
    lib.borrow(999, 1)
    lib.borrow(101, 999)
    lib.return_book(999, 1)
    lib.display_member_books(999)

    # TEST 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Members and Their Books:")
    for member_id, m in lib.members.items():
        print(f"\n{m.name} ({m.id}):")
        if not m.borrowed_books:
            print("  (No books borrowed)")
        else:
            for book_id in m.borrowed_books:
                b = lib.books.get(book_id)
                if b:
                    print(f"  - {b.title}")

    print("\n=== Available Books at End ===")
    lib.display_available_books()

    print("\n" + "=" * 60)
    print("INTEGRATION TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_integration()
