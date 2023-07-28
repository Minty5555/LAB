#!/usr/bin/python3

"""
This Will Install pip
"""
##This Section Holds Modules##
import time
from termcolor import colored
##############################


print(colored('Installing pip Please Wait...', 'blue'))
time.sleep(2)
import os
os.system("sudo apt install python3-pip -y")





