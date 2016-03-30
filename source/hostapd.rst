.. _hostapd :


Install hostapd
===============

Install hostapd package
----------------------

.. code-block:: bash

   sudo apt-get install hostapd


Ιnitialize hostapd
-------------------

.. code-block:: bash

   sudo nano /etc/hostapd/hostapd.conf

add these lines of code:

.. code-block:: bash

   interface=wlan0
   driver=nl80211
   ssid=THE_NAME_OF_YOUR_WIFI_NETWORK
   hw_mode=g
   chanel=11
   wpa=1
   wpa_passphrase=SECRETPASSWORD
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP CCMP
   wpa_ptk_rekey=600
   macaddr_acl=0

.. note::
   
   In case your Wi-Fi USB dongle is the TP-Link tl-wn725n model, please go to the following section. If not, please skip the following section (TP-LINK TL-WN725N)

	 
Only for the TP-LINK TL-WN725N model
------------------------------------
		
follow these steps:

.. code-block:: bash

   sudo wget https://dl.dropboxusercontent.com/u/80256631/8188eu-20160219.tar.gz
   sudo tar xzf 8188eu-20160219.tar.gz 
   sudo ./install.sh
   sudo reboot 
   


Start the access point by running hostapd
-----------------------------------------

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -d /etc/hostapd/hostapd.conf

Run hostapd in the background
-----------------------------

.. code-block:: bash

   sudo ifdown wlan0
   sudo hostapd -B /etc/hostapd/hostapd.conf

.. note::
   In case the hostapd cannot start, you should bring down the wlan0 interface, then bring it up again and restart the isc –serserver.

.. code-block:: bash
   
   sudo ifdown wlan0
   sudo ifup wlan0
   sudo service isc-dhcp-server restart
