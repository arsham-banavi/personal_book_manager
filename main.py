from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

username = input("Enter your username: ")
print(f"Welcome {username}")

admin_mode = input("Enter admin mode? (yes/no): ")
if admin_mode == "yes":
    admin_pass = input("Enter admin password: ")
    if admin_pass == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")


books = load_books()
book_number = int(input("Enter number of books: "))
for _ in range(book_number):
    book_name = input("Enter book name: ")
    book_priority = input("Enter book priority (low / medium / high): ").lower()
    book = {
        "name": book_name,
        "priority": book_priority
    }
    books.append(book)

print("------")
print(f"{username}'s books: ")
if books == []:
    print("no books")
else:
    show_books(books)

save_books(books)