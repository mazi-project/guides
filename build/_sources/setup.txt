.. _setup :

Initial setup
=============

Plugging in your Raspberry Pi
-----------------------------

Before you plug anything into your Raspberry Pi, make sure that you have all the
equipment listed above to hand. Then follow these instructions:

1) Begin by slotting your SD card into the SD card slot on the Raspberry Pi, which will only fit one way.


2) Next, plug in your USB keyboard into the USB slots on the Raspberry Pi.


3) Make sure that your monitor or TV is turned on and that you have selected the right input (e.g. HDMI 1, DVI, etc).


4) Then connect your HDMI cable from your Raspberry Pi to your monitor or TV.


5) If you intend to connect your Raspberry Pi to the Internet, plug in an ethernet cable into the ethernet port next to the USB ports, otherwise skip this step.

6) When you are happy that you have plugged in all the cables and SD card required, finally plug in the micro USB power supply. This action will turn on and boot your Raspberry Pi.


Logging into your Raspberry Pi
------------------------------


Once your Raspberry Pi has completed the boot process, a login prompt will
appear. The default login for Raspbian is username **pi** with the password
**raspberry**. Note you will not see any writing appear when you type the
password. This is a security feature in Linux.

After you have successfully logged in, you will see the command line prompt
*pi@raspberrypi~$*


.. image:: ../_static/pi@.png



Rasbian configuration tool
--------------------------

Once you succesfully log in the Raspberry, start the rasbian configuration tool:

.. code-block:: bash
  
    sudo raspi-config

.. image:: ../_static/raspi-config.png


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
