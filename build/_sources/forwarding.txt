.. _forwarding :


Turn on IP forwarding
---------------------

.. code-block:: bash
  
   echo "1" | sudo tee /proc/sys/net/ipv4/ip_forward

Add a routing rule for forwarding internet
------------------------------------------

If you want to forward traffic from ethernet

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

If you want to forward traffic from antenna

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE

 
Save the iptables rules
-----------------------

Install the iptables-persistent package

.. code-block:: bash
   
   sudo apt-get install iptables-persistent

Using this command to give you root user privileges 

.. code-block:: bash

   sudo su

Type this command to save the rules 

.. code-block:: bash

   iptables-save > /etc/iptables/rules.v4

