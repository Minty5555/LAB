#!/usr/bin/python3

"""
This is my first python script. This Script Greets, Scans, And Enumerates Systems. I hope you enjoy
"""


##This Section Holds Modules##
import time
from termcolor import colored
##############################




#This will locate the Dependency.py script and execute it
print(colored('Changing Into The Depend Directory. Checking Dependencies...', 'blue'))
import os
os.system("cd Depend ; python Dependencies.py")

print("\n")

print(colored('Warming Up Robot Scanner, This Process Wont Take Long.\n', 'blue'))
time.sleep(2)


#This will perform a network scan of all live hosts
print(colored('Robot Initialized Network Scanner', 'red'))
import os
os.system("ping -c 4 8.8.8.8")


print (" \n")


#This will find all files starting from the root directory that have the SUID bit set
print(colored('Robot Activating SUID Enumeration', 'red'))
import os
os.system("find / -type f -perm -u+s 2>/dev/null ")





