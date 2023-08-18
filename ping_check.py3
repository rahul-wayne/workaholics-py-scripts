#!/usr/bin/python3

import os

########################
# This script will check the status of various websites
# This could be used to verify your internet connection
# or to check if your internal servers are functioning.
#######################

vmlist = input("enter file name containing IP list:")
def ping(mysite):
    myping = ("ping -q -c 1 %s > /dev/null" % mysite)
    status = os.system(myping)
    return(status)

with open(vmlist) as file:
    mysites = file.readlines()

for site in mysites:
    mystatus = ping(site.strip())
    if mystatus == 0:
   	 print(site.strip() + " is fine")
    if mystatus != 0:
   	 print("%s is down!" % (site.strip()))
    print("-----------")
