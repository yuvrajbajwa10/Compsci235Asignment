from datetime import date
from compsci235flix_app.domainmodel.actor import Actor
from compsci235flix_app.domainmodel.director import Director
from compsci235flix_app.domainmodel.genre import Genre
from compsci235flix_app.domainmodel.movie import Movie
from compsci235flix_app.domainmodel.review import Review
from compsci235flix_app.domainmodel.user import User
from compsci235flix_app.domainmodel.watchlist import WatchList

import pytest


@pytest.fixture()
def user():
    return User("Yuvraj123", "Ybaj161")


@pytest.fixture()
def actor():
    return Actor('Leo')


@pytest.fixture()
def director():
    return Director("tutu")


@pytest.fixture()
def genre():
    return Genre('PooPoo')


@pytest.fixture()
def movie():
    return Movie("Your Mom", 2020)


@pytest.fixture()
def review(movie):
    return Review(movie, "Its werid question to ask; You weirdo", 10, date.today())


@pytest.fixture()
def watchlist():
    return WatchList()


def test_user_construction(user):
    assert user.username == 'yuvraj123'
    assert user.password == 'Ybaj161'
    assert repr(user) == '<User yuvraj123>'


def test_review(review):
    assert review.movie.title == "Your Mom"
    assert review.movie.release_year == 2020
    assert review.review_text == "Its werid question to ask; You weirdo"
    assert review.rating == 10
    assert review.timestamp == date.today()


def test_movie(movie):
    assert movie.title == 'Your Mom'
    assert movie.release_year == 2020


    
