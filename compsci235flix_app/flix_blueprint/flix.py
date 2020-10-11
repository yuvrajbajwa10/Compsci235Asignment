from flask import Blueprint, render_template, session
from werkzeug.utils import redirect

from compsci235flix_app.flix_blueprint.ultilites import *

movie_bluePrint = Blueprint("movie_bp", __name__)


@movie_bluePrint.route('/', methods=['GET', 'POST'])
def home():
    instant_WTForm = searchBar()
    if instant_WTForm.validate_on_submit():
        movies = search(instant_WTForm.searchText.data)
        return render_template("listOfAllMovies.html", movies=movies, pageTitle="Search Results",
                               headerName="The {0} Search Results".format(len(movies)),
                               genres=sorted(reader_instance.dataset_of_genres))

    return render_template("Home.html", form=instant_WTForm, genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route('/the1000')
def the1000():
    return render_template('listOfAllMovies.html', movies=sorted(reader_instance.dataset_of_movies),
                           pageTitle="1000 Movies", headerName="The 1000 Movies",
                           genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route('/listMovie/<year>/<title>',methods=['GET', 'POST'])
def listMovie(year=0, title=""):
    form = reviewForm()
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


@movie_bluePrint.route("/listdirector/<director>")
def listdirector(director):
    return render_template('listOfAllMovies.html', movies=searchDirectorMovies(director),
                           pageTitle=director, headerName="The " + director + " Movies",
                           genres=sorted(reader_instance.dataset_of_genres))


@movie_bluePrint.route("/favicon.ico")
def returnFavicon():
    return render_template('favicon.html')


@movie_bluePrint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    username_not_unique = None
    if form.validate_on_submit():
        try:
            add_user(form.username.data, form.password.data, reader_instance)
            return redirect('/login')
        except NameNotUniqueException:
            username_not_unique = 'Your username is already taken - please supply another'

    return render_template('register.html', form=form, username_error_message=username_not_unique,
                           genres=sorted(reader_instance.dataset_of_genres), password_error_message=None,
                           handler_url='/register',
                           Title="Register")


@movie_bluePrint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username_not_recognised = None
    password_does_not_match_username = None

    if form.validate_on_submit():
        try:
            user = get_user(form.username.data, reader_instance)
            authenticate_user(user['username'], form.password.data, reader_instance)
            session.clear()
            session['username'] = user['username']
            return redirect('/')

        except UnknownUserException:
            username_not_recognised = 'Username not recognised - please supply another'
        except AuthenticationException:
            password_does_not_match_username = 'Password does not match supplied username - please check and try again'

    return render_template(
        'register.html',
        Title='Login',
        username_error_message=username_not_recognised,
        password_error_message=password_does_not_match_username,
        handler_url='/login',
        form=form,
        genres=sorted(reader_instance.dataset_of_genres)
    )


@movie_bluePrint.route('/logout')
def logout():
    session.clear()
    return redirect('/')
