.. _boot :


Configuration 
==============

.. code-block:: bash

   sudo nano /etc/rc.local

Add the following lines before exit 0

.. code-block:: bash
   
   echo "1"| sudo tee /proc/sys/net/ipv4/ip_forward
   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  

   /sbin/ifconfig wlan0 10.0.0.1
   sudo ifdown wlan0
   sleep 1
   hostapd -B /etc/hostapd/hostapd.conf
   sudo ifconfig wlan0 10.0.0.1
   exit 0   
