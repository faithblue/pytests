"""
    This is the hello world program in python
"""
import sys

# print the version of python you are running, it should be 3.x
print()
print("Version is: ", sys.version)
print()

#ask for input
message = input("Enter your message: ")
# print hello world
print("MOTD: " , str(message))
