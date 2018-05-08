.. _sense :

Sensors
=======

Manage the sensors attached on the Raspberry of the MAZI toolkit.

.. note::
   For the interaction with the sensors attached on the MAZI toolkit you can use the MAZI backend script **mazi-sense.sh**. Check more info |here|.

.. |here| raw:: html

   <a href="https://github.com/mazi-project/back-end" target=_"blank">here</a>



Sensehat
--------

Examples of *mazi-sense.sh* usage:

* Take measurements from sensehat each 2 seconds for the next 10 seconds

.. code-block:: bash

   sudo bash mazi-sense.sh -n sensehat -d 10 -i 2

* Display the status of the sensehat module

.. code-block:: bash

   sudo bash mazi-sense.sh -n sensehat -a


* Take measurements from sensehat each 2 seconds for the next 10 seconds and store them in the database

.. code-block:: bash

   sudo bash mazi-sense.sh -n sensehat -d 10 -i 2 -s

Sht11
-----

To be filled soon
