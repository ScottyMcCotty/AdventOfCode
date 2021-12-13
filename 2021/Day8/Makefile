#  Part1.java - the code for running part 1 of the challenge
#  Part2.java - the code for running part 2 of the challenge
#  test.txt - test input for both parts
#  input.txt - real input for both parts

JAVA = java
JAVAC = javac

test1: Part1.class FORCE
	$(JAVA) Part1 test.txt
test2: Part2.class FORCE
	$(JAVA) Part2 test.txt

part1: Part1.class FORCE
	$(JAVA) Part1 input.txt
part2: Part2.class FORCE
	$(JAVA) Part2 input.txt

Part1.class: Part1.java
	$(JAVAC) Part1.java
Part2.class: Part2.java
	$(JAVAC) Part2.java

clean:
	rm *.class
FORCE:
