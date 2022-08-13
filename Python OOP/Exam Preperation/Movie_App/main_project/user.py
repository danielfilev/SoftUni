class User:

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"
        if not self.movies_liked:
            result += "No movies liked.\n"
        else:
            result += "Liked movies:\n"
            for movie in self.movies_liked:
                result += f"{movie.details()}\n"
        if not self.movies_owned:
            result += "No movies owned.\n"
        else:
            result += "Owned movied:\n"
            for movie in self.movies_owned:
                result += f"{movie.details()}\n"
        return result.strip()
