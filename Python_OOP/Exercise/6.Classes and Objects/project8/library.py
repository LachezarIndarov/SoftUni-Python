from project8.user import User


class Library:
    def __init__(self):
        self.user_records = list()
        self.books_available = dict()
        self.rented_books = dict()

    def get_book(self, author, book_name, days_to_return, user: User):
        for renter_user in self.rented_books.keys():
            for bk, days in self.rented_books[renter_user].items():
                if bk == book_name:
                    return f'The book "{book_name}" is already rented and will be available in ' \
                           f'{self.rented_books[renter_user][book_name]} days!'
        for auth, books in self.books_available.items():
            for book in books:
                if author == auth and book_name == book:
                    if user.username not in self.rented_books.keys():
                        self.rented_books[user.username] = {}
                    self.rented_books[user.username][book_name] = days_to_return
                    self.books_available[author].remove(book_name)
                    user.books.append(book_name)
                    return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        del self.rented_books[user.username][book_name]
        if author in self.books_available.keys():
            self.books_available[author].append(book_name)
        else:
            self.books_available[author] = [book_name]

