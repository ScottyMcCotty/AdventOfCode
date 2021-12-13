
import sys

if len(sys.argv) != 3:
    print("makepart2.py needs one input file and one output file")
    sys.exit(2)


print("Reading from file '" + sys.argv[1] + "'")

# read the whole file into memory
with open(sys.argv[1], "r") as f:
    data = f.readlines()

search_string = "public class Part1"
new_string = "public class Part2"
new_data = []

# make the replacement
found = False
for line in data:
    if search_string in line:
        line = line.replace(search_string, new_string)
        found = True
    new_data += [line]

if not found:
    print("search string '" + search_string + "' not found in file... did you mean to do that?")
    sys.exit(2)

print("Writing to file '" + sys.argv[2] + "'")
# open the destination file
with open(sys.argv[2], "w") as f:

    for line in new_data:
        f.write(line)

