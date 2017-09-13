.. _wifi-setup

Setup the Wi-Fi Access Point
========================

Assign a static ip address to wlan0
-----------------------------------

.. code-block:: bash

   sudo nano /etc/network/interfaces


set the following lines of code:

.. code-block:: bash

   # for Internet Connection Sharing

   auto wlan0
   iface wlan0 inet static
      address 10.0.0.1
      netmask 255.255.255.0
      gateway 10.0.0.1

