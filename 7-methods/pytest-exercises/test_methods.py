import methods

from pytest import approx

def test_greeting():
    assert methods.greeting('Base Camp') == 'Hello, Base Camp!'
    assert methods.greeting('World') == 'Hello, World!'


def test_city_banner():
    assert methods.city_banner('Water Valley', 50) == '             Welcome to Water Valley!             '
    assert methods.city_banner('Los Angeles', 40) == '        Welcome to Los Angeles!         '
    assert methods.city_banner('Megaton', 60) == '                    Welcome to Megaton!                     '


def test_how_long_is_my_name():
    assert methods.how_long_is_my_name('Gordon Freeman') == "The name 'Gordon Freeman' is 14 characters long"
    assert methods.how_long_is_my_name('Alyx Vance') == "The name 'Alyx Vance' is 10 characters long"


def test_student_email():
    assert methods.student_email('Andrew', 'Ryan') == 'aryan@basecampcodingacademy.org'
    assert methods.student_email('Elizabeth', 'DeWitt') == 'edewitt@basecampcodingacademy.org'


def test_old_enough_to_vote():
    assert not methods.old_enough_to_vote(8)
    assert methods.old_enough_to_vote(18)
    assert not methods.old_enough_to_vote(17)
    assert methods.old_enough_to_vote(28)

def test_has_two_os():
    assert not methods.has_two_os('Base Camp Coding Academy')
    assert methods.has_two_os('Coookie Crisp')
    assert methods.has_two_os('Oolacile')


def test_has_more_e_than_a():
    assert not methods.has_more_e_than_a('Big Hat Logan')
    assert methods.has_more_e_than_a('Seathe')
    assert not methods.has_more_e_than_a('Dusk')


def test_walk_or_drive():
    assert methods.walk_or_drive(.2, True) == 'walk'
    assert methods.walk_or_drive(.2, False) == 'drive'
    assert methods.walk_or_drive(.3, True) == 'drive'
    assert methods.walk_or_drive(.3, False) == 'drive'


def test_gold_stars():
    assert methods.gold_stars(900) == '*'
    assert methods.gold_stars(1900) == '**'
    assert methods.gold_stars(7999) == '***'
    assert methods.gold_stars(9001) == '****'
    assert methods.gold_stars(1234567) == '*****'


def test_damage_dealt():
    assert methods.damage_dealt(100, 0, False) == approx(100.0)
    assert methods.damage_dealt(100, 0, True) == approx(25.0)
    assert methods.damage_dealt(50, 10, False) == approx(40.0)
    assert methods.damage_dealt(50, 10, True) == approx(10.0)
    assert methods.damage_dealt(10, 50, False) == approx(0.0)
    assert methods.damage_dealt(30, 30, True) == approx(0.0)


def test_how_many_points():
    assert methods.how_many_points('extra kick') == 1
    assert methods.how_many_points('extra conv') == 2
    assert methods.how_many_points('safety') == 2
    assert methods.how_many_points('fg') == 3
    assert methods.how_many_points('td') == 6
