#!/usr/bin/python3

"""
This is my first python script. This Script Greets, Scans, And Enumerates Systems. I hope you enjoy
"""
from stringcolor import *

print("Warming Up Robot Scanner, This Process Wont Take Long.\n")

print(cs("Robot Initialized Network Scanner", "red"))
import os
os.system("ping -c 4 8.8.8.8")

print (" \n")

print(cs("Robot Activating SUID Enumeration", "red"))
import os
os.system("find / -type f -perm -u+s 2>/dev/null ")





