import json


class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their books."""

    def __init__(self):
        """Initialize a new book collection with an empty list andset up file storage."""
        self.book_list = []
        self.storage_file = "book_collection.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.If the file doesn't exist or its corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Save the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection with user-provided details."""
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        book_genre = input("Enter the genre of the book: ")
        book_publication_year = input("Enter the publication year of the book: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )
        new_book = {
            "title": book_title,
            "author": book_author,
            "genre": book_genre,
            "publication_year": book_publication_year,
            "read": is_book_read,
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection based on its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
            # Exit the function after removing the book
        print("Book not found in the collection.\n")

    def find_book(self):
        """Search for a book in the collection by its title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "unread"
                print(
                    f"{index}. Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Publication Year: {book['publication_year']}, Status: {reading_status}"
                )
        else:
            print("No matching books found.\n")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to update: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing values.")
                book["title"] = input(f"Enter new title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"Enter new author ({book['author']}): ") or book["author"]
                )
                book["genre"] = input(f"Enter new genre ({book['genre']}): ") or book["genre"]
                book["publication_year"] = input(f"Enter new publication year ({book['publication_year']}): ") or book["publication_year"]
                book["read"] = (
                    input(f"Have you read this book? (yes/no): ").strip().lower() == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found in the collection.\n")

    def show_all_books(self):
        """Display all boooks in the collection with thier details."""
        if not self.book_list:
            print("No books in the collection.\n")
            return
        
        print("All books in the collection: ")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "unread"
            print(
                f"{index}. Title: {book['title']} by Author: {book['author']}, Genre: {book['genre']} - Publication Year: {book['publication_year']} - Status: {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about yuor reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_percentage = (
            (completed_books / total_books) * 100 if total_books > 0 else 0
        )
        print(f"Total books in the collection: {total_books}")
        print(f"Reading progress: {completion_percentage: .2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("\n📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Find a book")
            print("4. Update book details")
            print("5. Show all books")
            print("6. Show reading progress")
            print("7. Exit")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                # Save the book collection to file before exiting
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


 # Handle invalid choices


if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.start_application()
