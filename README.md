
# README

My Advent of Code repository where I attempt to solve the daily puzzles.

## Setting up 2021

In your 2021 directory, put your session cookie in `local.properties`:

    session = 53616c74...

And, uhh... super lame, but create a `Makefile.config` depending on your
platform.  For DOS:

    #  DOS
    JAVA = java
    JAVAC = javac
    PYTHON = python3
    RM = del
    CP = copy

or Unix:

    JAVA = java
    JAVAC = javac
    PYTHON = python3
    RM = rm
    CP = cp

Then you can set up a day's code and fetch its input:

    python getter.py 1

That should create a `Day1` directory with various files:

    Day1/
        input.txt
        Makefile
        Part1.java

In that directory:
- `make test1` should build and run the `Part1` class using `test.txt` (which
  won't exist unless you create it).
- `make part1` should build and run the `Part1` class using `input.txt`.
- `make test2` should build and run the `Part2` class using `test.txt`
- `make part2` should build and run the `Part2` class using `input.txt`.

`Part2.java` will be copied from `Part1.java` the first time you run
`make test2` or `make part2`.