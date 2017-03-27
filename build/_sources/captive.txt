.. _captive : 



Configuration Captive Portal
============================


Firstly, you need to configure raspberry pi as access point :ref:`accessPoint`.


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


Redirecting every “unknown user” HTTP/HTTPS traffic to the "index" portal
-------------------------------------------------------------------------

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

When you finish, please save the iptables rules with this command

.. code-block:: bash
   
   sudo iptables-save | sudo tee /etc/iptables/rules.v4


Redirect all to index.html via htaccess file
--------------------------------------------

Enable and load mod_rewrite   

.. code-block:: bash

   sudo a2enmod rewrite

Then open up the following file, and replace  "AllowOverride None" with "AllowOverride all"

.. code-block:: bash

   sudo nano /etc/apache2/apache2.conf

Restart apache web server

.. code-block:: bash

 sudo service apache2 restart

Finally, create a secret file .htaccess and import the following lines of code 

.. code-block:: bash

  sudo nano /var/www/html/.htaccess

Add the follow code 

.. code-block:: bash

  RewriteEngine on 
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_FILENAME} !-f 
  RewriteRule . index.html [L]
 
