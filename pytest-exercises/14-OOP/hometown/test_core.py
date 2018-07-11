import core
import pytest


class TestTopping:
    def setup(self):
        self.pep = core.Topping('Pepperoni', .5)

    def test_topping_init(self):
        assert self.pep.name == 'Pepperoni'
        assert self.pep.price == .5

    def test_topping_str(self):
        assert str(self.pep) == 'Pepperoni ($0.50)'

    def test_topping_repr(self):
        assert repr(self.pep) == 'Topping(\'Pepperoni\',0.5)'


class TestSide:
    def setup(self):
        self.sticks = core.Side('Bread sticks', 1.5)

    def test_side_init(self):
        assert self.sticks.name == 'Bread sticks'
        assert self.sticks._price == 1.5

    def test_side_matches_name_full_match(self):
        assert self.sticks.matches_name('Bread sticks')

    def test_side_matches_name_partial_match(self):
        assert self.sticks.matches_name('Brea')

    def test_side_matches_name_case_insensitive(self):
        assert self.sticks.matches_name('bread st')

    def test_side_str(self):
        assert str(self.sticks) == 'Side Bread sticks ($1.50)'

    def test_side_repr(self):
        assert repr(self.sticks) == 'Side(\'Bread sticks\',1.5)'


class TestPizza:
    def setup(self):
        self.pep = core.Pizza('Pepperoni', [core.Topping('Pepperoni', .75)])

    def test_pizza_init(self):
        assert self.pep.name == 'Pepperoni'
        assert self.pep.base_price == 7
        assert len(self.pep.toppings) == 1

    def test_pizza_price(self):
        assert self.pep.price() == 7.75

    def test_pizza_matches_name_full_match(self):
        assert self.pep.matches_name('Pepperoni')

    def test_pizza_matches_name_partial_match(self):
        assert self.pep.matches_name('Pepp')

    def test_pizza_matches_name_case_insensitive(self):
        assert self.pep.matches_name('pep')

    def test_pizza_matches_name_with_pizza_suffix(self):
        assert self.pep.matches_name('pepperoni pizza')

    def test_pizza_str(self):
        assert str(self.pep) == '''Pepperoni Pizza ($7.75)
    Pepperoni ($0.75)'''

    def test_pizza_repr(self):
        assert repr(
            self.pep) == 'Pizza(\'Pepperoni\',[Topping(\'Pepperoni\',0.75)])'


class TestOrder:
    def setup(self):
        self.pep = core.Pizza('Pepperoni', [core.Topping('Pepperoni', 1.0)])

        self.breadsticks = core.Side('Breadsticks', 2.5)
        self.order = core.Order('Base Camp Coding Academy', [
            self.pep, self.pep, self.pep, self.breadsticks
        ])

    def test_order_init(self):
        assert self.order.customer == 'Base Camp Coding Academy'
        assert self.order.items == [
            self.pep, self.pep, self.pep, self.breadsticks
        ]

    def test_order_total(self):
        assert self.order.total() == 26.5

    def test_order_add_item(self):
        order = core.Order('nate', [])
        order.add_item(self.pep)
        assert order.items == [self.pep]

    def test_order_str(self):
        assert str(self.order) == '''Customer: Base Camp Coding Academy
Total: $26.50
Items
----------------
Pepperoni Pizza ($8.00)
    Pepperoni ($1.00)
Pepperoni Pizza ($8.00)
    Pepperoni ($1.00)
Pepperoni Pizza ($8.00)
    Pepperoni ($1.00)
Side Breadsticks ($2.50)'''

    def test_order_repr(self):
        assert repr(self.order) == (
            'Order(\'Base Camp Coding Academy\',['
            'Pizza(\'Pepperoni\',[Topping(\'Pepperoni\',1.0)]), '
            'Pizza(\'Pepperoni\',[Topping(\'Pepperoni\',1.0)]), '
            'Pizza(\'Pepperoni\',[Topping(\'Pepperoni\',1.0)]), '
            'Side(\'Breadsticks\',2.5)])')


class TestInventory:
    def setup(self):
        self.pep = core.Pizza('Pepperoni', [core.Topping('Pepperoni', 1.0)])
        self.sticks = core.Side('Bread sticks', 1.5)
        self.inventory = core.Inventory([self.pep], [self.sticks])

    def test_inventory_pep_in_stock(self):
        assert self.inventory.in_stock('Pepperoni Pizza')

    def test_inventory_short_pep_in_stock(self):
        assert self.inventory.in_stock('pep')

    def test_inventory_sticks_in_stock(self):
        assert self.inventory.in_stock('Bread sticks')

    def test_inventory_cheese_not_in_stock(self):
        assert not self.inventory.in_stock('Cheese Pizza')

    def test_inventory_pep_get_item(self):
        assert self.inventory.get_item('pep') == self.pep

    def test_inventory_cheese_get_item(self):
        assert self.inventory.get_item('cheese') is None

    def test_inventory_str(self):
        assert str(self.inventory) == '''Pizzas:
Pepperoni Pizza ($8.00)
    Pepperoni ($1.00)
Sides:
Side Bread sticks ($1.50)'''

    def test_inventory_repr(self):
        assert repr(
            self.inventory
        ) == 'Inventory([Pizza(\'Pepperoni\',[Topping(\'Pepperoni\',1.0)])],[Side(\'Bread sticks\',1.5)])'
