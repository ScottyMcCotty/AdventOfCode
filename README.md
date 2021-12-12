
# README

My Advent of Code repository where I attempt to solve the daily puzzles.

## Setting up 2021

In your 2021 directory, put your session cookie in `local.properties`:

    session = 53616c74...

Then you can set up a day's code and fetch its input:

    python getter.py 1

That should create a `Day1` directory with various files:

    Day1/
        input.txt
        Makefile
        Part1.java
        Part2.java

Changing to that directory, and running `make part1`, should build and run the
`Part1` class using `input.txt`; `make test` should build and run the `Part1`
class using `test.txt` (which won't exist unless you create it).
