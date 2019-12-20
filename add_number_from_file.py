#!/usr/bin/python3
file = open("/home/madhab/Desktop/Python-Assignment-Code/number.txt", "r") #location of the file 

line = file.read()

line.split(",")

print (line.split(","))

total = sum([int(num) for num in line.split(',')])

print(total)