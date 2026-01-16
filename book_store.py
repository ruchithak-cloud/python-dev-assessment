class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2025 - self.publication_year

    def get_summary(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"



books = [
    Book("1984", "George Orwell", "9780451524935", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960)
]

for book in books:
    print(f"{book.get_summary()} (Age: {book.get_age()} years)")
