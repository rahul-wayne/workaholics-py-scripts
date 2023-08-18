#!/usr/bin/python3
#Import the OS module
import os
 
try:
 
#Gets the name of the current user
    user = os.getlogin()
 
#Prints the name of the current user
    print(user)
 
#Prints an error message, in case it occurs
except:
    print("An error occurred")
