from dictionaries import *


def test_parse_inventory_item():
    assert parse_inventory_item('Coke\t0.40\t1.00') == {
        'name': 'Coke',
        'paid': .4,
        'charging': 1.0,
    }

    assert parse_inventory_item('Tab\t0.54\t1.49') == {
        'name': 'Tab',
        'paid': 0.54,
        'charging': 1.49
    }


def test_profit():
    assert profit({'name': 'Coke', 'paid': 0.3, 'charging': 1.0}) == 0.7

    assert profit({'name': 'Tab', 'paid': 0.54, 'charging': 1.49}) == 0.95


def test_profits():
    assert profits([]) == 0.0

    assert profits([{'name': 'Coke', 'paid': 0.3, 'charging': 1.0}]) == 0.7

    assert profits([
        {
            'name': 'Coke',
            'paid': 0.3,
            'charging': 1.0
        },
        {
            'name': 'Tab',
            'paid': 0.54,
            'charging': 1.49
        },
    ]) == 1.65


def test_is_dollar_store():
    assert is_dollar_store({})

    assert not is_dollar_store({
        'Regular': {
            'name': 'Regular',
            'charging': 2.1,
            'paid': 2.0
        },
        'Mid Grade': {
            'name': 'Mid Grade',
            'charging': 2.4,
            'paid': 2.2
        },
        'Premium': {
            'name': 'Premium',
            'charging': 2.7,
            'paid': 2.4
        }
    })

    assert not is_dollar_store({
        'Apples': {
            'name': 'Apples',
            'charging': 2.1,
            'paid': 2.0
        },
        'Bananas': {
            'name': 'Bananas',
            'charging': 2.4,
            'paid': 2.3
        }
    })

    assert not is_dollar_store({
        'Chips': {
            'name': 'Chips',
            'charging': .75,
            'paid': .5
        },
        'Coke': {
            'name': 'Coke',
            'charging': .6,
            'paid': .5
        },
        'Car': {
            'name': 'Car',
            'charging': 6000.0,
            'paid': 5500.0
        }
    })

    assert is_dollar_store({
        'Chips': {
            'name': 'Chips',
            'charging': .75,
            'paid': .5
        },
        'Coke': {
            'name': 'Coke',
            'charging': .6,
            'paid': .5
        },
        'Can': {
            'name': 'Can',
            'charging': .06,
            'paid': 0
        }
    })


def test_items_to_buy_here():
    sample_inventory = {
        'Chips': {
            'name': 'Chips',
            'paid': 0.5,
            'charging': 1.25
        },
        'Pizza': {
            'name': 'Pizza',
            'paid': 3.0,
            'charging': 5.0
        },
        'Coke': {
            'name': 'Coke',
            'paid': 0.4,
            'charging': 1.0
        }
    }

    assert items_to_buy_here(
        sample_inventory,
        ['Chips', 'Dip', 'Pizza', 'Dr. Pepper', 'A Movie About Explosions'],
    ) == ['Chips', 'Pizza']

    assert items_to_buy_here(sample_inventory, [
        'Chips', 'Fancy Dip', 'Expensive Water',
        'A Somber Meeting of Distant and Estranged Relatives'
    ]) == ['Chips']

    assert items_to_buy_here({}, []) == []

    assert items_to_buy_here(sample_inventory, []) == []

    assert items_to_buy_here({}, ['Coke']) == []


def test_cost_of_groceries():
    sample_inventory = {
        'Chips': {
            'name': 'Chips',
            'paid': 0.5,
            'charging': 1.25
        },
        'Pizza': {
            'name': 'Pizza',
            'paid': 3.0,
            'charging': 5.0
        },
        'Coke': {
            'name': 'Coke',
            'paid': 0.4,
            'charging': 1.0
        }
    }

    assert cost_of_groceries(
        sample_inventory,
        ['Chips', 'Dip', 'Pizza', 'Dr. Pepper', 'A Movie About Explosions'],
    ) == 6.25

    assert cost_of_groceries(sample_inventory, [
        'Chips', 'Fancy Dip', 'Expensive Water',
        'A Somber Meeting of Distant and Estranged Relatives'
    ]) == 1.25

    assert cost_of_groceries({}, []) == 0

    assert cost_of_groceries(sample_inventory, []) == 0

    assert cost_of_groceries({}, ['Coke']) == 0


def test_read_inventory():
    assert read_inventory('') == {}

    assert read_inventory('Coke\t0.40\t1.00\nTab\t0.54\t1.49') == {
        'Coke': {
            'name': 'Coke',
            'paid': .4,
            'charging': 1.0
        },
        'Tab': {
            'name': 'Tab',
            'paid': 0.54,
            'charging': 1.49
        }
    }

    assert read_inventory('Chips\t0.5\t1.25\nPizza\t3.00\t5.00\nCoke\t0.4\t1.0') == {
        'Chips': {
            'name': 'Chips',
            'paid': 0.5,
            'charging': 1.25
        },
        'Pizza': {
            'name': 'Pizza',
            'paid': 3.0,
            'charging': 5.0
        },
        'Coke': {
            'name': 'Coke',
            'paid': 0.4,
            'charging': 1.0
        }
    }


def test_inventory_to_string():
    assert inventory_to_string({
        'Coke': {
            'name': 'Coke',
            'paid': .4,
            'charging': 1.0
        },
        'Tab': {
            'name': 'Tab',
            'paid': 0.54,
            'charging': 1.49
        }
    }) == 'Coke\t0.4\t1.0\nTab\t0.54\t1.49'

    assert inventory_to_string({
        'Chips': {
            'name': 'Chips',
            'paid': 0.5,
            'charging': 1.25
        },
        'Pizza': {
            'name': 'Pizza',
            'paid': 3.0,
            'charging': 5.0
        },
        'Coke': {
            'name': 'Coke',
            'paid': 0.4,
            'charging': 1.0
        }
    }) == 'Chips\t0.5\t1.25\nCoke\t0.4\t1.0\nPizza\t3.0\t5.0'
