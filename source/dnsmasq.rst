.. _dnsmasq :


Install DNSMASQ
===============



We have to configure the DHCP server

.. code-block:: bash

   sudo apt-get install dnsmasq


We set the range of the IPs that will be assigned to the clients

.. code-block:: bash

    sudo nano/etc/dnsmasq.conf

    # ADD THE FOLLOWING LINES
    interface=wlan0
    dhcp-range=192.168.1.10,192.168.1.200,255.255.255.0,12h
    address=/#/192.168.1.1    #redirect all DNS requests to 192.168.1.1


Edit the file Hosts

.. code-block:: bash

   sudo nano /etc/hosts

   #ADD THE FOLLOWING LINE AT THE BOTTOM
   192.168.1.1     mazizone


And type :

.. code-block:: bash

   sudo service hostapd start
   sudo service dnsmasq restart
   sudo reboot




