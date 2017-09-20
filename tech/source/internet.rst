.. _internet :

Configuring Internet Forwarding
================================

Add internet forwarding
-----------------------

Turn on IP forwarding

.. code-block:: bash

   echo "1" | sudo tee /proc/sys/net/ipv4/ip_forward

Install the iptables-persistent package for saving the iptables rules

.. code-block:: bash

   sudo apt-get install iptables-persistent

Type this command to save the rules

.. code-block:: bash

   sudo iptables-save | sudo tee /etc/iptables/rules.v4



Online mode
-----------

In "online" mode, the MAZI toolkit forwards Internet traffic either from its Ethernet interface or from its external USB Wi-Fi Adapter or from its external OpenWRT router to the connected users.

Delete redirect in dnsmasq

.. code-block:: bash

  sudo sed -i '/address=\/#\/10.0.0.1/d' /etc/dnsmasq.conf 

Add a routing rule for forwarding internet

In case you want to forward traffic from ethernet

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE


If you want to forward traffic from external wifi dongle

.. code-block:: bash

   sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE

Restart dnsmasq

.. code-block:: bash

   sudo service dnsmasq restart

Offline mode
------------

In "offline" mode, the MAZI toolkit blocks Internet access to all its users and redirects every request to the MAZI Portal

Redirect in dnsmasq

.. code-block:: bash

   sudo sed -i '/#Redirect rule/a \address=\/#\/10.0.0.1' /etc/dnsmasq.conf


Block Internet traffic

.. code-block:: bash

   sudo iptables -A FORWARD -i wlan1 -j DROP
   sudo iptables -A FORWARD -i eth0 -j DROP


HTTP redirect rules

.. code-block:: bash

   sudo iptables -t mangle -N HTTP
   sudo iptables -t mangle -A PREROUTING -i wlan0 -p tcp -m tcp --dport 80 -j HTTP
   sudo iptables -t mangle -A HTTP -j MARK --set-mark 99
   sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp -m mark --mark 99 -m tcp --dport 80 -j DNAT --to-destination 10.0.0.1

HTTPS redirect rules

.. code-block:: bash

   sudo iptables -t mangle -N HTTPS
   sudo iptables -t mangle -A PREROUTING -i wlan0 -p tcp -m tcp --dport 443 -j HTTPS
   sudo iptables -t mangle -A HTTPS -j MARK --set-mark 98
   sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp -m mark --mark 98 -m tcp --dport 443 -j DNAT --to-destination 10.0.0.1


Restart dnsmasq

.. code-block:: bash

   sudo service dnsmasq restart

When you finish, please save the iptables rules with this command

.. code-block:: bash
   
   sudo iptables-save | sudo tee /etc/iptables/rules.v4

MAZI backend
------------

.. note::
   For the configuration of Internet Forwarding you can also use the MAZI backend script *mazi-internet.sh*. Check more info |here|.

.. |here| raw:: html

   <a href="https://github.com/mazi-project/back-end" target=_"blank">here</a>

Examples of mazi-internet.sh usage:

* Set the mode to offline

.. code-block:: bash

   sudo sh internet.sh -m offline

* Set the mode to online

.. code-block:: bash

   sudo sh internet.sh -m online


Start everything at boot
------------------------

Add the following lines of code to the rc.local file before exit 0

.. code-block:: bash

   sudo nano /etc/rc.local

The code which you will import to the rc.local file

.. code-block:: bash

   echo "1" | sudo tee /proc/sys/net/ipv4/ip_forward



