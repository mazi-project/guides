.. _backend :

MAZI backend
==============

The MAZI backend has been designed and developed in order to handle low-level communication between the MAZI toolkit's hardware and the MAZI Portal. Moreover, it can be used by developers or advanced MAZI toolkit users to configure a MAZI Zone or build one from scratch.

Install the MAZI backend
------------------------

In order to install the MAZI Backend, you have to clone the repository in your |raspbian| Operating System.

.. |raspbian| raw:: html

  <a href="https://www.raspberrypi.org/downloads/raspbian/" target="blank">Raspbian</a>

Become root user.

.. code-block:: bash

   sudo su

Clone the repository.

.. code-block:: bash

   cd /root
   git clone git@github.com:mazi-project/back-end.git

Finally, install the following requirements:

.. code-block:: bash

  apt-get install python-pip
  pip install speedtest-cli
  apt-get install sshpass
  apt-get install jq 
 
You can now proceed with the rest of the guidelines and take advantage of the MAZI backend in order to control and manage your MAZI Zone. At the end of each of the following sections, you can find examples on the usage of the scripts for the corresponding configuration actions.
