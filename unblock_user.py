#!/usr/bin/python

import sys
import os
import commands

path = "/home/pi/mazi/"

ip = sys.argv[1]

#Get MAC address from  ipmac.txt
mac = commands.getoutput("cat '%s'ipmac.txt |grep '%s' |cut -d ' ' -f2" % (path, ip))



if mac != '':
    #Cancel iptables rules for user with specific MAC
    os.system("sudo iptables -D FORWARD -i wlan1 -m mac --mac-source '%s' -j DROP" % mac)
    os.system("sudo iptables -t nat -D PREROUTING -p tcp -m tcp --dport 80 -m mac --mac-source '%s' -j DNAT --to-destination 192.168.1.1" % mac)

    #Delete user (IP MAC)  from  ipmac.txt
    os.system("sudo sed -i /'%s'/d ./ipmac.txt" % mac)


    #Seve iptables 
    os.system("sudo iptables-save | sudo tee /home/pi/etc/iptables/rules.v4 > '%s'rulesv4.log" % path)
    print "Unblock user with '%s' IP and '%s' MAC" % (ip, mac)









