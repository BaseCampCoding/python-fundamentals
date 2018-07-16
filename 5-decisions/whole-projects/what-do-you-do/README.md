# What do you do

Write a program that asks a user for a person's name, and then tells the user what that person does at Base Camp Coding Academy. Look at https://basecampcodingacademy.org/contact for information.

Create a new file `what_do_you_do.py`.

`what_do_you_do.py` should have a `main` function that is called
inside `if __name__ == '__main__':`.

You should have a test file `test_what_do_you_do.py`. The test file should at least include 6 tests (one for each example).

#### Hint:

You will need to use `@with_inputs(...)` and `@should_print` to define your test cases.
Don't forget to import them from `bcca.test`.

# Examples

    $ python3 what_do_you_do.py
    Name: Nate Clark
    Technical Director

    $ python3 what_do_you_do.py
    Name: Sean Anthony
    Director

    $ python3 what_do_you_do.py
    Name: Kagan Coughlin
    Co-Founder

    $ python3 what_do_you_do.py
    Name: Carla Lewis
    Trustee

    $ python3 what_do_you_do.py
    Name: Martin Guzman
    Graduated 2017

    $ python3 what_do_you_do.py
    Name: Irma Patton
    Current Student
