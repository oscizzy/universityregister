class User:
    # OOP - Encapsulation:
    # User stores its data (username, password, user_id) and exposes
    # accessor methods (get_user_id, get_username) so internal state is
    # not manipulated directly by external code.
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id

    def login(self, input_username, input_password):
        # OOP - Polymorphism:
        # `login` is defined here on the base `User` class and is used
        # polymorphically for both `Admin` and `Student` instances.
        return self.username == input_username and self.password == input_password

    def logout(self):
        print(f"Logging out... Goodbye, {self.username}!")

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username