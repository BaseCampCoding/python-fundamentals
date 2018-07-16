def normalize_names(names):
    '''List[String] -> List[String]

    Return the a lowercased, stripped version of names.
    '''


def remove_empty(names):
    '''List[String] -> List[String]

    Return the provided names excluding empty strings.
    '''


def split_first_last(whole_names):
    '''List[String] -> List[List[String]]

    whole_names is a list of whole names (e.g. "Abe Lincoln").
    Return a list with each name split into first and last name (e.g. ['Abe', 'Lincoln'])
    '''


def normalized_first_last(whole_names):
    '''List[String] -> List[List[String]]

    whole_names is a list of whole names (e.g. "Abe Lincoln").
    Return a list with each name split into first and last name and normalized (e.g. ['abe', 'lincoln'])

    HINT: You don't need to a new loop for this function,
          you can just reuse functions you have already written.
    '''


def total_revenue(transactions):
    '''List[Transaction] -> Number

    transactions is a list of transactions from a retailer, where a transaction is a list shaped like this:
        [String, String, Number]
    The first String is the item name.
    The second String is the item category.
    The Number is the revenue generated by the transaction.
    For example:
        ['burrito', 'food', 3]

    Return the total revenue for all transactions.
    '''


def total_item_revenue(transactions, item):
    '''(List[Transaction], String) -> Number

    transactions is a list of transactions from a retailer, where a transaction is a list shaped like this:
        [String, String, Number]
    The first String is the item name.
    The second String is the item category.
    The Number is the revenue generated by the transaction.
    For example:
        ['burrito', 'food', 3]

    Return the total revenue for transactions of a particular item.
    '''


def total_category_revenue(transactions, category):
    '''(List[Transaction], String) -> Number

    transactions is a list of transactions from a retailer, where a transaction is a list shaped like this:
        [String, String, Number]
    The first String is the item name.
    The second String is the item category.
    The Number is the revenue generated by the transaction.
    For example:
        ['burrito', 'food', 3]

    Return the total revenue for transactions of a particular category.
    '''


def total_minutes_used(phone_calls):
    '''List[PhoneCall] -> Number

    phone_calls is a list of PhoneCalls, where a PhoneCall is a list shaped like:
        [String, String, Number]
    The first String is the phone number where the call originated (the dailer).
    The second String is the phone number where the call was received.
    The Number is the duration of the phone call in minutes.
    For example:
        ['(555)555-5555', '(222)222-2222', 17]

    Return the total minutes used for all phone calls
    '''


def total_number_minutes_used(phone_calls, number):
    '''(List[PhoneCall], String) -> Number

    phone_calls is a list of PhoneCalls, where a PhoneCall is a list shaped like:
        [String, String, Number]
    The first String is the phone number where the call originated (the dailer).
    The second String is the phone number where the call was received.
    The Number is the duration of the phone call in minutes.
    For example:
        ['(555)555-5555', '(222)222-2222', 17]

    Return the total minutes used by the provided number
    '''


def is_number_over_limit(phone_calls, number, limit):
    '''(List[PhoneCall], String, Number) -> Number

    phone_calls is a list of PhoneCalls, where a PhoneCall is a list shaped like:
        [String, String, Number]
    The first String is the phone number where the call originated (the dailer).
    The second String is the phone number where the call was received.
    The Number is the duration of the phone call in minutes.
    For example:
        ['(555)555-5555', '(222)222-2222', 17]

    Return whether or not the user has met or exceeded their limit.
    '''