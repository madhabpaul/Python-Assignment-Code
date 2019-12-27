#!/usr/bin/python3
import os
path = os.getcwd()
dirlist = os.listdir(path)
for i in dirlist:
    print(i)