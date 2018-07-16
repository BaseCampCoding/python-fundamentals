# FINISH THESE FUNCTIONS
#
# These 4 functions are used by the code at the bottom of the file.
# Your job is to write function bodies for these functions so the
# grocery store program can work.
#
# Start small (print the simplest thing possible).
# Then tweak the output for a more pleasant user experience.
#
# Have fun!


def print_greeting():
    ''' () -> None

    Prints out a greeting to the user whenever the program is started.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def print_item(number, name, price):
    ''' (int, str, float) -> None

    Prints out a description of a single inventory item to the user.
    This code is used when presenting the menu to the user.

    Parameters:
        - number: This is the inventory number for the item. Think of it
                  like a line item number. It doesn't have anything to do
                  with the product itself. It is just used to identify
                  different products.
        - name: The name of the inventory item.
        - price: The price of a single unit of the inventory item.

    If I was trying to print out the description of "chips"
    that cost $1.45 and are line item #3, I would write:
        print_item(3, "chips", 1.45)
    '''
    raise NotImplementedError("Delete this line and put your code here")


def print_cart_item(name, price, quantity):
    ''' (str, float, int) -> None

    Prints out a description of a reciept entry.
    This is used when a customer checks out of the store.

    Parameters:
        - name: The name of the item.
        - price: The price of a single unit of the item.
        - quantity: The quantity being purchased.

    If I was checkout out with 3 bags of chips at $1.75 a piece,
    this code would run:
        print_cart_item("chips", 1.75, 3)
    '''
    raise NotImplementedError("Delete this line and put your code here")


def print_goodbye():
    ''' () -> None

    Prints a goodbye message to your user.
    This is run just before the program finishes.
    '''
    raise NotImplementedError("Delete this line and put your code here")


# DON'T TOUCH THE REST OF THIS
#
# The code below here will call the above functions.
# Don't worry about the stuff below.

from itertools import groupby

inventory = [{
    'name': 'chips',
    'price': 2.45
}, {
    'name': 'coke',
    'price': 1.5
}, {
    'name': 'popcorn',
    'price': 2.0
}, {
    'name': 'sandwich',
    'price': 4.0
}, {
    'name': 'candy',
    'price': 1.0
}]


def shop():
    cart = []
    while True:
        response = get_action()
        if response == 'leave':
            cart.clear()
            break
        elif response == 'checkout':
            checkout(cart)
            break
        else:
            add_to_cart(cart, response)


def get_action():
    while True:
        print_options()
        response = input(">>> ")
        if is_valid_action(response):
            return response
        else:
            print("Invalid response!")


def print_options():
    print("What would you like to add to your cart?")
    print("    \"leave\" to quit without buying")
    print("    \"checkout\" to stop shopping and checkout")
    print("    provide the desired item's number to add to cart")
    for i, item in enumerate(inventory):
        print_item(i, item['name'], item['price'])


def is_valid_action(response):
    return (response == 'leave' or response == 'checkout'
            or is_valid_item_number(response))


def is_valid_item_number(response):
    try:
        return 0 <= int(response) < len(inventory)
    except ValueError:
        return False


def add_to_cart(cart, item_number):
    cart.append(inventory[int(item_number)])


def checkout(cart):
    print_cart(cart)
    print_total_cost(cart)


def print_cart(cart):
    for name, items in groupby(cart, lambda i: i['name']):
        items_list = list(items)
        quantity = len(items_list)
        item = items_list[0]
        print_cart_item(item['name'], item['price'], quantity)


def print_total_cost(cart):
    print(f"Total: ${sum(map(lambda i: i['price'], cart))}")


def main():
    print_greeting()
    shop()
    print_goodbye()


if __name__ == '__main__':
    main()
