.. _dnsmasq :


Install DNSMASQ server
======================



Install DNSMASQ server package
------------------------------

.. code-block:: bash

   sudo apt-get install dnsmasq

Setup the DNSMASQ server
------------------------

We set the range of the IPs that will be assigned to the clients

.. code-block:: bash

    sudo nano/etc/dnsmasq.conf

    # ADD THE FOLLOWING LINES
    interface=wlan0
    dhcp-range=192.168.1.10,192.168.1.200,255.255.255.0,12h
    


Edit the file Hosts

.. code-block:: bash

   sudo nano /etc/hosts

   #ADD THE FOLLOWING LINE AT THE BOTTOM
   192.168.1.1     mazizone


Restart the DNSMASQ server
--------------------------

.. code-block:: bash

   sudo service dnsmasq restart



Turn on IP forwarding
---------------------

.. code-block:: bash

   echo "1"| sudo tee /proc/sys/net/ipv4/ip_forward

Add a routing rule for forwarding internet
------------------------------------------

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE


