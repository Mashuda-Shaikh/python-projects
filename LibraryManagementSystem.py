library = {
    "101": {"title": "Python Basics", "status": "available"},
    "102": {"title": "C++ Guide", "status": "available"},
    "103": {"title": "Data Structures", "status": "available"}
}

def display_books():
    print("\n--- Book List ---")
    for id, info in library.items():
        print(f"ID: {id}, Title: {info['title']}, Status: {info['status']}")

def issue_book(book_id):
    if library.get(book_id):
        if library[book_id]["status"] == "available":
            library[book_id]["status"] = "issued"
            print(f"Book '{library[book_id]['title']}' issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book(book_id):
    if library.get(book_id):
        library[book_id]["status"] = "available"
        print(f"Book '{library[book_id]['title']}' returned.")
    else:
        print("Book not found.")

while True:
    print("\n1. Display Books\n2. Issue Book\n3. Return Book\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        display_books()
    elif choice == "2":
        bid = input("Enter Book ID to issue: ")
        issue_book(bid)
    elif choice == "3":
        bid = input("Enter Book ID to return: ")
        return_book(bid)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
