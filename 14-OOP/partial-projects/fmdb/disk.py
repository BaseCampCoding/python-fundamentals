import core
import csv


def load_fmdb():
    with open('./movie_metadata.csv') as f:
        reader = csv.DictReader(f)
        movies = []
        for entry in reader:
            title = entry['movie_title']
            director = entry['director_name']
            genre = entry['genres'].split('|')[0]
            cast = []
            for key in entry:
                if key.startswith('actor') and key.endswith('name'):
                    cast.append(entry[key])
            movies.append(core.Movie(title, director, genre, cast))
    return core.FMDB(movies)