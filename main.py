from books import show_books

username = input("Enter your username: ")
print(f"Welcome {username}")

books = []
book_number = int(input("Enter number of books: "))
for _ in range(book_number):
    book = input("Enter book name: ")
    books.append(book)

print("------")
print(f"{username}'s books: ")
if books == []:
    print("no books")
else:
    show_books(books)