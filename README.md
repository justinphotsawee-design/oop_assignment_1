# Library Management System  
### Procedural Version → OOP Version (Full Assignment)

This project is part of an Object-Oriented Programming assignment.  
The goal is to transform an existing **procedural-style library system** into a clean, maintainable **Object-Oriented implementation** using Python.

The project includes:

- Original procedural version  
- Full OOP version  
- Tests for each phase (commit)  
- Final integration test that mirrors procedural behavior  

---

## Project Structure

```
library-management-oop/
│
├── README.md  # This file
│
├── procedural_version/
│   ├── library_procedural.py      # Original procedural code
│   └── test_procedural.py        # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py    # Student's OOP implementation (to create)
│   └── test_oop.py      # Tests for OOP version (to create)


---

Procedural Version (Given)

The procedural version uses:

- Global lists (`books`, `members`, `borrowed_books`)
- Many standalone functions
- Manual checking for borrow/return rules
- No object encapsulation

While functional, it becomes difficult to maintain as the program grows.

---

Object-Oriented Version (Student Implementation)

The OOP version converts the procedural system into three clean, modular classes.

---

1. Book Class

Attributes
- `id`
- `title`
- `author`
- `total_copies`
- `available_copies`

Methods
- `borrow()`
- `return_back()`

Encapsulates book information and borrowing/return logic.

---

2. Member Class**

Attributes
- `id`
- `name`
- `email`
- `borrowed_books` (list of book IDs)

Methods
- `can_borrow()`
- `borrow_book(book_id)`
- `return_book(book_id)`

Manages borrowing rules (max 3 books per member).

---

3. Library Class

Responsibilities
- Store and manage all `Book` and `Member` objects
- Borrow and return operations
- Prevent borrowing unavailable books
- Prevent borrowing more than 3 books
- Validate member and book existence
- Display available books
- Display member status

This class replaces all procedural logic and becomes the “controller” of the system.

---

Testing: Procedural vs OOP

Procedural Test  
`test_procedural.py` contains 14 tests covering:

- Adding books/members  
- Borrowing  
- Returning  
- Borrow limits  
- Last-copy scenarios  
- Invalid cases  
- Final library status  

OOP Final Test  
`test_oop.py` includes the **same 14 scenarios**, reimplemented using OOP objects:

- Book objects  
- Member objects  
- Library controller class  

This confirms functional equivalence between procedural and OOP designs.

---

Commit History (Required by Assignment)

| Commit | Description |
|--------|-------------|
|   1    | Add procedural version + test |
|   2    | Add Book class + test |
|   3    | Add Member class + test |
|   4    | Add Library class + test |
|   5    | Final full integration test (all classes working together) |

This commit sequence demonstrates proper step-by-step OOP refactoring.

---

How to Run

Run Procedural Version
```
cd procedural_version
python3 test_procedural.py
```

Run OOP Version
```
cd oop_solution
python3 test_oop.py
```

---

Summary

This project demonstrates how to:

- Refactor procedural code into clean OOP structures  
- Apply encapsulation, modularity, and responsibility separation  
- Build a system with real-world logic (borrowing rules, limits, etc.)  
- Test functionality thoroughly using realistic use cases  
- Track development properly through meaningful commits  

The final OOP design is scalable and ready for future extensions (due dates, categories, GUI, etc.)

---


