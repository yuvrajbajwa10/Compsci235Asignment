from datetime import datetime

from compsci235flix_app.domainmodel.movie import Movie


class Review:
    def __init__(self, movie=Movie(), review_text="", rating=0, timestamp=None):
        if not isinstance(movie, Movie): movie = Movie()
        self._movie = movie
        if review_text != "" and review_text is not None:
            self._review_text = review_text.strip()
        if rating < 1 or rating > 10: rating = None
        self._rating = rating
        self._timestamp = timestamp

    def __repr__(self):
        return f"<Review {self._movie}, {self._rating}, {self._review_text}, {self._timestamp}>"

    def __eq__(self, other: Movie):
        return self._movie == other.movie and self._rating == other.rating and \
               self._review_text == other.review_text and self._timestamp == other.timestamp

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp
