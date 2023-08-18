#!/usr/bin/python3

#Import the OS module
import os
 
#The shell command to run
command = "whoami; grep gigith /etc/passwd"
 
try:
 
#Runs the system command
    result = os.system(command)
 
#Prints the result of the command
    print(result)
 
#Prints an error message, in case an error occurs
except:
    print("An error occurred")
