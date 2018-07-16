def annual_snack_cost(snack_price):
    '''Float -> Float

    Returns the annual cost of buying a snack every weekday for a year (52 weeks).
    '''
    raise NotImplementedError("Delete this line and put your code here")


def snack_cost_breakdown(snack_prices):
    '''List[Float] -> List[Float]

    Returns the annual stack cost for each provided snack price.

    `snack_prices` is a list of floats representing snack prices of snack options.
    
    For example, given the following snack options:
        - Snickers @ $1.00
        - Gum @ $0.10
        - Cake @ $15.00
    the argument list would be [1.0, 0.1, 15.0].
    '''
    raise NotImplementedError("Delete this line and put your code here")


def difference_from_minimum(costs):
    '''List[Float] -> List[Float]

    Returns the difference between each cost and the minimum cost.
    
    For example, if our options were [1, 3, 3, 2, 5].
    The minimum cost would be 1, and the differences from that
    minimum would be [0, 2, 2, 1, 4]
    '''
    raise NotImplementedError("Delete this line and put your code here")


def hashtags(tweet):
    '''String -> List[String]

    Returns the hashtags used in the provided tweet.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def mentions(tweet):
    '''String -> List[String]

    Returns the mentions used in the provided tweet.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def reverse_my_words(message):
    '''String -> String

    Returns the message, but with each word reversed.
    '''
    raise NotImplementedError("Delete this line and put your code here")


def parse_inventory_item(string):
    '''String -> Item

    Return an inventory item encoded in the provided string.

    An Item is a list of 3 elements:
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
