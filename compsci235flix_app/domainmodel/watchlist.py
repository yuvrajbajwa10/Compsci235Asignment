from domainmodel.movie import Movie


class WatchList:

    def __init__(self):
        self._watchlist = []

    def add_movie(self, movie: Movie):
        if movie not in self._watchlist:
            self._watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        self._watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if index >= len(self._watchlist) or index <= -len(self._watchlist): return None
        return self._watchlist[index]

    def size(self):
        return len(self._watchlist)

    def first_movie_in_watchlist(self):
        if len(self._watchlist) < 1: return None
        return self._watchlist[0]

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        nextmovie = self._watchlist[self._n]
        self._n = self._next + 1
        return nextmovie
