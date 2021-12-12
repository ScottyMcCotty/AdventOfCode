import subprocess
import os, sys
from shutil import copyfile

def setup(day):

    path = "Day" + day

    #Create folder from input
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
        print("Directory may already exist... or something else is wrong")
        return

    #Create 4 empty files
    # lista = ["/part2.py", "/test.py", "/testinput.txt"]
    # for i in lista:
    #     open(path + i, 'a').close()

    #Create and Write to part1.py
    # part1 = path + "/part1.py"
    # f = open(part1, "a")
    # f.write('data = open("input.txt").read().split("\\n")')
    # f.close()

    # this might be OS specific, hopefully it works
    # subprocess.run(["copy", "part1.java", "Day" + day], shell=True)
    copyfile("Makefile.in", path + "/Makefile")
    copyfile("Part1.java.in", path + "/Part1.java")
    copyfile("Part2.java.in", path + "/Part2.java")

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    properties = {}

    # read the key from local.properties
    with open("local.properties", "r") as f:
        data = f.readlines()
        for line in data:
            split = line.split(" = ")
            properties[ split[0] ] = split[1]
        
    # print(properties)

    # url for where the input file is
    url_input = "https://adventofcode.com/2021/day/" + day + "/input"
    
    subprocess.run(["curl", "-b", properties["session"], "-o", path + "/input.txt", url_input]) #, shell=True)

    #Success?!
    print(str(path) + " and adjacent files created!")


if __name__ == "__main__":
    #Verify we're getting input
    if len(sys.argv) == 1:
        print('Run with at least one day number')
        sys.exit(2)
    
    # run through each specified day and run setup
    for ii, day in enumerate(sys.argv):

        # skip first argument, which is file name
        if ii == 0:
            continue
        
        # run setup
        setup(day)

