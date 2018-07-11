from loops1 import *

def test_annual_snack_cost():
    assert annual_snack_cost(1.0) == 260.0
    assert annual_snack_cost(.75) == 195.0
    assert annual_snack_cost(1.5) == 390.0


def test_snack_cost_breakdown():
    assert snack_cost_breakdown([1.0, .75, 1.5]) == [260.0, 195.0, 390.0]
    assert snack_cost_breakdown([2.50, .25, 8.0]) == [650.0, 65.0, 2080.0]


def test_difference_from_minimum():
    assert difference_from_minimum([260.0, 195.0, 390.0]) == [65.0, 0.0, 195.0]
    assert difference_from_minimum([
        650.0,
        65.0,
        2080.0,
    ]) == [585.0, 0.0, 2015.0]


def test_hashtags():
    assert hashtags('#python is #totes the best.') == ['#python', '#totes']
    assert hashtags('@nate ... who says #totes') == ['#totes']
    assert hashtags('@SomeFashionStore is having a #FireSale on trendy #Totes',
                    ) == ['#FireSale', '#Totes']


def test_mentions():
    assert mentions('#python is #totes the best.') == []
    assert mentions('@nate ... who says #totes') == ['@nate']
    assert mentions('@SomeFashionStore is having a #FireSale on trendy #Totes',
                    ) == ['@SomeFashionStore']


def test_reverse_my_words():
    assert reverse_my_words('Hello World') == 'olleH dlroW'
    assert reverse_my_words('reverse_my_words') == 'sdrow_ym_esrever'
    assert reverse_my_words('reverse my words') == 'esrever ym sdrow'


def test_parse_inventory_item():
    assert parse_inventory_item('Coke\t0.40\t1.00') == ['Coke', 0.4, 1.0]
    assert parse_inventory_item('Tab\t0.54\t1.49') == ['Tab', 0.54, 1.49]


def test_profit():
    assert profit(['Coke', 0.3, 1.0]) == 0.7
    assert profit(['Tab', 0.54, 1.49]) == 0.95


def test_profits():
    assert profits([]) == 0.0
    assert profits([['Coke', 0.3, 1.0]]) == 0.7
    assert profits([['Coke', 0.3, 1.0], ['Tab', 0.54, 1.49]]) == 1.65
