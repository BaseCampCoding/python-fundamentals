def print_all(l):
    '''List -> None

    Prints each item from l.
    '''


def double_all(l):
    '''List -> None

    Doubles each element in l
    '''

def doubled_list(l):
    '''List -> List

    Returns a new list with doubled values from l.
    l should not be mutated.
    '''


def print_with_numbers(l):
    '''List -> None

    Prints the contents of l with #. beside it.
    '''


def reversed_list(l):
    '''List -> List

    Returns a reversed version of l.
    l should not be mutated.
    '''

def students_per_class(classes):
    '''List[List] -> List[Int]

    Returns a list of the number of students in each class.
    '''


def print_steps(n):
    '''Int -> None

    Prints "steps" n steps tall and wide.
    Use an M for the steps character.
    '''


def bar_chart(widths):
    '''List[Int] -> None

    Print out the bar chart described by widths.
    Each element in widths is the number of characters that should be printed in its bar.
    Use M for the bar chart character.
    '''


def labelled_bar_chart(labelled_widths):
    '''List[List] -> None

    Print out the labelled bar chart described by labelled_widths.
    Elements of labelled_widths are lists with 2 items: the label, and the width.
    The label should be printed to the right of its bar.
    Use M for the bar chart character.
    '''


def what_should_i_buy(ingredient_list, pantry_list):
    '''(List, List) -> List

    Return the list of items that need to be purchased.
    ingredient_list contains all the items needed.
    pantry_list contains all the items already owned.
    Whatever is ingredient list, but not the pantry list, needs to be purchased.
    '''


def exercise_report(results):
    '''List[List] -> None

    Print an exercise report to the user.
    The report should tell the user which problems were answered incorrectly.

    Each element in results is a result for a single problem in the exercise.
    The first element in the problem result is the name of the exercise.
    The second element in the problem result is True if the student correctly completed the exercise,
    otherwise it is False.
    '''


def decode_message(indicies, letters):
    '''(List[Int], List[String]) -> String

    Decode the message described by indicies and letters.

    Indicies is a list of indicies into the list letters.
    Letters is all the letters required to reconstruct the message.

    Use each index in indicies to find the correct character in letters.
    Return the decoded message.

    For example, using the following arguments:
        indicies as [2, 1, 0]
        letters as ['y', 'e', 'H']
    The message would be
        indicies[0] | indicies[1] | indicies[2]
             2      |      1      |     0
         letters[2] | letters[1]  | letters[0]
    '''
    
