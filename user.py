class User:
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id

    def login(self, input_username, input_password):
        return self.username == input_username and self.password == input_password

    def logout(self):
        print(f"Logging out... Goodbye, {self.username}!")

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username