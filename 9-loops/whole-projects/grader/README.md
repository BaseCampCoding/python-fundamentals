# Grader (Part 1)

This program asks the user for a series of grades.
Once the user enters all their grades, the program shows the user their final grade.

Create a new file `grader.py`.

`grader.py` should have a `main` function that is called
inside `if __name__ == '__main__':`.

You should have a test file `test_grader.py`. The test file should at least include 2 tests (one for each example).

#### Hint:

You will need to use `@with_inputs(...)` and `@should_print` to define your test cases.
Don't forget to import them from `bcca.test`.

## Examples

    $ python3 grader.py
    Enter your grades. Enter "grade" when you are finished.
    Grade #1: 100
    Grade #2: 97
    Grade #3: 92
    Grade #4: 82
    Grade #5: 93
    Grade #6: grade
    You averaged 92.8 and received an A.

    $ python3 grader.py
    Enter your grades. Enter "grade" when you are finished.
    Grade #1: 86
    Grade #2: 92
    Grade #3: 80
    Grade #4: grade
    You averaged 86.0 and received an B.

# Grader (Part 2)

Now that you have a working grader, your job is to change your program to allow for dropped grades.

Before you start collecting grades, you will ask the user how many grades should be dropped.

**Validate the users input.** You can't drop `-3` grades. Also, you can't drop all of your grades.

## Example

    $ python3 grader.py
    How many grades will get dropped: 0
    Enter your grades. Enter "grade" when you are finished.
    Grade #1: 100
    Grade #2: 97
    Grade #3: 92
    Grade #4: 82
    Grade #5: 93
    Grade #6: grade
    You averaged 92.8 and received an A.

    $ python3 grader.py
    How many grades will get dropped: 1
    Enter your grades. Enter "grade" when you are finished.
    Grade #1: 86
    Grade #2: 92
    Grade #3: 80
    Grade #4: grade
    You averaged 89.0 and received an B.

## First step

**Before** changing `grader.py` update your test cases.
