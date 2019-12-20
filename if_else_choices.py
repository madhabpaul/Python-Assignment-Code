#!/usr/bin/python3
import subprocess
import os
import sys
import webbrowser
import time
import pyspeedtest
options="""
Press  1  to start your default web browser :- 
Press  2  to check your internet connection speed :- 
Press  3  to check your internet status  :- 
Press  4  to check current date and  time:- 
Press  5  to check current temperature in your city :- 
Press  6  to check current public IP :- 
Press  7  to create  a directory in your OS :- 
Press  8  to reboot your system :- 
Press  9  to play song in you tube  :- 
Press  10 to search something in google search engine  :- 
"""
print(options)
#  to accept input from user
choice=input("Enter your choice :")
#  input  function will accept in string form only
print("You have enter "+choice)
#  conditional statements
if choice == '1' :
	print("Opening browser plzz wait ...")
	time.sleep(2)
	webbrowser.open_new("https://www.google.com") #it will open default browser
elif choice =='2' :
	st = pyspeedtest.SpeedTest("www.google.com")
	print("Your ping",st.ping())
	print("Your download speed",st.download())
	print("Your upload speed",st.upload())
elif choice =='3' :
	output=subprocess.getstatusoutput('ping -c 2 8.8.8.8')
	if output[0] == 0:
		print("Internet is working")
	else:
		print("Internet is not working")
elif choice =='4'  :
	print("current time is ",subprocess.getoutput("date +%T"))
elif choice =='7' :
	dir_name=input("Enter directory name")
	dir_output=subprocess.getstatusoutput("mkdir "+dir_name)
	if dir_output[0] == 0:
		print("Your directory"+dir_name+" successfully created")
	else :
		print("Please choose another directory name")
elif choice == '8':
	restart = input("Do you wish to resboot your computer ? (y / n): ") 
	if restart == 'n': 
		exit() 
	else: 
		print("Rebooting....")
		time.sleep(2)
		os.system("shutdown /r /t 1") 
elif choice == '10' :
	search = input("Enter Keywords ")
	webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(search))
else :
	print("wrong option")
