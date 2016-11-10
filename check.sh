#!/bin/bash



# Redirect output of this file to /var/log/syslog
exec 1> >(logger -s -t $(basename $0)) 2>&1

# Get connection variables from dnsmasq

# Operation, "add" or "del" or "old"
op="${1:-op}"

# MAC address
mac="${2:-mac}"

# IP address
ip="${3:-ip}"

# Hostname
hostname="${4}"

tstamp="`date '+%Y-%m-%d %H:%M:%S'`"

# Call block_user.py and online_user.py
sudo python /home/pi/mazi/block_user.py ${mac} ${ip} 
sudo python /home/pi/mazi/online_users.py




