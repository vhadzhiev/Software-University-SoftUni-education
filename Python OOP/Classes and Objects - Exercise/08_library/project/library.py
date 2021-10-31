class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, new_user):
        for user in self.user_records:
            if user.user_id == new_user.user_id:
                return f"User with id = {new_user.user_id} already registered in the library!"

        self.user_records.append(new_user)
        self.rented_books[new_user.username] = {}

    def remove_user(self, new_user):
        if new_user in self.user_records:
            self.user_records.remove(new_user)
        else:
            return 'We could not find such user to remove!'

    def change_username(self, user_id, new_username):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"

                rented_books = self.rented_books.pop(user.username)
                user.username = new_username
                self.rented_books[user.username] = rented_books
                return f'Username successfully changed to: {new_username} for userid: {user_id}'

        return f'There is no user with id = {user_id}!'
