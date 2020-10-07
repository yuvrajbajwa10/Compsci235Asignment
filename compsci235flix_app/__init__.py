from flask import Flask, Blueprint, render_template
import compsci235flix_app.datafilereaders.movie_file_csv_reader as repo
from compsci235flix_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


def main():
    app = Flask(__name__)
    filename = 'compsci235flix_app/datafiles/Data1000Movies.csv'
    repo.reader_instance = repo.MovieFileCSVReader(filename)
    repo.reader_instance.read_csv_file()

    with app.app_context():
        from .flix_blueprint import flix
        app.register_blueprint(flix.movie_bluePrint)
    return app
