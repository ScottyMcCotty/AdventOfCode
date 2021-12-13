include ../Makefile.config

aoc.jar: LibraryClass1.java LibraryClass2.java
	$(JAVAC) *.java
	$(JAR) cf aoc.jar *.class

clean:
	$(RM) aoc.jar *.class
