import core
import pytest


class TestListContains:

    @staticmethod
    def test_does_not_explode_for_empty_list():
        assert not core.contains([], 'anything')

    @staticmethod
    def test_returns_true_for_first_element():
        assert core.contains([1, 2, 3], 1)

    @staticmethod
    def test_return_true_for_inside_element():
        assert core.contains(['a', 'b', 'c'], 'b')

    @staticmethod
    def test_returns_true_for_last_element():
        assert core.contains([1, 'b', 3, 9], 9)

    @staticmethod
    def test_returns_false_for_elements_not_in_list():
        assert not core.contains([1, 2, 3], 5)
        assert not core.contains(['a', 'b', 'c'], 2)
        assert not core.contains([1, 'b', 3, 9], 4)


class TestListLength:

    @staticmethod
    def test_returns_zero_for_empty_list():
        assert core.length([]) == 0

    @staticmethod
    def test_returns_one_for_list_of_one():
        assert core.length([0]) == 1
        assert core.length([[]]) == 1
        assert core.length([3]) == 1

    @staticmethod
    def test_returns_correct_answer_for_larger_list():
        assert core.length(['a', 'b', 'c', 'd']) == 4
        assert core.length([1, 2, 3]) == 3


class TestListSlice:

    @staticmethod
    def test_does_not_explode_for_empty_list():
        assert core.slice([], 0, 0) == []

    @staticmethod
    def test_returns_entire_list_for_whole_slice():
        assert core.slice([1, 2, 3, 4], 0, 4) == [1, 2, 3, 4]

    @staticmethod
    def test_from_one_skips_first_element():
        assert core.slice([1, 2, 3, 4], 1, 4) == [2, 3, 4]

    @staticmethod
    def test_up_to_end_excludes_last_one():
        assert core.slice([1, 2, 3, 4], 0, 3) == [1, 2, 3]

    @staticmethod
    def test_can_cut_off_both_ends():
        assert core.slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


class TestListCount:

    @staticmethod
    def test_does_not_explode_for_empty_list():
        assert core.count([], 5678) == 0

    @staticmethod
    def test_returns_correct_values_for_singletons():
        assert core.count(['a'], 'a') == 1
        assert core.count(['b'], 'a') == 0
        assert core.count(['a'], 'b') == 0
        assert core.count(['b'], 'b') == 1

    @staticmethod
    def test_returns_correct_values_for_larger_lists():
        assert core.count([1, 2, 3, 4], 3) == 1
        assert core.count([1, 1, 3, 3, 4, 1, 2], 2) == 1
        assert core.count([1, 1, 3, 3, 4, 1, 2], 3) == 2
        assert core.count([1, 1, 3, 3, 4, 1, 2], 1) == 3


class TestListAppended:

    @staticmethod
    def test_does_not_explode_for_empty_list():
        assert core.appended([], 1) == [1]
        assert core.appended([], 'a') == ['a']
        assert core.appended([], []) == [[]]

    @staticmethod
    def test_works_for_singletons():
        assert core.appended([1], 2) == [1, 2]
        assert core.appended(['a'], 'c') == ['a', 'c']

    @staticmethod
    def test_works_for_larger_lists():
        assert core.appended([1, 2, 3, 4, 5], 9) == [
            1, 2, 3, 4, 5, 9]
        assert core.appended([1, 39, 'b', [], [], []], 'c') == [
            1, 39, 'b', [], [], [], 'c']


class TestListExtended:

    @staticmethod
    def test_does_not_explode_for_empty_lists():
        assert core.extended([], []) == []

    @staticmethod
    def test_works_for_singletons():
        assert core.extended([1], [2]) == [1, 2]
        assert core.extended([1], []) == [1]
        assert core.extended([], ['c']) == ['c']

    @staticmethod
    def test_works_for_larger_lists():
        assert core.extended([1, 2, 3], []) == [1, 2, 3]
        assert core.extended([], [1, 2, 3]) == [1, 2, 3]
        assert core.extended([1, 2, 3], [1, 2, 3]) == [
            1, 2, 3, 1, 2, 3]


class TestListInserted:

    @staticmethod
    def test_does_not_explode_for_empty_list():
        assert core.inserted([], 0, 'a') == ['a']

    @staticmethod
    def test_works_for_singleton_lists():
        assert core.inserted(['b'], 0, 'a') == ['a', 'b']
        assert core.inserted(['b'], 1, 'a') == ['b', 'a']

    @staticmethod
    def test_works_for_larger_lists():
        assert core.inserted([1, 2, 3], 1, 'b') == [1, 'b', 2, 3]
        assert core.inserted([1, 2, 3], 2, 'b') == [1, 2, 'b', 3]
        assert core.inserted([1, 2, 3], 3, 'b') == [1, 2, 3, 'b']