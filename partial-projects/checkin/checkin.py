def load_students():
    ''' () -> list[str]

    Returns the list of current students from current_students.txt
    '''
    raise NotImplementedError


def all_checked_in(current_students, checkins):
    ''' (list[str], list[str]) -> bool
    
    Returns True iff all of the current students have checked in.
    '''
    raise NotImplementedError


def is_student(name, current_students):
    '''(str, list[str]) -> bool
    
    Returns True iff the provided name matches one of the name of
    a current student.    
    '''
    raise NotImplementedError


def is_checked_in(name, checkins):
    '''(str, list[str]) -> bool
    
    Returns True iff the provided name matches one of name of
    a checked in student.
    '''
    raise NotImplementedError


def checkin(name, current_students, checkins):
    ''' (str, list[str], list[str]) -> bool

    Returns True iff `name` was successfully checked in.

    Checking in a student adds their name to `checkins`.

    `name` should only be checked in if:
      - they are currently a Base Camp Coding Academy Student
      - they are not already checked_in
    '''
    raise NotImplementedError


def main():
    current_students = load_students()

    checkins = []

    print("Good Morning!")
    while not all_checked_in(current_students, checkins):
        user_response = input(
            '''Enter your name to check in, or enter "quit" to close the application: ''')
        raise NotImplementedError
    print("Goodbye!")


if __name__ == '__main__':
    main()
