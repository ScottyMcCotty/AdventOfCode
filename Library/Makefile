include ../Makefile.config

aoc.jar: *.java
	$(JAVAC) *.java
	$(JAR) cf aoc.jar *.class

clean:
	$(RM) aoc.jar *.class
