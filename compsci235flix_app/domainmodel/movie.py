from compsci235flix_app.domainmodel.actor import Actor
from compsci235flix_app.domainmodel.director import Director
from compsci235flix_app.domainmodel.genre import Genre


class Movie:
    def __init__(self, title: str = None, year: int = None):
        if title != "" and title is not None:
            self._title = title.strip()
        if year is not None and year < 1900: year = None
        self._release_year = year

        self._description = None
        self._director = None
        self._actors = []
        self._genres = []
        self._runtime_minutes = 0
        self._votes = 0
        self._rating = 0
        self._meta_score = 0
        self._revenue = 0

    @property
    def title(self):
        return self._title

    @property
    def release_year(self):
        return self._release_year

    @property
    def description(self):
        return self._description

    @property
    def director(self):
        return self._director

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @property
    def actors(self):
        return self._actors

    @property
    def genres(self):
        return self._genres

    @property
    def votes(self):
        return self._votes

    @property
    def rating(self):
        return self._rating

    @property
    def meta_score(self):
        return self._meta_score

    @property
    def revenue(self):
        return self._revenue

    @description.setter
    def description(self, value):
        if type(value) != str: value = None
        if value == "": value = None
        self._description = value.strip()

    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value

    @runtime_minutes.setter
    def runtime_minutes(self, value):
        if value < 0: raise ValueError
        self._runtime_minutes = value

    @votes.setter
    def votes(self, value):
        if value < 0: raise ValueError
        self._votes = value

    @rating.setter
    def rating(self, value):
        if value < 0: raise ValueError
        self._rating = value

    @meta_score.setter
    def meta_score(self, value):
        self._meta_score = value

    @revenue.setter
    def revenue(self, value):
        self._revenue = value

    def add_actor(self, actor):
        if isinstance(actor, Actor): self._actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.actors: self._actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre): self._genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.genres: self._genres.remove(genre)

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.title == other._title and self.release_year == other.release_year

    def __lt__(self, other):
        if self._title < other.title: return True
        if self._title == other.title:
            return self._release_year < other.release_year
        return False

    def __hash__(self):
        return hash(str(self.title) + str(self.release_year))
