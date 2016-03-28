.. _boot :


Configuration 
==============

.. code-block:: bash

   sudo nano /etc/rc.local

Add the following lines before exit 0

.. code-block:: bash
   
   /sbin/ifconfig wlan0 192.168.1.1
   service isc-dhcp-server start
   sudo ifdown wlan0
   sleep 1
   hostapd -B /etc/hostapd/hostapd.conf
   sudo ifconfig wlan0 192.168.1.1
   exit 0   
