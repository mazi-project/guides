.. _dhcpServer :

Install DHCP server
===================


.. code-block:: bash
 
   sudo apt-get install isc-dhcp-server

Setup the DHCP server
---------------------

.. code-block:: bash

   sudo nano /etc/dhcp/dhcpd.conf

add these lines of code:

.. code-block:: bash
   
   subnet 192.168.1.0 netmask 255.255.255.0 {
      range 192.168.1.10 192.168.1.200;
      option domain-name-servers 192.168.1.1;
      option routers 192.168.1.1;
      interface wlan0;
   }

Bring up the interface
----------------------

.. code-block:: bash

   sudo ifconfig wlan0 192.168.1.1

Restart the DHCP server
-----------------------

.. code-block:: bash

   sudo service isc-dhcp-server restart

Turn on IP forwarding
--------------------

.. code-block:: bash

   echo "1" > sudo /proc/sys/net/ipv4/ip_forward

Add a routing rule for forwarding internet
------------------------------------------

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

Configure isc-dhcp-server
-------------------------

.. code-block:: bash

   sudo nano /etc/default/isc-dhcp-server

1. uncomment the line DHCP_CONF=/etc/dhcp/dhcp.conf (remove the #)

.. code-block:: bash
   
    DHCP_CONF=/etc/dhcp/dhcp.conf    
    
2. fill in the interface wlan0, in the last line

.. code-block:: bash
   
    INTERFACES="wlan0"
