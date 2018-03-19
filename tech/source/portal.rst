.. _portal :

MAZI Portal
============

The MAZI Portal is the software interface of the MAZI toolkit and comprises of the User page and the Administration Panel.

* User Page (demo.mazizone.eu): Through the User Page the user of the MAZI Zone is able to access the available applications, as well as useful statistics
* Administration Panel (demo.mazizone.eu:4567/admin): Through the Administration Panel the admin of the MAZI Zone is able to make all the configurations of the MAZI node

After following all the above sections for setting up the networking components of the toolkit, you can install the MAZI Portal following the instructions of this section.

Install MAZI Portal
-------------------

Install the following packages:

.. code-block:: bash

   apt-get update
   apt-get install build-essential git-core libsqlite3-dev ruby ruby-dev libmysqlclient-dev


.. note::
   For debian stretch (instead of jessie) replace in the command above "libmysqlclient-dev" with "default-libmysqlclient-dev".

Also install the following gems:

.. code-block:: bash

   gem install sinatra sequel sqlite3 rake thin rubyzip mysql --no-ri --no-rdoc

Make sure you have cloned the MAZI backend repository (:ref:`backend`).

Installation
------------

.. code-block:: bash

   sudo su
   cd /root
   git clone https://github.com/mazi-project/portal.git
   cd portal
   rake init
   rake db:migrate
   cp init/mazi-portal /etc/init.d/mazi-portal
   update-rc.d mazi-portal enable

Execution
---------

.. code-block:: bash

   service mazi-portal start

Update
-------

Since version 1.6.4 there is an update button in the Administration Panel. It is **strongly recommended** to use this update functionality, but if you still insist to update the Portal using the command line, you need to execute the following commands:

.. code-block:: bash

   sudo su
   cd /root/portal
   git pull origin master
   rake db:migrate
   cp /etc/mazi/config.yml /etc/mazi/config.yml.bu
   cp etc/config.yml /etc/mazi/config.yml
   cd /root/back-end
   git pull origin master
   service mazi-portal restart


MAZI backend
------------

.. note::
   You can reset the password of the MAZI Portal to 1234, using the MAZI backend script **mazi-resetpswd.sh**. This way, the administrator can access again the MAZI Portal administration panel and change the admin password accordingly. Check more info |here|.

.. |here| raw:: html

   <a href="https://github.com/mazi-project/back-end" target=_"blank">here</a>

Examples of *mazi-resetpswd.sh* usage:

* Reset the MAZI Portal's admin password to 1234

.. code-block:: bash

   sudo sh mazi-resetpswd.sh
