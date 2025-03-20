# Movie Library Create a class MovieLibrary that manages a collection of movies.

class MovieLibrary:
    available_movies = ["Inception", "Titanic", "Interstellar", "The Dark Knight", "Avatar"]

    def __init__(self, member_name):
        self.member_name = member_name
        self.borrowed_movies = []

    def borrow_movie(self, movie):
        if movie in MovieLibrary.available_movies:
            MovieLibrary.available_movies.remove(movie)
            self.borrowed_movies.append(movie)
            print(f"Borrowed: {movie}")
        else:
            print(f"'{movie}' not available.")

    def return_movie(self, movie):
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"Returned: {movie}")
        else:
            print(f"You didn't borrow '{movie}'.")

    def view_borrowed_movies(self):
        print("Borrowed Movies:", ', '.join(self.borrowed_movies) if self.borrowed_movies else "None")


member = MovieLibrary("Alice")
member.borrow_movie("Inception")
member.view_borrowed_movies()
member.return_movie("Inception")

''' OUTPUT:

  Borrowed: Inception
Borrowed Movies: Inception
Returned: Inception '''
