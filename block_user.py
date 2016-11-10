#!/usr/bin/python

#Block internet access

import sys
import os
import commands

path = "/home/pi/mazi/"

# MAC
mac = sys.argv[1]

# IP
ip = sys.argv[2]

#Date
date = commands.getoutput("date | cut -d ' ' -f2-5")

#Search the file ipmac.txt to check out if already exist user with specific MAC
exist_mac = commands.getoutput("cat '%s'ipmac.txt | grep '%s' | cut -d ' ' -f2"  % (path, mac))

#Information (IP MAC) 
info = ip + ' ' + mac

#Information (DATE MAC)
users = date + ' '  + mac

if mac != '' and mac != exist_mac  :

    #Block internet access for user with specific MAC
    os.system("sudo iptables -A FORWARD -i wlan1 -m mac --mac-source '%s' -j DROP" % mac)
    #Redirect user to index.html MAZIplayground   
    os.system("sudo iptables -t nat -A PREROUTING -p tcp -m tcp --dport 80 -m mac --mac-source '%s' -j DNAT --to-destination 192.168.1.1" % mac)
    #Save iptables 
    os.system("sudo iptables-save > /etc/iptables/rules.v4")
    #Create file ipmac.txt wtih information (IP MAC)
    os.system("sudo echo '%s' >> '%s'ipmac.txt" % (info, path))
    #Create file history.txt wtih information (DATE MAC) 
    os.system("sudo echo '%s' >> '%s'history.txt" %(users, path))
    print "Block user with '%s' IP and '%s' MAC" % (ip, mac)

else:
    print"It's already blocked"

