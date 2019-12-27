#!/usr/bin/python3

import sys
#pass file name as argument
file_names=sys.argv[1:]
for  i  in  file_names:
    f=open(i,'r')
    print(f.read())