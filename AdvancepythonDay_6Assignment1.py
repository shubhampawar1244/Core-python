# Write a Python program to model a Library system.



class Library:
    total_books = 0  # Class attribute to track total books
    all_books = []  # Class attribute to store all available books

    def __init__(self, name):
        self.name = name  # Member name
        self.borrowed_books = []  # List to track borrowed books

    def borrow_book(self, book):
        """Method to borrow a book from the library."""
        if book in Library.all_books:
            self.borrowed_books.append(book)  # Add book to member's list
            Library.all_books.remove(book)  # Remove book from library
            Library.total_books -= 1  # Decrease total books
            print(f"{self.name} borrowed '{book}'.")
        else:
            print("Book not available.")

    def return_book(self, book):
        """Method to return a book to the library."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Remove from member's list
            Library.all_books.append(book)  # Add book back to library
            Library.total_books += 1  # Increase total books
            print(f"{self.name} returned '{book}'.")
        else:
            print("This book was not borrowed from the library.")

    @classmethod
    def view_library_books(cls):
        """Class method to view all available books."""
        print(f"Total books in library: {cls.total_books}")
        print("Available books:", ", ".join(cls.all_books) if cls.all_books else "No books available.")


Library.all_books = ["Python Basics", "Data Science", "Machine Learning"]
Library.total_books = len(Library.all_books)

member1 = Library("Alice")
Library.view_library_books()

member1.borrow_book("Python Basics")
Library.view_library_books()

member1.return_book("Python Basics")
Library.view_library_books()


''' OUTPUT:

  Total books in library: 3
Available books: Python Basics, Data Science, Machine Learning
Alice borrowed 'Python Basics'.
Total books in library: 2
Available books: Data Science, Machine Learning
Alice returned 'Python Basics'.
Total books in library: 3
Available books: Data Science, Machine Learning, Python Basics '''
