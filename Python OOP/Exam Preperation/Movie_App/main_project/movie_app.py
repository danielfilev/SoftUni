from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        new_user = User(username, age)
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")

        if new_user not in self.users_collection:
            self.users_collection.append(new_user)
            return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):

        user = self.__find_user(username)
        if user not in self.users_collection:
            raise Exception("This user does not exist!")

        user_owns_movie = self.__owner_owns_movie(user, movie)

        if user in self.users_collection and not user_owns_movie:
            raise Exception(
                f"{user.username} is not the owner of the movie {movie.title}!")

        is_movie_uploaded = self.__is_movie_uploaded(user, movie)
        if not is_movie_uploaded:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):

        user = self.__find_user(username)
        self.__owner_owns_movie_exception(user, movie)
        self.__is_movie_uploaded_exception(user, movie)

        if "title" in kwargs.keys():
            movie.title = kwargs["title"]
        if "year" in kwargs.keys():
            movie.year = kwargs["year"]
        if "age_restriction" in kwargs.keys():
            movie.age_restriction = kwargs["age_restriction"]
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):

        user = self.__find_user(username)
        self.__owner_owns_movie_exception(user, movie)
        self.__is_movie_uploaded_exception(user, movie)

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):

        user = self.__find_user(username)
        self.__owner_owns_movie_but_likes_exception(user, movie)
        self.__user_already_liked_movie(user, movie)

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):

        user = self.__find_user(username)
        self.__user_has_not_liked_movie_but_tries_to_dislike(user, movie)

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."

        sorted_by_year = sorted(self.movies_collection,
                                key=lambda x: (x.year, -x.title), reverse=True)
        result = ""
        for movie in sorted_by_year:
            result += f"{movie.details()}\n"
        return result.strip()

    def __str__(self):

        result = ""
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            users_list_usernames = ", ".join(
                [user.username for user in self.users_collection])
            result += f"All users: {users_list_usernames}\n"
        if not self.movies_collection:
            result += "All movies: No movies.\n"
        else:
            movies_list_titles = ", ".join(
                [movie.title for movie in self.movies_collection])
            result += f"All movies: {movies_list_titles}\n"
        return result.strip()

    def __find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __owner_owns_movie(self, user, movie):
        if user != movie.owner:
            return False
        return True

    def __is_movie_uploaded(self, user, movie):
        if movie in self.movies_collection or movie in user.movies_owned:
            return False
        return True

    def __is_movie_uploaded_exception(self, user, movie):
        if movie not in self.movies_collection or movie not in user.movies_owned:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def __owner_owns_movie_exception(self, user, movie):
        if user != movie.owner:
            raise Exception(
                f"{user.username} is not the owner of the movie {movie.title}!")

    def __owner_owns_movie_but_likes_exception(self, user, movie):
        if user == movie.owner:
            raise Exception(
                f"{user.username} is the owner of the movie {movie.title}!")

    def __user_already_liked_movie(self, user, movie):
        if movie in user.movies_liked:
            raise Exception(
                f"{user.username} already liked the movie {movie.title}!")

    def __user_has_not_liked_movie_but_tries_to_dislike(self, user, movie):
        if movie not in user.movies_liked:
            raise Exception(
                f"{user.username} has not liked the movie {movie.title}!")
