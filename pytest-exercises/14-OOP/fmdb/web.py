from flask import Flask, render_template, redirect, request
import disk

app = Flask(__name__)

fmdb = disk.load_fmdb()


@app.route('/')
def root():
    return render_template('root.html')


@app.route('/choose_director')
def choose_director():
    return render_template('choose_director.html')


@app.route('/choose_cast')
def choose_cast():
    return render_template('choose_cast.html')


@app.route('/director_movies')
def director_movies():
    director = request.args.get('director')
    if director is None:
        return redirect('/choose_director')
    else:
        movies = fmdb.movies_by_director(director)
        return render_template('movies.html', movies=movies)


@app.route('/cast_member_movies')
def cast_member_movies():
    cast_member = request.args.get('cast_member')
    if cast_member is None:
        return redirect('/choose_cast')
    else:
        movies = fmdb.movies_by_cast_member(cast_member)
        return render_template('movies.html', movies=movies)


def main():
    app.run()


if __name__ == '__main__':
    main()