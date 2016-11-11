.. _dns :

**Install resolvconf package**

.. code-block:: bash

   sudo apt-get install resolvconf

Then edit (with root permissions) either /etc/resolvconf/resolv.conf.d/head or /etc/resolvconf/resolv.conf.d/tail 

.. code-block:: bash 

   sudo nano /etc/resolvconf/resolv.conf.d/head
   or
   sudo nano /etc/resolvconf/resolv.conf.d/tail

Add the following lines 

.. code-block:: bash
   
   nameserver 8.8.8.8
   nameserver 8.8.4.4

And then run resolvconf -u to update the file

.. code-block:: bash

    sudo resolvconf -u
