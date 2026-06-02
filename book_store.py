class Book:
    def __init__(self, title: str, author: str, isbn: str, publication_year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self) -> int:
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


book1 = Book("Na Drini cuprija", "Ivo Andric", "9788617150530", 1945)
book2 = Book("Seobe", "Milos Crnjanski", "9788652109630", 1929)
book3 = Book("Hazarski recnik", "Milorad Pavic", "9788652119936", 1984)

books = [book1, book2, book3]

for book in books:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Age: {book.get_age()} years")
        print(f"Summary: {book.get_summary()}")
        print("-" * 30)
print("For books example AI is used. :)")