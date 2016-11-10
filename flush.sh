#!/bin/bash

path="/home/pi/mazi/"

#Delete iptables rules
sudo iptables -F
sudo iptables -F -t nat

#Add a routing rules for forwarding internet
echo "1"| sudo tee /proc/sys/net/ipv4/ip_forward
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE

#Save rules.v4 without iptables rules 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 

#Remove files with information of users
sudo rm ${path}ipmac.txt
sudo rm ${path}history.txt
sudo rm ${path}online.txt






