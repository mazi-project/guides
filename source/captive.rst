.. _captive : 



Configuration Captive Portal
============================


Firstly, you need configure raspberry pi as access point :ref:`accessPoint`  

Install lighttpd
----------------

Lighttpd is a lightweight web server application that works well on the Pi. It can be installed using the following commands :



.. code-block:: bash

   sudo apt-get install lighttpd
   sudo apt-get install php5-common php5-cgi php5


Tweak Permission
----------------

Now we will adjust some permissions to ensure the “Pi” user account can write files to the location where Lighttpd expects to find web pages. The /var/www directory is currently owned by the “root” user. So let’s make the “www-data” user and group the owner of the /var/www directory

.. code-block:: bash

   sudo chown www-data:www-data /var/www
   sudo chmod 775 /var/www
   sudo usermod -a -G www-data pi

Enable fast CGI for the php

.. code-block:: bash
   
   sudo lighty-enable-mod fastcgi-php
   sudo servive lighttpd force-reload

Configuring Networking
----------------------

Edit the file Hostapd

.. code-block:: bash

   sudo nano /etc/default/hostapd
   #Uncomment the line 
       DEAMON_CONF=""
   #AND ADD
       /etc/hostapd/hostapd.conf


We have to configure the DHCP server

.. code-block:: bash

   sudo apt-get install dnsmasq

We set the range of the IPs that will be assigned to the clients

.. code-block:: bash
  
    sudo nano/etc/dnsmasq.conf
   
    # ADD THE FOLLOWING LINES
    interface=wlan0
    dhcp-range=192.168.1.1,192.168.1.200,255.255.255.0,12h
    address=/#/192.168.1.1    #redirect all DNS requests to 192.168.1.1


Edit the file Hosts

.. code-block:: bash

   sudo nano /etc/hosts

   #ADD THE FOLLOWING LINE AT THE BOTTOM
   192.168.1.1     eins 


And type :

.. code-block:: bash

   sudo service hostapd start
   sudo service dnsmasq restart
   sudo reboot 
   
Replace the placeholder page
----------------------------

Let’s browse to the /var/www directory and rename this default page :

.. code-block:: bash
  
   cd /var/www/html
   mv index.lighttpd.html index.lighttpd.hxxx

Now you can add you site or edit the index.html in /var/www/html

.. code-block:: bash

   wget /path of your page/
