#!/usr/bin/python3

#Import the socket module
import socket
 
try:
 
#Domain to be checked
    domain = "google.com"
 
#Getting the IP address of the domain
    ip = socket.gethostbyname(domain)
 
#Prints the IP address
    print(f"IP address: {ip}")
 
#Prints an error message, if an error occurs
except:
    print("An error occurred")
