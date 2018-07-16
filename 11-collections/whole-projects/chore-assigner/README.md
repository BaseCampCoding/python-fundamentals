# Chore Assigner

Write a program to automate assigning and reporting chores for base camp students.

This application has 3 main features:

-   Weekly random assignment of chores
-   Remembering what students were assigned what chores
-   Allowing students to report that they finished their chore for the week
-   Report who hasn't finished their chore

## Weekly random assignment

Every week, students are assigned new chores.
Your program should not more than once a week.
This means your program will need to know two things:

-   What week is it?
-   Have I assigned chores already this week?

### What week is it?

Python's standard library has a module for dealing with dates and times.
Look at the documentation for the `datetime` module (particularly the `date` class).

### Have I assigned chores already this week?

If you want to remember information, you need to write it to a file.
You will need to figure out a scheme for reading and writing down
chore assignments. **Don't forget to include the date they are being assigned!**

### Examples

    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 1
    Assigning Chores ...
    Student 1 => Bathroom 2
    Student 2 => Bathroom 1
    Student 3 => Classroom Windows
    ...


    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 1
    Chores already assigned for this week.
    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    ->

## Remembering what students were assigned what chores

Again, this is about your requirement to read and write to the file system.

### Example

    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 2
    Student 1 => Bathroom 2
    Student 2 => Bathroom 1
    Student 3 => Classroom Windows
    ...

## Allowing students to report that they finished their chore for the week

Your program should not only remember the assignments, but it should remember
whether or not someone has completed their chore yet. If they haven't completed
it yet, they should be allowed to report that they completed their chore.

### Example

    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 3
    Your name: Nate
    Clean Kitchen has been marked finished.
    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 3
    Your name: Nate
    You already finished your chore.

## Report who hasn't finished their chore

With all of this data in place, the program should be able to report who hasn't
finished their chore yet.

### Example

    What would you like to do:
    1. assign chores
    2. view chore assignments
    3. report a finished chore
    4. view unfinished chores
    5. quit
    -> 4
    Unfinished Chores:
    Student 1 => Bathroom 2
    Student 3 => Classroom Windows
    ...
