def user_authentication(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}")
        print(f"It returned: {function(*args, **kwargs)}")

    return wrapper


class User:
    def __init__(self, name: str):
        self.name = name
        self.is_logged_in = False

    @user_authentication
    def create_post(self):
        if self.is_logged_in:
            print(f"{self.name} creating blog post...")


user = User(name="Eugene")
user.is_logged_in = True
user.create_post()

