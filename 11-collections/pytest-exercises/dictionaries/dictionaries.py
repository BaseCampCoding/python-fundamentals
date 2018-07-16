def parse_inventory_item(string):
    '''String -> Item

    Return an inventory item encoded in the provided string.

    An Item is a dictionary of 3 elements:
        - name
        - price we paid
        - price we're charging

    The provided string seperates each of these pieces with a tab.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def profit(item):
    '''Item -> Float

    Returns the profit earned by selling the provided Item.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def profits(items):
    '''List[Item] -> Float

    Returns the profit earned by selling all of the provided Items.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def is_dollar_store(inventory):
    '''Dict[String, Item] -> Boolean

    Returns True if the provided inventory is a "dollar store".
    The store is a dollar store if all of its inventory costs $1 or less.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def items_to_buy_here(inventory, grocery_list):
    '''(Dict[String, Item], List[str]) -> List[str]

    I have 2 parameters:
        - the first is a Dictionary where the keys are Strings and the values are Items
        - the second is a List of Strings

    I return a List of Strings

    Return the list of items from `grocery_list` that can be found
    in `inventory`.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def cost_of_groceries(inventory, grocery_list):
    '''(Dict[String, Item], List[str]) -> float

    Return the cost of buying items from `grocery_list` at `inventory`.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def read_inventory(string):
    '''String -> Dict[String, Item]

    Reads an inventory in from a provided string.
    Each line of the string represents a single inventory item formatted as described by `parse_into_inventory`.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def inventory_to_string(inventory):
    '''Dict[String, Item] -> String

    Returns a string representation of the provided inventory.
    The string format of the inventory is the same as the one provided to `read_inventory`
    The items should be written out in alphabetical order according to their names.
    '''
    raise NotImplementedError("Delete this line and put your code here")
