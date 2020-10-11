from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, HiddenField
from wtforms.fields.html5 import SearchField
from wtforms.validators import DataRequired, Length, ValidationError
from password_validator import PasswordValidator

from compsci235flix_app.datafilereaders.movie_file_csv_reader import reader_instance, MovieFileCSVReader
from compsci235flix_app.domainmodel.genre import Genre
from compsci235flix_app.domainmodel.movie import Movie
from compsci235flix_app.domainmodel.user import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def add_review(movieId: str, review_text: str, username: str, repo: MovieFileCSVReader):
    pass


def reviewForm():
    review = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short')])
    movieid = HiddenField("movieId")
    submit = SubmitField('Submit')


def add_user(username: str, password: str, repo: MovieFileCSVReader):
    user = repo.get_user(username)
    if user is not None:
        raise NameNotUniqueException

    password_hash = generate_password_hash(password)
    user = User(username, password_hash)
    repo.add_user(user)


def get_user(username: str, repo: MovieFileCSVReader):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    return user_to_dict(user)


def authenticate_user(username: str, password: str, repo: MovieFileCSVReader):
    authenticated = False

    user = repo.get_user(username)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException


def user_to_dict(user: User):
    user_dict = {
        'username': user.username,
        'password': user.password
    }
    return user_dict


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
    listofResults.sort()
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
    for director in reader_instance.dataset_of_directors:
        if director.director_full_name == directorToFind:
            directorToFind = director
            break

    listOfResults = []
    for movie in reader_instance.dataset_of_movies:
        if directorToFind == movie.director:
            listOfResults.append(movie)

    return listOfResults


class searchBar(FlaskForm):
    searchText = SearchField("Search")
    submit = SubmitField("Search For Movies")


def getMovies(year, title):
    for movie in reader_instance.dataset_of_movies:
        if movie.title == title and movie.release_year == year:
            return movie
    return Movie()


class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter,\
            a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    username = StringField('Username', [
        DataRequired(message='Your username is required'),
        Length(min=3, message='Your username is too short')])
    password = PasswordField('Password', [
        DataRequired(message='Your password is required'),
        PasswordValid()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired()])
    submit = SubmitField('Login')
