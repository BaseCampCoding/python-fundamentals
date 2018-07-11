from loops2 import *

def test_normalize_names():
    assert normalize_names([
        ' AbbY  ',
        '  JoHhNy',
        'Abe',
    ]) == ['abby', 'johhny', 'abe']
    assert normalize_names([]) == []
    assert normalize_names([' J o e l   ']) == ['j o e l']


def test_remove_empty():
    assert remove_empty([]) == []
    assert remove_empty(['']) == []
    assert remove_empty(['john', '']) == ['john']
    assert remove_empty(['', 'john']) == ['john']
    assert remove_empty(['', ' ', '', ' ', '', '']) == [' ', ' ']


def test_split_first_last():
    assert split_first_last([]) == []
    assert split_first_last(['Abe Lincoln']) == [['Abe', 'Lincoln']]
    assert split_first_last([
        'Abe Lincoln',
        'George Washington',
        'Benjamin Franklin',
    ]) == [
        ['Abe', 'Lincoln'],
        ['George', 'Washington'],
        ['Benjamin', 'Franklin'],
    ]


def test_normalized_first_last():
    assert normalized_first_last([]) == []
    assert normalized_first_last(['Abe Lincoln']) == [['abe', 'lincoln']]
    assert normalized_first_last([
        'Abe Lincoln',
        'George Washington',
        'Benjamin Franklin',
    ]) == [
        ['abe', 'lincoln'],
        ['george', 'washington'],
        ['benjamin', 'franklin'],
    ]
    assert normalized_first_last([
        '   Abe Lincoln',
        ' George Washington   ',
        '  Benjamin Franklin    ',
    ]) == [
        ['abe', 'lincoln'],
        ['george', 'washington'],
        ['benjamin', 'franklin'],
    ]


def test_total_revenue():
    assert total_revenue([]) == 0
    assert total_revenue([['burrito', 'food', 3]]) == 3
    assert total_revenue([['burrito', 'food', 3], ['taco', 'food', 2]]) == 5
    assert total_revenue([
        ['burrito', 'food', 3],
        ['taco', 'food', 2],
        ['shirt', 'clothing', 2],
    ]) == 7
    assert total_revenue([
        ['burrito', 'food', 3],
        ['taco', 'food', 2],
        ['shirt', 'clothing', 2],
        ['shirt', 'clothing', 5],
    ]) == 12


def test_total_item_revenue():
    assert total_item_revenue([], 'burrito') == 0
    assert total_item_revenue([['burrito', 'food', 3]], 'burrito') == 3
    assert total_item_revenue([['burrito', 'food', 3], ['taco', 'food', 2]],
                              'taco') == 2
    assert total_item_revenue(
        [['burrito', 'food', 3], ['taco', 'food', 2], ['shirt', 'clothing', 2]],
        'taco') == 2
    assert total_item_revenue(
        [['burrito', 'food', 3], ['taco', 'food', 2], ['shirt', 'clothing', 2],
         ['shirt', 'clothing', 5]], 'shirt') == 7


def test_total_category_revenue():
    assert total_category_revenue([], 'food') == 0
    assert total_category_revenue([['burrito', 'food', 3]], 'clothing') == 0
    assert total_category_revenue([
        ['burrito', 'food', 3],
        ['taco', 'food', 2],
    ], 'food') == 5
    assert total_category_revenue([
        ['burrito', 'food', 3],
        ['taco', 'food', 2],
        ['shirt', 'clothing', 2],
    ], 'clothing') == 2
    assert total_category_revenue([
        ['burrito', 'food', 3],
        ['taco', 'food', 2],
        ['shirt', 'clothing', 2],
        ['shirt', 'clothing', 5],
    ], 'food') == 5


def test_total_minutes_used():
    assert total_minutes_used([]) == 0
    assert total_minutes_used([['(555)555-5555', '(222)222-2222', 3]]) == 3
    assert total_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
    ]) == 5
    assert total_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
    ]) == 7
    assert total_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
        ['(333)333-3333', '(444)444-4444', 5],
    ]) == 12


def test_total_number_minutes_used():
    assert total_number_minutes_used([], '(555)555-5555') == 0
    assert total_number_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
    ], '(555)555-5555') == 3
    assert total_number_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
    ], '(111)111-1111') == 2
    assert total_number_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
    ], '(222)222-2222') == 5
    assert total_number_minutes_used([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
        ['(333)333-3333', '(444)444-4444', 5],
    ], '(333)333-3333') == 7


def test_is_number_over_limit():
    assert not is_number_over_limit([], '(555)555-5555', 5)
    assert is_number_over_limit([
        ['(555)555-5555', '(222)222-2222', 3],
    ], '(555)555-5555', 2)
    assert is_number_over_limit([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
    ], '(111)111-1111', 2)
    assert not is_number_over_limit([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
    ], '(222)222-2222', 6)
    assert is_number_over_limit([
        ['(555)555-5555', '(222)222-2222', 3],
        ['(111)111-1111', '(222)222-2222', 2],
        ['(333)333-3333', '(444)444-4444', 2],
        ['(333)333-3333', '(444)444-4444', 5],
    ], '(333)333-3333', 6)
