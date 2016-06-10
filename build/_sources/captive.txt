.. _captive : 



Configuration Captive Portal
============================


Firstly, you need to configure raspberry pi as access point :ref:`accessPoint`  


Configure dnsmasq
-----------------

.. code-block:: bash

  sudo nano /etc/dnsmasq.conf

Add the following line:

.. code-block:: bash

 address=/#/192.168.1.1 #redirect all DNS requests to 192.168.1.1

Your final dnsmasq configuration file should include the following:

.. code-block:: bash

 # MAZI configuration
 interface=wlan0
 dhcp-range=192.168.1.10,192.168.1.200,255.255.255.0,12h
 address=/#/192.168.1.1 #redirect all DNS requests to 192.168.1.1

Installing a web server
-----------------------

.. code-block:: bash

 sudo apt-get install apache2


Replace the placeholder page
----------------------------

Let’s browse to the /var/www/html directory and rename the default page:

.. code-block:: bash
  
   cd /var/www/html/
   mv index.html index.html.old

Now you can make a new folder and add your site in it.

Then you should make a new index.html file inside the folder /var/www/html for redirecting all requests to your site.

.. code-block:: bash

   mkdir your-new-page/
   sudo nano index.html

Paste the following

.. code-block:: html

 <html>
 	<head>
 		<meta HTTP-EQUIV="REFRESH" content="0; url=http://localhost/your-new-page">
 	</head>
 	<body>
 	</body>
 </html>


Restart apache web server

.. code-block:: bash

 sudo service apache2 restart
