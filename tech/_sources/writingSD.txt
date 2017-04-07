.. _writingSD :

Writing an image to the SD card
-------------------------------

**For Linux**

Please note that the use of the dd tool can overwrite any partition of your machine. If you specify the wrong device in the instructions below, you could delete your primary Linux partition. Please be careful.

1.Run 

.. code-block:: bash 

   df -h 

To see what devices are currently mounted. 

2.Insert the SD card and run **df -h** again. The new device that has appeared is your SD card. The left column gives the device name of your SD card. It will be listed as something like **/dev/mmcblk0p1** or **/dev/sdd1**. The last part (p1 or 1 respectively) is the partition number but you want to write to the whole SD card, not just one partition. You therefore need to remove that part from the name, getting, for example, **/dev/mmcblk0** or **/dev/sdd** as the device name for the whole SD card.

3.Now that you've noted what the device name is, you need to unmount it so that files can't be read or written to the SD card while you are copying over the SD image

4.Run 

.. code-block:: bash

  umount /dev/sdd1

Replacing sdd1 with whatever your SD card's device name is (including the partition number).

5.In the terminal, write the image to the card with the command below, making sure you replace the input file **if=** argument with the path to your .img file, and the /dev/sdd in the output file **of=** argument with the right device name. This is very important, as you will lose all data on the hard drive if you provide the wrong device name. Make sure the device name is the name of the whole SD card as described above, not just a partition of it. For example, **sdd**, not **sdds1** or **sddp1**, and **mmcblk0**, not **mmcblk0p1**

.. code-block:: bash
   
   sudo dd bs=4M if=2016-05-27-raspbian-jessie.img of=/dev/sdd

6.The **dd** command does not give any information of its progress and so may appear to have frozen.To see the progress of the copy operation you can run in another terminal

.. code-block:: bash

   sudo pkill -USR1 -n -x dd

**For Windows**


Download |win32| application for flashing the SD card

.. |win32| raw:: html

   <a href="http://sourceforge.net/projects/win32diskimager" target="_blank">Win32</a>

**1. Select your device (SD card)**
                      

.. image:: _static/photo1.png

**2. Locate the downloaded disk image**


.. image:: _static/photo2.png


**3. Click *Write* and wait for the write to be comleted**


.. image:: _static/photo3.png


As soon as the process is finished mount the SD card on the Raspberry Pi and turn it on.

