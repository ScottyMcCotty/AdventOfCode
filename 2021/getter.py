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

    # copy in the template files
    copyfile("Makefile.in", path + "/Makefile")
    copyfile("Part1.java.in", path + "/Part1.java")

    properties = {}

    # read the key from local.properties
    with open("local.properties", "r") as f:
        data = f.readlines()

        for line in data:
            if line.strip()[0] == "#":
                # it's a comment line, so skip it
                continue
            split = line.split("=", 1)
            properties[ split[0].strip() ] = split[1].strip()
    
    if "session" not in properties:
        print('Your local.properties file needs a session key. Example:\n"session = 123456789ABC"')
        exit(1)
        
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

