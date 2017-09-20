.. _setup :

Initial setup
=============

Plugging in your Raspberry Pi
-----------------------------

Before you plug anything into your Raspberry Pi, make sure that you have all the
equipment listed above to hand. Then follow these instructions:

1) Begin by slotting your microSD card into the microSD card slot on the Raspberry Pi, which will only fit one way.

2) Next, plug in your USB keyboard into the USB slots on the Raspberry Pi.

3) Make sure that your monitor or TV is turned on and that you have selected the right input (e.g. HDMI 1, DVI, etc).

4) Then connect your HDMI cable from your Raspberry Pi to your monitor or TV.

5) If you intend to connect your Raspberry Pi to the Internet, plug in an ethernet cable into the ethernet port next to the USB ports, otherwise skip this step.

6) When you are happy that you have plugged in all the cables and microSD card required, finally plug in the micro USB power supply. This action will turn on and boot your Raspberry Pi.


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


And make the following configurations:


**Re-size (expand) the file-system to use the entire SD card** 

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

