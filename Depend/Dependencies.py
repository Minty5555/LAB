#!/usr/bin/python3

"""
This Will Install A Text Color Module For Python & pip
"""
##This Section Holds Modules##
import time
from termcolor import colored
##############################


print(colored('Installing pip Please Wait...', 'blue'))
time.sleep(2)
import os
os.system("sudo apt install python3-pip -y")

time.sleep(4)

print(colored('Installing Color Module Please Wait...', 'blue'))
time.sleep(2)
import os
os.system("pip install string-color")





