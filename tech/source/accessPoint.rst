.. _accessPoint :

Setting up a Wi-Fi Access Point
===========================

Setup a Wi-Fi Access Point in the Raspberry 
--------------------------------------------

Assign a static ip address to wlan0

.. code-block:: bash

   sudo nano /etc/network/interfaces


Set the following lines of code:

.. code-block:: bash

   # for Internet Connection Sharing

   auto wlan0
   iface wlan0 inet static
      address 10.0.0.1
      netmask 255.255.255.0
      gateway 10.0.0.1

Install dnsmasq server
----------------------
Dnsmasq provides network infrastructure for small networks: DNS, DHCP and network boot

Install dnsmasq server package

.. code-block:: bash

   sudo apt-get install dnsmasq


Setup the dnsmasq server
We set the range of the IPs that will be assigned to the clients

.. code-block:: bash

    sudo nano /etc/dnsmasq.conf

    # ADD THE FOLLOWING LINES
    interface=wlan0
    dhcp-range=10.0.0.10,10.0.0.200,255.255.255.0,12h


Edit the file Hosts

.. code-block:: bash

   sudo nano /etc/hosts

   #ADD THE FOLLOWING LINE AT THE BOTTOM
   10.0.0.1     mazizone


Restart the dnsmasq server

.. code-block:: bash

   sudo service dnsmasq restart

Install hostapd
---------------
Hostapd (Host access point daemon) is a user space software access point capable of turning normal network interface cards into access points and authentication servers.


Install hostapd package

.. code-block:: bash

   sudo apt-get install hostapd

Ιnitialize hostapd


.. code-block:: bash

   sudo nano /etc/hostapd/hostapd.conf

add these lines of code:

.. code-block:: bash

   interface=wlan0
   driver=nl80211
   ssid=THE_NAME_OF_YOUR_WIFI_NETWORK
   hw_mode=g
   channel=11
   wpa=1
   wpa_passphrase=SECRETPASSWORD
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP CCMP
   wpa_ptk_rekey=600
   macaddr_acl=0


.. note::

   In case you want a access point without password  add a # in front of all the lines starting with wpa


Start the access point by running hostapd

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -d /etc/hostapd/hostapd.conf


Or run hostapd in the background

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -B /etc/hostapd/hostapd.conf

.. note::
   In case the hostapd is not starting, you should bring down the wlan0 interface, then bring it up again and restart the dnsmasq server.

.. code-block:: bash

   sudo ifdown wlan0
   sudo ifup wlan0
   sudo service dnsmasq restart


.. note::
   For the configuration of the Wi-Fi Access Point you can also use the MAZI backend script *mazi-wifiap.sh*. Check more info |here|.

.. |here| raw:: html

   <a href="https://github.com/mazi-project/back-end" target=_"blank">here</a>


Add internet forwarding
-----------------------

Turn on IP forwarding

.. code-block:: bash

   echo "1" | sudo tee /proc/sys/net/ipv4/ip_forward

Add a routing rule for forwarding internet

In case you want to forward traffic from ethernet 

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE


If you want to forward traffic from external wifi dongle 

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE


Save the iptables rules

Install the iptables-persistent package

.. code-block:: bash

   sudo apt-get install iptables-persistent


Type this command to save the rules

.. code-block:: bash

   sudo iptables-save | sudo tee /etc/iptables/rules.v4

.. note::
   For the configuration of Internet Forwarding you can also use the MAZI backend script *mazi-.sh*. Check more info |here|.

.. |here| raw:: html

   <a href="https://github.com/mazi-project/back-end" target=_"blank">here</a>

Start everything at boot
------------------------

Add the following lines of code to the rc.local file before exit 0

.. code-block:: bash

   sudo nano /etc/rc.local


The code which you will import to the rc.local file 

.. code-block:: bash

   echo "1"| sudo tee /proc/sys/net/ipv4/ip_forward
   
   /sbin/ifconfig wlan0 10.0.0.1
   sudo ifdown wlan0
   sleep 1
   hostapd -B /etc/hostapd/hostapd.conf
   sudo ifconfig wlan0 10.0.0.1


