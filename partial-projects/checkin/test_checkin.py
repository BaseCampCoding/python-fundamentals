from bcca.test import should_print, with_inputs

from checkin import *


def test_all_checked_in():
    assert all_checked_in([], [])

    assert not all_checked_in(['nate'], [])

    assert all_checked_in(['nate'], ['nate'])

    assert not all_checked_in(['nate', 'evil nate'], ['nate'])

    assert all_checked_in(['nate', 'evil nate'], ['evil nate', 'nate'])


def test_is_student():
    assert not is_student('nate', [])

    assert not is_student('', [])

    assert is_student('nate', ['nate'])

    assert is_student('nate', ['evil nate', 'nate'])

    assert is_student('evil nate', ['nate', 'evil nate'])

    assert not is_student('evil nate', ['nate', 'good nate'])


def test_is_checked_in():
    assert not is_checked_in('nate', [])

    assert not is_checked_in('', [])

    assert is_checked_in('nate', ['nate'])

    assert is_checked_in('nate', ['evil nate', 'nate'])

    assert is_checked_in('evil nate', ['nate', 'evil nate'])

    assert not is_checked_in('evil nate', ['nate', 'good nate'])


def test_checkin_success():
    '''
    `nate` is a current student that is not currently checked in.

    `checkin` should successfully return `True` and add `nate`
    to `checkins`
    '''
    students = ['nate', 'good nate', 'evil nate']
    checkins = ['good nate']

    assert checkin('nate', students, checkins)

    assert students == ['nate', 'good nate', 'evil nate']
    assert checkins == ['good nate', 'nate']


def test_checkin_non_student():
    '''
    `evil nate` is not a current student so `checkin` should return
    `False` and not add `nate` to `checkins`.
    '''
    students = ['nate']
    checkins = []

    assert not checkin('evil nate', students, checkins)

    assert students == ['nate']
    assert checkins == []


def test_checkin_all_empty():
    '''
    The empty string isn't a current student, so this should fail.

    This test is mostly about checking for edge cases around empty
    lists/strings.
    '''
    assert not checkin('', [], [])


def test_checkin_already_checkedin():
    '''
    `nate` is a valid student, but `nate` is already checked in.
    `checkin` should return False and not add `nate` to checkins.
    '''
    students = ['nate', 'good nate', 'evil nate']
    checkins = ['good nate', 'nate']

    assert not checkin('nate', students, checkins)

    assert students == ['nate', 'good nate', 'evil nate']
    assert checkins == ['good nate', 'nate']


@should_print
@with_inputs('quit')
def test_main_immediate_quit(output):
    main()

    assert output == '''
Good Morning!
Enter your name to check in, or enter "quit" to close the application: quit
Goodbye!
'''


@should_print
@with_inputs('Jakylan Standifer', 'quit')
def test_main_checkin_one_student(output):
    main()

    assert output == '''
Good Morning!
Enter your name to check in, or enter "quit" to close the application: Jakylan Standifer
Thanks Jakylan Standifer! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: quit
Goodbye!
'''


@should_print
@with_inputs(
    'Cody vander Poel',
    'Cody van der Poel',
    'quit',
)
def test_main_typo_then_correction(output):
    main()

    assert output == '''
Good Morning!
Enter your name to check in, or enter "quit" to close the application: Cody vander Poel
Unable to checkin. Did you enter a current student's name?
Enter your name to check in, or enter "quit" to close the application: Cody van der Poel
Thanks Cody van der Poel! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: quit
Goodbye!
'''


@should_print
@with_inputs(
    'Cole Anderson',
    'Timothy Bowling',
    'Logan Harrell',
    'Desma Hervey',
    'Ginger Keys',
    'Matt Lipsey',
    'Myeisha Madkins',
    'Henry Moore',
    'John Morgan',
    'Irma Patton',
    'Danny Peterson',
    'Jakylan Standifer',
    'Justice Taylor',
    'Ray Turner',
    'Cody van der Poel',
    'Andrew Wheeler',
)
def test_main_everyone_signs_in(output):
    main()

    assert output == '''
Good Morning!
Enter your name to check in, or enter "quit" to close the application: Cole Anderson
Thanks Cole Anderson! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Timothy Bowling
Thanks Timothy Bowling! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Logan Harrell
Thanks Logan Harrell! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Desma Hervey
Thanks Desma Hervey! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Ginger Keys
Thanks Ginger Keys! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Matt Lipsey
Thanks Matt Lipsey! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Myeisha Madkins
Thanks Myeisha Madkins! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Henry Moore
Thanks Henry Moore! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: John Morgan
Thanks John Morgan! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Irma Patton
Thanks Irma Patton! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Danny Peterson
Thanks Danny Peterson! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Jakylan Standifer
Thanks Jakylan Standifer! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Justice Taylor
Thanks Justice Taylor! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Ray Turner
Thanks Ray Turner! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Cody van der Poel
Thanks Cody van der Poel! You're all checked in!
Enter your name to check in, or enter "quit" to close the application: Andrew Wheeler
Thanks Andrew Wheeler! You're all checked in!
Goodbye!
'''
