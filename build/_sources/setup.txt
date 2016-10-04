.. _setup :

Setup
-----

Once you succesfully log in the Raspberry, start the rasbian configuration tool:

.. code-block:: bash
  
    sudo raspi-config

**Re-size to file-system to use the entire SD card** 

**Internationalisation option**

 1. Change the locale to match your location
 2. Change the timezone to match your location

**In the Advanced options**

 1. Enable the SSH server
 2. Change the hostname

Change the root password
------------------------

.. code-block:: bash

   sudo passwd

Change the password of the pi user
----------------------------------

.. code-block:: bash

	 passwd

Update repositories
-------------------

.. code-block:: bash

   sudo apt-get update

Assign a static ip address to wlan0
-----------------------------------

.. code-block:: bash

   sudo nano /etc/network/interfaces


set the following lines of code:

.. code-block:: bash

   # for Internet Connection Sharing
   
   auto wlan0  
   iface wlan0 inet static
      address 192.168.1.1
      netmask 255.255.255.0
      gateway 192.168.1.1
     


TP-LINK TL-WN725N model
-----------------------

In case your Wi-Fi USB dongle is the TP-Link tl-wn725n model, please follow these steps:  

Use command uname -a to find the kernel version

.. code-block:: bash
   
   sudo  uname -a

For example, for the Pi 2 B or 3 B, if uname -a shows **Linux raspberrypi 4.4.8-v7+ #881 SMP Sat Apr 30 12:16:50 BST 2016 armv7l GNU/Linux** the file to download is 8188eu-4.4.8-v7-881.tar.gz

Find the driver that corresponds to you, according to the model of kernel. |Here|

.. |Here| raw:: html

   <a href="https://www.raspberrypi.org/forums/viewtopic.php?t=62371" target="_blank">Here</a>

Download and install driver

.. code-block:: bash

   sudo wget https://dl.dropboxusercontent.com/u/80256631/8188eu-4.4.8-v7-881.tar.gz
   sudo tar xzf 8188eu-4.4.8-v7-881.tar.gz
   sudo ./install.sh
   sudo reboot

.. note::

   Replace the **80256631/8188eu-4.4.8-v7-881.tar.gz** with the appropriate file  to your own kernel
