from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from compsci235flix_app.datafilereaders.movie_file_csv_reader import reader_instance
from compsci235flix_app.domainmodel.actor import Actor
from compsci235flix_app.domainmodel.director import Director
from compsci235flix_app.domainmodel.genre import Genre
from compsci235flix_app.domainmodel.movie import Movie

movie_bluePrint = Blueprint("movie_bp", __name__)


def search(searchTerms):
    searchTerms = searchTerms.lower()
    listOfActors = []
    listOfGenres = []
    listofResults = []
    listOfDirector = []

    for director in reader_instance.dataset_of_directors:
        if searchTerms in director.director_full_name.lower():
            listOfDirector.append(director)
    for actor in reader_instance.dataset_of_actors:
        if searchTerms in actor.actor_full_name.lower():
            listOfActors.append(actor)
    for genre in reader_instance.dataset_of_genres:
        if searchTerms in genre.genre_name.lower():
            listOfGenres.append(genre)

    for movie in reader_instance.dataset_of_movies:
        if searchTerms in movie.title.lower() or \
                searchTerms == str(movie.release_year) or \
                searchTerms in movie.description.lower():
            listofResults.append(movie)
            continue
        for actor in listOfActors:
            if actor in movie.actors:
                listofResults.append(movie)
                break

        if movie in listofResults:
            continue

        for genre in listOfGenres:
            if genre in movie.genres:
                listofResults.append(movie)
                break

        if movie in listofResults:
            continue

        for director in listOfDirector:
            if director is movie.director:
                listofResults.append(movie)
                break

    return listofResults


def searchGenreMovies(genreToFind):
    genreToFind = Genre(genreToFind)
    if genreToFind not in reader_instance.dataset_of_genres:
        return []

    listOfResults = []
    for movie in reader_instance.dataset_of_movies:
        if genreToFind in movie.genres:
            listOfResults.append(movie)
    return listOfResults


def searchActorMovies(actorToFind):
    listOfResults = []
    for movie in reader_instance.dataset_of_movies:
        if actorToFind in movie.actors:
            listOfResults.append(movie)
    return listOfResults


def searchDirectorMovies(directorToFind):
    directorToFind = Director(directorToFind)
    if directorToFind not in reader_instance.dataset_of_directors:
        return []

    listOfResults = []
    for movie in reader_instance.dataset_of_movies:
        if directorToFind in movie.actors:
            listOfResults.append(movie)
    return listOfResults


class searchBar(FlaskForm):
    searchText = StringField("Search")
    submit = SubmitField("Find")


def getMovies(year, title):
    for movie in reader_instance.dataset_of_movies:
        if movie.title == title and movie.release_year == year:
            return movie
    return Movie()


@movie_bluePrint.route('/', methods=['GET', 'POST'])
def home():
    instant_WTForm = searchBar()
    if instant_WTForm.validate_on_submit():
        movies = search(instant_WTForm.searchText.data)
        return render_template("listOfAllMovies.html", movies=movies, pageTitle="Search Results",
                               headerName="The {0} Search Results".format(len(movies)),
                               )

    return render_template("Home.html", form=instant_WTForm, genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route('/the1000')
def the1000():
    return render_template('listOfAllMovies.html', movies=sorted(reader_instance.dataset_of_movies),
                           pageTitle="1000 Movies", headerName="The 1000 Movies",
                           genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route('/listMovie/<year>/<title>')
def listMovie(year=0, title=""):
    movie = getMovies(int(year), title);
    return render_template("DetailedMovieDetails.html", movie=movie, genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route("/listActor/<actorName>")
def listActor(actorName=""):
    for aActor in reader_instance.dataset_of_actors:
        if actorName == aActor.actor_full_name:
            actor = aActor
            break

    return render_template("actorDetails.html", actor=actor, movies=searchActorMovies(actor),
                           genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route("/listGenre/<genreName>")
def listGenre(genreName):
    return render_template('listOfAllMovies.html', movies=searchGenreMovies(genreName),
                           pageTitle=genreName, headerName="The " + genreName + " Movies",
                           genres=sorted(reader_instance.dataset_of_genres))
