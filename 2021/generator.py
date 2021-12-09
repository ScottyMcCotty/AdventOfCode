

import subprocess
import sys

def mkdir(dir):

    subprocess.run(["mkdir", dir], shell=True)

def copy_self(dir):

    subprocess.run(["copy", "generator.py", dir], shell=True)
    
def copy_template(dir):

    subprocess.run(["copy", "part1.java", dir], shell=True)

# Can't get this shit to work on windows...
# def rename_template(dir = "."):
#     subprocess.run(["ren", "\"" + dir + "/template.java\"", "\"" + dir + "/part1.java\""], shell=True)

# GRRRRR
# def copy_rename_template(dir):
#     copy_template(dir)
#     rename_template(dir)

def make_input_files(dir):
    # make test.in and input.in
    with open(dir + "/test.in", "x") as f:
        # f.write("\n")
        # nothing to put in the file
        pass

    with open(dir + "/input.in", "x") as f:
        # f.write("\n")
        # nothing to put in the file
        pass


if __name__ == "__main__":

    if (len(sys.argv) > 1):
        print("Alright, let's do this")
    else:
        print("I can't do much without commandline arguments...")

    # print(len(sys.argv))

    for arg in sys.argv:
        # print("  " + arg)
        if arg == "generator.py":
            continue
        mkdir(arg)
        copy_template(arg)
        make_input_files(arg)

    # for ii in range(3, 10):
    #     directory_name = "Day" + str(ii)
    #     subprocess.call(["mkdir", directory_name], shell = True)

    # subprocess.call(["dir"], shell=True)
    # subprocess.call(["cd", "Day1"], shell=True)
    # subprocess.call(["dir"], shell=True)

    # make a sub directory below the current one
    # write the python file into the new directory
    # run the python file

    # subprocess.call(["mkdir", "subfolder"], shell=True)

    # with open("subfolder/test.py", "x") as f:
    #     # f.write("This is a test!\n")
    #     # f.write("Will it work?\n")

    #     # f.writelines(["This is a test!\n",
    #     #               "Will it work?\n"])

    #     f.writelines(["\n",
    #                   "import subprocess\n",
    #                   "\n",
    #                   "print(\"Alright, let's do this\")\n",
    #                   "\n",
    #                   "subprocess.call([\"mkdir\", \"subfolder\"], shell=True\n",
    #                   "\n",
    #                   "with open(\"subfolder/test.py\", \"x\") as f:\n",
    #                   "\n",

    #                   ])

    # subprocess.call(["copy", "generator.py", "subfolder"], shell=True)

    # subprocess.call(["python", "subfolder/generator.py"], shell=True)
    
    # subprocess.call(["python", "subfolder/test.py"], shell=True)

