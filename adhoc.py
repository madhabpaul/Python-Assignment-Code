#!/usr.bin/python3


import time

def clear():
    print("\n"*50)

def sum(*x):
   add=0
   for i in x:
    add=add+i
    print(add)

def motd():
    print("The time is")