class Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name

    @property
    def genre_name(self):
        return self._genre_name

    @genre_name.setter
    def genre_name(self, value):
        if value == "": value = "None"
        self._genre_name = value

    def __repr__(self):
        return f"<Genre {self.genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre): return False
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)