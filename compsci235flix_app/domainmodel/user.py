from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, username:str, password:str):
        self._username = username.strip().lower()
        self._password = password
        self._watched_movies = []
        self._reviews = []
        self._tswmm = 0 # TSWMM = TimeSpentWatchingMoviesMinutes

    @property
    def username(self):
        return self._username

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews (self):
        return self._reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self._tswmm

    def __repr__(self):
        return f"<User {self.username}>"

    def __eq__(self, other):
        if isinstance(other,User):
            return self.username == other.username
        return  False

    def __lt__(self, other):
       return self.username < other.username

    def __hash__(self):
        return hash(self.username + self._password)

    def watch_movie (self, movie):
        if isinstance(movie, Movie):
            self._watched_movies.append(movie)
            self._tswmm += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review):
            self._reviews.append(review)
