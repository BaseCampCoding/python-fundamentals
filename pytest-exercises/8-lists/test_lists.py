from lists import *

def test_first_three():
    assert first_three([1, 2, 3]) == [1, 2, 3]
    assert first_three([1, 2, 3, 4]) == [1, 2, 3]
    assert first_three([]) == []
    assert first_three([1, 2]) == [1, 2]
    assert first_three([5, 4, 3, 2]) == [5, 4, 3]


def test_last_three():
    assert last_three([1, 2, 3]) == [1, 2, 3]
    assert last_three([1, 2, 3, 4]) == [2, 3, 4]
    assert last_three([]) == []
    assert last_three([1, 2]) == [1, 2]
    assert last_three([5, 4, 3, 2]) == [4, 3, 2]


def test_first_n():
    assert first_n([1, 2, 3, 4], 2) == [1, 2]
    assert first_n([1, 2, 3, 4], 0) == []
    assert first_n([4, 3, 2, 1], 3) == [4, 3, 2]
    assert first_n([1, 3, 5], 5) == [1, 3, 5]
    assert first_n([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]


def test_bookends():
    assert bookends([1, 2, 3]) == [1, 3]
    assert bookends([1, 2, 3, 4]) == [1, 4]
    assert bookends([4, 3, 2, 1]) == [4, 1]
    assert bookends([5, 7]) == [5, 7]
    assert bookends([9]) == []
    assert bookends([]) == []


def test_insides():
    assert insides([1, 2, 3]) == [2]
    assert insides([1, 2]) == []
    assert insides([1, 2, 3, 4]) == [2, 3]
    assert insides([1, 3, 8, 12]) == [3, 8]
    assert insides([]) == []
    assert insides([5]) == []


def test_combine():
    assert combine([1, 2], [2, 1]) == [1, 2, 2, 1]
    assert combine([1], [2]) == [1, 2]
    assert combine([], [7, 2, 3]) == [7, 2, 3]
    assert combine([5, 67, 9], []) == [5, 67, 9]


def test_doubled_bookends():
    assert doubled_bookends([]) == []
    assert doubled_bookends([5678]) == []
    assert doubled_bookends([7, 4]) == [14, 8]
    assert doubled_bookends([6, 3, 2, 1234, 8]) == [12, 16]


def test_average():
    assert average([]) == None
    assert average([1]) == 1.0
    assert average([1, 2, 3]) == 2.0
    assert average([5, 5, 10, 10]) == 7.5


def test_lucky_number_seven():
    assert not lucky_number_seven([])
    assert not lucky_number_seven([1])
    assert lucky_number_seven([7])
    assert lucky_number_seven([1, 7])
    assert not lucky_number_seven([1, 2])
    assert lucky_number_seven([1, 7, 2])


def test_longer():
    assert longer([], [1]) == [1]
    assert longer([3], []) == [3]
    assert longer([3], [4]) == [3, 4]
    assert longer([3, 4], [4, 3]) == [3, 4, 4, 3]
    assert longer([1, 3, 3], [4, 7]) == [1, 3, 3]
    assert longer([8, 7, 3], [1, 2, 2, 1]) == [1, 2, 2, 1]


def test_list_with_min():
    assert list_with_min([1, 2, 3, -1, 4], [2]) == [1, 2, 3, -1, 4]
    assert list_with_min([1, 2, 3, 1, 4], [1, 2, 3, -1, 4]) == [1, 2, 3, -1, 4]
    assert list_with_min([1, 2, 3, -1, 4], [5, -2, 3]) == [5, -2, 3]
    assert list_with_min([-1], [-2]) == [-2]
    assert list_with_min([-1, 2, -3], [-3]) == [-1, 2, -3]
    assert list_with_min([-3], [-1, 2, -3]) == [-3]


def test_index_of_index_of_five():
    assert index_of_index_of_five([1, 5]) == 0
    assert index_of_index_of_five([5, 0]) == 1
    assert index_of_index_of_five([0, 5, 0, 1]) == 3
    assert index_of_index_of_five([0, 5, 0, 0, 1]) == 4
    assert index_of_index_of_five([0, 5, 0, 0, 0, 1]) == 5
    assert index_of_index_of_five([0, 1, 5, 0, 2]) == 4
    assert index_of_index_of_five([0, 5, 0, 1]) == 3


def test_sum_indicies_two_and_three():
    assert sum_indicies_two_and_three([0, 1, 2, 3, 4, 5, 6]) == 5
    assert sum_indicies_two_and_three([2, 3]) == 1
    assert sum_indicies_two_and_three([0, 1, 2, 3]) == 5
    assert sum_indicies_two_and_three([0, 2, 1, 3, 4, 5, 6]) == 4
    assert sum_indicies_two_and_three([2, 0, 0, 0, 0, 0, 3]) == 6
    assert sum_indicies_two_and_three([0, 0, 0, 2, 0, 0, 3]) == 9
    assert sum_indicies_two_and_three([0, 0, 0, 3, 0, 0, 2]) == 9


def test_list_of_three_ls():
    assert list_of_three_ls([1]) == [[1], [1], [1]]
    assert list_of_three_ls([1, 2]) == [[1, 2], [1, 2], [1, 2]]
    assert list_of_three_ls([]) == [[], [], []]
    assert list_of_three_ls([4, 3, 2]) == [[4, 3, 2], [4, 3, 2], [4, 3, 2]]


def test_n_times_l():
    assert n_times_l([], 3) == []
    assert n_times_l([1], 3) == [1, 1, 1]
    assert n_times_l([1, 2], 3) == [1, 2, 1, 2, 1, 2]
    assert n_times_l([1, 2], 5) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]


def test_list_of_n_ls():
    assert list_of_n_ls([1], 3) == [[1], [1], [1]]
    assert list_of_n_ls([1, 2], 3) == [[1, 2], [1, 2], [1, 2]]
    assert list_of_n_ls([], 5) == [[], [], [], [], []]
    assert list_of_n_ls([4, 3, 2], 1) == [[4, 3, 2]]
    assert list_of_n_ls([4, 3, 2], 0) == []
    assert list_of_n_ls([4, 2], 5) == [[4, 2], [4, 2], [4, 2], [4, 2], [4, 2]]


def test_sum_of_insides_and_len():
    assert sum_of_insides_and_len([]) == 0
    assert sum_of_insides_and_len([1]) == 1
    assert sum_of_insides_and_len([1, 2]) == 2
    assert sum_of_insides_and_len([1, 2, 3]) == 5
    assert sum_of_insides_and_len([5, 5, 5]) == 8
    assert sum_of_insides_and_len([1, 2, 3, 4, 5]) == 14
    assert sum_of_insides_and_len([7, 0, 0, 0, 0, 7]) == 6


def test_sum_of_longer():
    assert sum_of_longer([], [1]) == 1
    assert sum_of_longer([1], [1]) == 2
    assert sum_of_longer([2], [1]) == 3
    assert sum_of_longer([2, 2], [1]) == 4
    assert sum_of_longer([1, 2, 3], [1]) == 6
    assert sum_of_longer([1, 2, 3], [1, 2, 3, 4]) == 10
