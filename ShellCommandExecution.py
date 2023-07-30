#!/usr/bin/python3

"""
This is my first python script. This Script Greets, Scans, And Enumerates Systems. I hope you enjoy test1234
"""


##This Section Holds Modules##
import time
from print_color import print
import os
##############################


#THESE LINES ARE ON THE BACK BURNER FOR NOW

#This will locate the Dependency.py script and execute it
#print(colored('Changing Into The Depend Directory. Checking Dependencies...', 'blue'))
#import os
#os.system("cd Depend ; python Dependencies.py")

#print("\n")

print("Warming Up Robot Scanner, This Process Wont Take Long.\n", color='blue')
time.sleep(2)


#This will perform a network scan of all live hosts
print("Robot Initialized Network Scanner", color='red')
os.system("ping -c 4 8.8.8.8")


print (" \n")


#This will find all files starting from the root directory that have the SUID bit set
print("Robot Activating SUID Enumeration", color='red')
os.system("find / -type f -perm -u+s 2>/dev/null ")





