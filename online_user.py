#!/usr/bin/python
import os
import commands

path ="/home/pi/mazi/"

#Date
date = commands.getoutput("date | cut -d ' ' -f2-3 ")

print date
#collected from file history.txt the number of users who have this date
users  = commands.getoutput("grep -w '%s' -c '%s'history.txt" %(date, path))

print users
#Store this number in file online.txt
os.system("sudo echo '%s' > '%s'online.txt" %(users, path))


