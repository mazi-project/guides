.. _hostapd :


Install hostapd
===============

Install hostapd package
-----------------------

.. code-block:: bash

   sudo apt-get install hostapd


Ιnitialize hostapd
------------------

.. code-block:: bash

   sudo nano /etc/hostapd/hostapd.conf

add these lines of code:

.. code-block:: bash

   interface=wlan0
   driver=nl80211
   ssid=YOUR-WIFI-NETWORK
   hw_mode=g
   channel=11
   wpa=1                               
   wpa_passphrase=SECRETPASSWORD  
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP CCMP
   wpa_ptk_rekey=600
   macaddr_acl=0   

.. note::
   
   In case you want a access point without password  add a # in front of the line with wpa



Start the access point by running hostapd
-----------------------------------------

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -d /etc/hostapd/hostapd.conf

Or run hostapd in the background
--------------------------------

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -B /etc/hostapd/hostapd.conf

.. note::
   In case the hostapd cannot start, you should bring down the wlan0 interface, then bring it up again and restart the dnsmasq server.

.. code-block:: bash
   
   sudo ifdown wlan0
   sudo ifup wlan0
   sudo service dnsmasq restart
