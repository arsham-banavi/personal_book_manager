import json
def show_books(books):
    for book in books:
            print(f"{book["name"]} - priority: {book["priority"]}")

def save_books(books):
      with open("books.json", "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=2)

def load_books():
      try:
        with open("books.json", "r", encoding="utf-8") as file:
                return json.load(file)
      except FileNotFoundError:
            return []