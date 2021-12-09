import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys

#Verify we're getting input
if len(sys.argv) != 2:
    print('Missing day number. Run e.g:')
    print('python getter.py 13')
    sys.exit(2)

day = str(sys.argv[1])
path = str(os.getcwd()) + "/Day" + day
#Create folder from input
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)

#Create 4 empty files
# lista = ["/part2.py", "/test.py", "/testinput.txt"]
# for i in lista:
#     open(path + i, 'a').close()

#Create and Write to part1.py
# part1 = path + "/part1.py"
# f = open(part1, "a")
# f.write('data = open("input.txt").read().split("\\n")')
# f.close()

subprocess.run(["copy", "part1.java", "Day" + day], shell=True)

chrome_options = Options()
chrome_options.add_argument("--headless")

# Replace value with your session cookie for AoC
session_cookie = {"name": "session", "value": "53616c7465645f5ff57fc2becfee8e21fbad7b7b13c800ba673107193059e3b43f82f17bd27fe133487ff0b8e6eb405b"}
# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/Scott/Downloads/chromedriver_win32/chromedriver.exe")

# URLs we need
url = "https://adventofcode.com/2021/day/"
url_input = "https://adventofcode.com/2021/day/" + day + "/input"

# get request to target the site selenium is active on, add our cookies and go to input
driver.get(url)
driver.add_cookie(session_cookie)
driver.get(url_input)

# Find our text input on the input page, "pre" is our tag ID
content = driver.find_element_by_tag_name("pre").text

# Save content to file
path = path + "/input.txt"
f = open(path, "a")
for line in content:
    f.write(line)
f.close()
# Remember to quit the driver
driver.quit()

#Success?!
# print(str(path) + " and adjacent files created!")