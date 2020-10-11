import csv
from compsci235flix_app.domainmodel.movie import Movie
from compsci235flix_app.domainmodel.actor import Actor
from compsci235flix_app.domainmodel.genre import Genre
from compsci235flix_app.domainmodel.director import Director
from compsci235flix_app.domainmodel.user import User

reader_instance = None


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = set()
        self._dataset_of_actors = set()
        self._dataset_of_actorsNames = set()
        self._dataset_of_directors = set()
        self._dataset_of_genres = set()
        self._dataset_of_users = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                temp_movie = Movie(title, release_year)

                genres = row['Genre'].split(",")
                for genre in genres:
                    genre = Genre(genre.strip())
                    temp_movie.add_genre(genre)
                    if genre not in self._dataset_of_genres:
                        self._dataset_of_genres.add(genre)

                c = 1
                actors = row['Actors'].split(",")
                for actor in actors:
                    actor2 = actor.strip().lower()
                    if actor2 not in self._dataset_of_actorsNames:
                        self._dataset_of_actorsNames.add(actor2)
                        actor2 = Actor(actor2)
                        self._dataset_of_actors.add(actor2)
                    else:
                        for actor3 in self._dataset_of_actors:
                            if actor3.actor_full_name == actor2:
                                actor2 = actor3
                                break
                    temp_movie.add_actor(actor2)

                for actor in temp_movie.actors:
                    c = 1
                    for thisActor in temp_movie.actors[c:]:
                        if not actor.check_if_this_actor_worked_with(thisActor) and thisActor is not actor:
                            actor.add_actor_colleague(thisActor)
                        if not thisActor.check_if_this_actor_worked_with(actor) and thisActor is not actor:
                            thisActor.add_actor_colleague(actor)
                    c += 1

                director = Director(row['Director'])
                if director not in self._dataset_of_directors:
                    self._dataset_of_directors.add(director)
                temp_movie.director = director

                temp_movie.description = row['Description']
                temp_movie.runtime_minutes = int(row['Runtime (Minutes)'])
                temp_movie.rating = float(row['Rating'])
                temp_movie.votes = int(row['Votes'])
                revenue = row['Revenue (Millions)']
                if revenue.isnumeric():
                    temp_movie.revenue = float(revenue)
                else:
                    temp_movie.revenue = revenue

                metascore = row['Metascore']
                if metascore.isnumeric():
                    temp_movie.meta_score = int(metascore)
                else:
                    temp_movie.meta_score = metascore

                if temp_movie not in self._dataset_of_movies:
                    self._dataset_of_movies.add(temp_movie)

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres

    @property
    def dataset_of_users(self):
        return self._dataset_of_users

    def get_user(self, value):
        value = value.lower()
        for x in self._dataset_of_users:
            if x.username == value:
                return x
        return None

    def add_user(self, user: User):
        self._dataset_of_users.add(user)
