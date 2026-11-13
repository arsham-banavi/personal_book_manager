
from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Hello, please enter your name: ")

book_list = load_books()

if book_list is None:
    book_list = []

print(f"\nWelcome {name} to the Personal Book Manager!")

print(f"\nYou currently have {len(book_list)} books in your collection.")

admin_mode = input("\nDo you want to enter admin mode (yes/no)? ").lower()

if admin_mode == "yes":
    admin_password = input("Enter admin password: ")

    if admin_password == os.getenv("admin_pass"):
        print("Admin mode activated!")
    else:
        print("Wrong password!")

count = int(input("\nHow many books do you want to add? "))

for i in range(count):
    book = input("\nEnter a book name: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    book_list.append({
        "name": book,
        "priority": priority
    })

print(f"\nYour collection now has {len(book_list)} books!")

show_books(book_list)
save_books(book_list)
