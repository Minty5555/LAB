#!/usr/bin/python3

"""
This is my first python script. This Script Greets, Scans, And Enumerates Systems. I hope you enjoy
"""

##This Section Holds Modules##
from stringcolor import *
import time
##############################


print(cs("Changing Into The Depend Directory. Checking Dependencies...", "blue"))
import os
os.system("cd Depend ; python Dependencies.py")

print("\n")

print(cs("Warming Up Robot Scanner, This Process Wont Take Long.\n","blue"))
time.sleep(2)


print(cs("Robot Initialized Network Scanner", "red"))
import os
os.system("ping -c 4 8.8.8.8")


print (" \n")


print(cs("Robot Activating SUID Enumeration", "red"))
import os
os.system("find / -type f -perm -u+s 2>/dev/null ")





