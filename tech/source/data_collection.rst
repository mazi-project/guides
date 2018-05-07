.. _data_collection :

MAZI Data Collection Service
=============================

The MAZI Data Collection Service is the framework for collecting and managing data in the context of MAZI Zones.

It can be installed either together with the MAZI Portal or as a standalone software component in any server for collecting data from MAZI Zones and depicting them on a map.


Install together with the MAZI Portal
--------------------------------------

You can follow the (:ref:`portal`) section to install the data collection framework alongside with the MAZI Portal.


Install as a standalone service
--------------------------------

Clone the repository

.. code-block:: bash

   sudo su
   cd /root
   git clone https://github.com/mazi-project/portal.git

Prepare the database

.. code-block:: bash

   cd portal
   rake init
   rake db:migrate

Create and enable the service for the data collection framework

.. code-block:: bash

   cp init/mazi-rest /etc/init.d/mazi-rest
   chmod +x /etc/init.d/mazi-rest
   update-rc.d mazi-rest enable

Execution
^^^^^^^^^^

Both services should be running

.. code-block:: bash

   service mazi-rest start

Usage
^^^^^

You can access the web interface of the data collection service in the following URL:

http://portal.mazizone.eu:7654/maps/monitoring_map
