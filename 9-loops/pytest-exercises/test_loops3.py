from bcca.test import should_print

from loops3 import *


@should_print
def test_print_all_empty(output):
    print_all([])

    assert output == ''


@should_print
def test_print_all_one(output):
    print_all([1])

    assert output == '1'


@should_print
def test_print_all_one_to_three(output):
    print_all([1, 2, 3])

    assert output == '''
1
2
3'''


@should_print
def test_print_all_three_to_one(output):
    print_all([3, 2, 1])
    assert output == '''
3
2
1
'''


def test_double_all():
    test_list = []
    double_all(test_list)
    assert test_list == []

    test_list = [1]
    double_all(test_list)
    assert test_list == [2]

    test_list = [3, 2, 1]
    double_all(test_list)
    assert test_list == [6, 4, 2]


def test_doubled_list():
    test_list = [1, 2, 3]
    assert doubled_list(test_list) == [2, 4, 6]
    assert test_list == [1, 2, 3]
    assert doubled_list(doubled_list(test_list)) == [4, 8, 12]
    assert doubled_list([]) == []


@should_print
def test_print_with_numbers_empty(output):
    print_with_numbers([])

    assert output == ''


@should_print
def test_print_with_numbers_single(output):
    print_with_numbers([5678])

    assert output == '1. 5678'


@should_print
def test_print_with_numbers_three(output):
    print_with_numbers(['a', 'b', 'c'])

    assert output == '''
1. a
2. b
3. c
'''


def test_reversed_list():
    test_list = [6, 7, 4]
    assert reversed_list(test_list) == [4, 7, 6]
    assert test_list == [6, 7, 4]
    assert reversed_list(reversed_list(test_list)) == test_list
    assert reversed_list([]) == []


def test_students_per_class():
    assert students_per_class([
        ['alice', 'bob', 'chloe'],
        ['david', 'everett'],
    ]) == [3, 2]
    assert students_per_class([]) == []
    assert students_per_class([['frank', 'gino']]) == [2]


@should_print
def test_print_steps_zero(output):
    print_steps(0)

    assert output == ''


@should_print
def test_print_steps_one(output):
    print_steps(1)

    assert output == 'M'


@should_print
def test_print_steps_two(output):
    print_steps(2)

    assert output == '''
M
MM
'''


@should_print
def test_print_steps_three(output):
    print_steps(3)

    assert output == '''
M
MM
MMM
'''


@should_print
def test_bar_chart_empty(output):
    bar_chart([])

    assert output == ''


@should_print
def test_bar_chart_one(output):
    bar_chart([1])

    assert output == 'M'


@should_print
def test_bar_chart_5(output):
    bar_chart([1, 3, 5, 3, 1])

    assert output == '''
M
MMM
MMMMM
MMM
M
'''


@should_print
def test_labelled_bar_chart_empty(output):
    labelled_bar_chart([])

    assert output == ''


@should_print
def test_labelled_bar_chart_single_empty(output):
    labelled_bar_chart([['label1', 0]])

    assert output == ' label1'


@should_print
def test_labelled_bar_chart_single_nonempty(output):
    labelled_bar_chart([['l2', 3]])

    assert output == 'MMM l2'


@should_print
def test_labelled_bar_chart_multiple_nonempty(output):
    labelled_bar_chart([['l1', 5], ['a3', 9], ['apples', 4]])

    assert output == '''
MMMMM l1
MMMMMMMMM a3
MMMM apples
'''


def test_what_should_i_buy():
    assert what_should_i_buy([], []) == []
    assert what_should_i_buy([], ['apples']) == []
    assert what_should_i_buy(['apples'], ['apples']) == []
    assert what_should_i_buy(['apples', 'bananas'], ['apples']) == ['bananas']
    assert what_should_i_buy(['bananas', 'apples'], ['apples']) == ['bananas']
    assert what_should_i_buy(['apples', 'bananas'],
                             ['cupcakes']) == ['apples', 'bananas']


@should_print
def test_exercise_report(output):
    exercise_report([
        ['is_even', True],
        ['is_odd', True],
        ['gold_stars', False],
        ['damage_dealt', False],
        ['walk_or_drive', True],
    ])

    assert output == '''
Incorrect Problems:
gold_stars
damage_dealt
'''


def test_decode_message():
    assert decode_message([2, 1, 0], ['y', 'e', 'H']) == 'Hey'
    assert decode_message(
        [2, 1, 7, 7, 0, 4, 3, 0, 5, 7, 6],
        ['o', 'e', 'H', 'W', ' ', 'r', 'd', 'l'],
    ) == 'Hello World'
    assert decode_message(
        [4, 3, 5, 3, 5, 3, 6, 0, 3, 4, 3, 5, 3, 6, 1, 3, 5, 2, 3, 5, 3],
        ['c', 's', 't', 'a', 'b', 'n', ' '],
    ) == 'banana cabana santana'
