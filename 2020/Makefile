CXXFLAGS = -g -std=c++14
default: runDay19

runDay19: day19
	./day19 < day19.example2.in

day19: day19.c++ aoc.o
	$(CXX) -o $@ $(CXXFLAGS) $< aoc.o

