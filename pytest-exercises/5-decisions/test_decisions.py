import decisions
from bcca.test import should_print


def test_is_even():
    assert decisions.is_even(2)
    assert not decisions.is_even(3)


def test_is_odd():
    assert not decisions.is_odd(2)
    assert decisions.is_odd(3)


def test_divisible_by_five():
    assert decisions.divisible_by_five(5)
    assert not decisions.divisible_by_five(8)


def test_divisible_by_d():
    assert decisions.divisible_by_d(5, 5)
    assert decisions.divisible_by_d(6, 3)
    assert not decisions.divisible_by_d(3, 6)


def test_problem2a():
    assert decisions.problem2a(True, True)
    assert not decisions.problem2a(True, False)
    assert not decisions.problem2a(False, True)
    assert not decisions.problem2a(False, False)


def test_problem2b():
    assert not decisions.problem2b(True, True)
    assert not decisions.problem2b(True, False)
    assert decisions.problem2b(False, True)
    assert decisions.problem2b(False, False)


def test_problem2c():
    assert decisions.problem2c(True, True)
    assert decisions.problem2c(True, False)
    assert decisions.problem2c(False, True)
    assert not decisions.problem2c(False, False)


def test_problem3():
    assert not decisions.problem3(True, True)
    assert decisions.problem3(True, False)
    assert decisions.problem3(False, True)
    assert decisions.problem3(False, False)


def test_problem5():
    assert decisions.problem5(0)
    assert decisions.problem5(1)
    assert decisions.problem5(1.0)
    assert not decisions.problem5(-1)
    assert not decisions.problem5(-1.0)


def test_problem6():
    assert not decisions.problem6(0, 0)
    assert decisions.problem6(1, 0)
    assert decisions.problem6(0, 1)
    assert decisions.problem6(True, False)
    assert decisions.problem6("Hello", "World")
    assert decisions.problem6("", " ")
    assert not decisions.problem6("", "")


@should_print
def test_problem7a_small_enough(output):
    decisions.problem7a(9999999, 12345)
    assert output == '9999999'


@should_print
def test_problem7a_barely_too_big(output):
    decisions.problem7a(10000000, 12345)
    assert output == ''


@should_print
def test_problem7a_too_big(output):
    decisions.problem7a(10000001, 12345)
    assert output == ''


@should_print
def test_problem7b_too_small(output):
    decisions.problem7b(9999999, 12345)
    assert output == ''


@should_print
def test_problem7b_barely_big_enough(output):
    decisions.problem7b(10000000, 12345)
    assert output == '10000000'


@should_print
def test_problem7b_big_enough(output):
    decisions.problem7b(10000001, 12345)
    assert output == '10000001'


@should_print
def test_problem7b_small_enough(output):
    decisions.problem7b(34999999, 12345)
    assert output == '34999999'


@should_print
def test_problem7b_barely_small_enough(output):
    decisions.problem7b(35000000, 12345)
    assert output == '35000000'


@should_print
def test_problem7b_too_big(output):
    decisions.problem7b(35000001, 12345)
    assert output == ''


@should_print
def test_problem7c_small_not_dense_enough(output):
    decisions.problem7c(100, 1)
    assert output == ''


@should_print
def test_problem7c_small_dense_enough(output):
    decisions.problem7c(101, 1)
    assert output == 'Densely Populated'


@should_print
def test_problem7c_big_not_dense_enough(output):
    decisions.problem7c(1000, 10)
    assert output == ''


@should_print
def test_problem7c_big_dense_enough(output):
    decisions.problem7c(1001, 10)
    assert output == 'Densely Populated'


@should_print
def test_problem7d_small_not_dense_enough(output):
    decisions.problem7d(100, 1)
    assert output == 'Sparsely Populated'


@should_print
def test_problem7d_small_dense_enough(output):
    decisions.problem7d(101, 1)
    assert output == 'Densely Populated'


@should_print
def test_problem7d_big_not_dense_enough(output):
    decisions.problem7d(1000, 10)
    assert output == 'Sparsely Populated'


@should_print
def test_problem7d_big_dense_enough(output):
    decisions.problem7d(1001, 10)
    assert output == 'Densely Populated'
