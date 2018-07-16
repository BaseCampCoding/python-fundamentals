import disk


def get_search_by():
    while True:
        print('Search by: [d]irector, [c]ast member, or [q]uit')
        response = input('->  ')
        if response in ['c', 'd', 'q']:
            return response
        else:
            print('Invalid option!')


def main():
    fmdb = disk.load_fmdb()
    print('Welcome to the (not so) Fake Movie Database!')
    while True:
        search_by = get_search_by()
        if search_by == 'q':
            break

        name = input('Who would you like to search for? ')
        if search_by == 'c':
            movies = fmdb.movies_by_cast_member(name)
        elif search_by == 'd':
            movies = fmdb.movies_by_director(name)
        for movie in movies:
            print(movie)
            print()
    print('Goodbye!')


if __name__ == '__main__':
    main()