# 5. LIBRARY MANAGEMENT SYSTEM
# --------------------------------------------------
# Concepts: Lists, Dictionaries, Loops
# Description:
# - Maintain a list of books.
# - Features: Add new books, issue books, return books, search by title/author.
# - Track available and issued books.

# --------------------------------------------------
# LIBRARY MANAGEMENT SYSTEM
# --------------------------------------------------
# Concepts Used: Lists, Dictionaries, Loops, Functions
# Features:
# - Add new books
# - Issue books
# - Return books
# - Search by title or author
# - Track available and issued books
# --------------------------------------------------

library_data = {
    "books": [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "Available"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "Available"},
        {"id": 3, "title": "1984", "author": "George Orwell", "status": "Issued"},
        {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "status": "Available"},
        {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "status": "Issued"},
        {"id": 6, "title": "The Alchemist", "author": "Paulo Coelho", "status": "Available"},
        {"id": 7, "title": "The Hobbit", "author": "J.R.R. Tolkien", "status": "Available"},
        {"id": 8, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "status": "Issued"},
        {"id": 9, "title": "The Da Vinci Code", "author": "Dan Brown", "status": "Available"},
        {"id": 10, "title": "The Power of Habit", "author": "Charles Duhigg", "status": "Available"}
    ],
    "issued_books": [
        {"id": 3, "title": "1984", "issued_to": "Rahul Sharma", "issue_date": "2025-10-10"},
        {"id": 5, "title": "The Catcher in the Rye", "issued_to": "Ananya Patel", "issue_date": "2025-10-12"},
        {"id": 8, "title": "Harry Potter and the Sorcerer's Stone", "issued_to": "Aman Verma", "issue_date": "2025-10-15"}
    ]
}

def display_books():
    print("Available Books:")
    for book in library_data["books"]:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")


def add_book():
    title = input("Enter book title: ").title()
    author = input("Enter author name: ").title()
    new_id = len(library_data["books"]) + 1
    library_data["books"].append({"id": new_id, "title": title, "author": author, "status": "Available"})
    print(f" '{title}' by {author} has been added to the library.")


def issue_book():
    book_id = int(input("Enter the book ID to issue: "))
    for book in library_data["books"]:
        if book["id"] == book_id:
            if book["status"] == "Available":
                name = input("Enter the name of the person issuing the book: ").title()
                date = input("Enter issue date (YYYY-MM-DD): ")
                book["status"] = "Issued"
                library_data["issued_books"].append(
                    {"id": book_id, "title": book["title"], "issued_to": name, "issue_date": date}
                )
                print(f"{book['title']}' has been issued to {name}.")
                return
            else:
                print(" This book is already issued.")
                return
    print(" Book ID not found.")


def return_book():
    book_id = int(input("Enter the book ID to return: "))
    for book in library_data["books"]:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                library_data["issued_books"] = [b for b in library_data["issued_books"] if b["id"] != book_id]
                print(f"{book['title']} has been returned successfully.")
                return
            else:
                print("This book is not issued currently.")
                return
    print("Book ID not found.")


def search_book():
    keyword = input("Enter title or author to search: ").lower()
    results = [book for book in library_data["books"]
               if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if results:
        print(" Search Results:")
        for book in results:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
    else:
        print("No books found matching your search.")




while True:
    print("\n========== LIBRARY MENU ==========")
    print("1. Display All Books")
    print("2. Add New Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. View Issued Books")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        display_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print(" Issued Books:")
        for issued in library_data["issued_books"]:
            print(f"ID: {issued['id']}, Title: {issued['title']}, Issued To: {issued['issued_to']}, Date: {issued['issue_date']}")
    elif choice == "7":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


