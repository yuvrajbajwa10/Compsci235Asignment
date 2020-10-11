import os
import pytest

from compsci235flix_app import main
from compsci235flix_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


@pytest.fixture
def in_memory_repo():
    repo = MovieFileCSVReader('compsci235flix_app/datafilereaders/movie_file_csv_reader.py')
    return repo


@pytest.fixture
def client():
    my_app = main({
        'TESTING': True,  # Set to True during testing.
        'TEST_DATA_PATH': 'compsci235flix_app/datafilereaders/movie_file_csv_reader.py',
        # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False  # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()


class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='thorke', password='cLQ^C#oFXloS'):
        return self._client.post(
            'authentication/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)
