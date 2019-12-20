#!/usr/bin/python3
import subprocess, time, webbrowser ,os, sys
l1=[1,7,99,5]
dynamic_input=sys.argv[1:]
sum=0
for i  in dynamic_input:
        sum=sum+int(i)
        print("element",i,"id added")
print(sum)
'''
for i dir(sys):
        if 'ar' in i :
                print(i)
[i for i in dir(sys) if 'ar' in i ]
'''        
