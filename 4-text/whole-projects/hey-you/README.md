# Hey You

Create a new file named `hey_you.py`.

Inside this file write a program that asks a user for
their name and then says hello.

`hey_you.py` should have a `main` function that is called
inside `if __name__ == '__main__':`.

You should have a test file `test_hey_you.py`. The test file should at least include 2 tests (one for each example).

#### Hint:

You will need to use `@with_inputs(...)` and `@should_print` to define your test cases.
Don't forget to import them from `bcca.test`.

## Examples

    $ python3 hey_you.py
    Hey, what is your name? Nate
    Hello, Nate.


    $ python3 hey_you.py
    Hey, what is your name? Sean
    Hello, Sean.
