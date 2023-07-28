#!/usr/bin/python3

"""
This Will Install pip & print-color
"""

##This Section Holds Modules##
import time
##############################

#This Will Install pip
print("Installing pip Please Wait...")
time.sleep(2)
import os
os.system("sudo apt install python3-pip -y")

print("\n")

#This Will Install Print-Color
print("Installing Python Colored Please Wait...")
time.sleep(2)
import os
os.system("pip3 install print-color")





