.. _apps :

Applications
============


Etherpad
^^^^^^^^

Install nodejs

.. code-block:: bash

	sudo apt-get install gzip git-core curl python libssl-dev pkg-config
	sudo apt-get install build-essential python g++ make checkinstall
	cd /usr/src
	sudo wget http://nodejs.org/dist/node-latest.tar.gz
	sudo tar xzvf node-latest.tar.gz
	cd node-v*
	sudo su
	./configure && checkinstall

When the dialog window opens, enter ‘3’ and remove the “v” in front of the version number.
Install nodejs with the following command:

.. code-block:: bash

	dpkg -i node_*
	exit


Create a MySQL or a MariaDB database

.. code-block:: bash

	mysql -u root -p
	mysql> CREATE DATABASE etherpad CHARACTER SET utf8 COLLATE utf8_general_ci; 
	mysql> GRANT ALL PRIVILEGES ON etherpad.* TO etherpad_user@localhost IDENTIFIED BY ‘password’;
	mysql> FLUSH PRIVILEGES;
	mysql> quit

.. note::

	You can change "etherpad_user" and "password" in the above command to whatever you like.

Install and configure Etherpad Lite

.. code-block:: bash

	cd /var/www/html
	sudo git clone git://github.com/ether/etherpad-lite.git
	cd etherpad-lite
	sudo cp settings.json.template settings.json
	sudo nano settings.json

and change the following settings:
 
.. code-block:: bash

	 //configure the connection settings
 	"dbType" : "mysql",
 	"dbSettings" : {
	   "user"    : "etherpad",
	   "host"    : "localhost",
	   "password": "mazizone",
	   "database": "etherpad"
	 },
	.
	.
	.
	// add admin user
	"users": {
	 "admin": {
	 "password": "mazizone",
	 "is_admin": true
	 }
	},

Create a system user

.. code-block:: bash

	sudo adduser --system --home=/var/www/html/etherpad-lite/ --group etherpad
	sudo chown -R etherpad: /var/www/html/etherpad-lite/

Start Etherpad Lite for the first time

.. code-block:: bash

	sudo su -c "/var/www/html/etherpad-lite/bin/run.sh" -s /bin/bash etherpad


Create an init script using your favorite editor

.. code-block:: bash

	cd /etc/init.d/
	sudo nano etherpad-lite

Copy and paste the following into your file:

.. code-block:: bash

	#!/bin/sh
	### BEGIN INIT INFO
	# Provides:          etherpad-lite
	# Required-Start:    $local_fs $remote_fs $network $syslog
	# Required-Stop:     $local_fs $remote_fs $network $syslog
	# Default-Start:     2 3 4 5
	# Default-Stop:      0 1 6
	# Short-Description: starts etherpad lite
	# Description:       starts etherpad lite using start-stop-daemon
	### END INIT INFO

	PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/opt/node/bin"
	LOGFILE="/var/www/html/etherpad-lite/etherpad-lite.log"
	EPLITE_DIR="/var/www/html/etherpad-lite"
	EPLITE_BIN="bin/safeRun.sh"
	USER="etherpad"
	GROUP="etherpad"
	DESC="Etherpad Lite"
	NAME="etherpad-lite"

	set -e

	. /lib/lsb/init-functions

	start() {
	  echo "Starting $DESC... "

	    start-stop-daemon --start --chuid "$USER:$GROUP" --background --make-pidfile --pidfile /var/run/$NAME.pid --exec $EPLITE_DIR/$EPLITE_BIN -- $LOGFILE || true
	  echo "done"
	}

	#We need this function to ensure the whole process tree will be killed
	killtree() {
	    local _pid=$1
	    local _sig=${2-TERM}
	    for _child in $(ps -o pid --no-headers --ppid ${_pid}); do
		killtree ${_child} ${_sig}
	    done
	    kill -${_sig} ${_pid}
	}

	stop() {
	  echo "Stopping $DESC... "
	   while test -d /proc/$(cat /var/run/$NAME.pid); do
	    killtree $(cat /var/run/$NAME.pid) 15
	    sleep 0.5
	  done
	  rm /var/run/$NAME.pid
	  echo "done"
	}

	status() {
	  status_of_proc -p /var/run/$NAME.pid "" "etherpad-lite" && exit 0 || exit $?
	}

	case "$1" in
	  start)
	      start
	      ;;
	  stop)
	    stop
	      ;;
	  restart)
	      stop
	      start
	      ;;
	  status)
	      status
	      ;;
	  *)
	      echo "Usage: $NAME {start|stop|restart|status}" >&2
	      exit 1
	      ;;
	esac
	exit 0

.. code-block:: bash

	sudo chmod +x /etc/init.d/etherpad-lite
	sudo update-rc.d etherpad-lite defaults
	sudo /etc/init.d/etherpad-lite start





Nextcloud
^^^^^^^^^

You can refer to the official |nc_doc| for the installation procedure.

.. |nc_doc| raw:: html

        <a href="https://docs.nextcloud.com/server/15/admin_manual/contents.html" target="_blank">Nextcloud documentation</a>


Guestbook
^^^^^^^^^

Install mongodb

.. code-block:: bash

	sudo apt-get install mongodb-server

and start it as a service 
 
.. code-block:: bash

	sudo service mongod start

Download Guestbook

.. code-block:: bash

	cd /var/www/html
	sudo git clone https://github.com/mazi-project/mazi-board.git
	cd mazi-board/src/node
	sudo npm install
	sudo npm install pm2 -g
	cp config.default.js  config.js

Start Guestbook

.. code-block:: bash

	sudo pm2 start main.config.js


Configuring Guestbook to run at boot time

.. code-block:: bash

	sudo nano /etc/init.d/mazi-board

Copy and paste the following into your file:

.. code-block:: bash

	#!/bin/sh

	### BEGIN INIT INFO
	# Provides:          guestbook
	# Required-Start:    $local_fs $remote_fs $network $syslog
	# Required-Stop:     $local_fs $remote_fs $network $syslog
	# Default-Start:     2 3 4 5
	# Default-Stop:      0 1 6
	# Short-Description: Starts main.config.js script 
	# Description:       Service script which start mazi-board at boot time
	### END INIT INFO

	start(){
	    cd /var/www/html/mazi-board/src/node/
	    sudo pm2 start main.config.js
	}
	stop(){
	    cd /var/www/html/mazi-board/src/node/
	    sudo pm2 stop guestbook-back-end
	}

	case "$1" in
	  start)
		start
		;;
	  stop)
		stop
		;;
	  restart)
		stop
		start
		;;
	  *)
		echo $"Usage: $0 {start|stop|restart}"
		exit 1
	esac
	exit 0


.. code-block:: bash

	sudo chmod +x /etc/init.d/mazi-board
	sudo update-rc.d mazi-board defaults
	sudo service mazi-board start




Wordpress
^^^^^^^^^
You can refer to the official |wordpress_doc| for the installation procedure.

.. |wordpress_doc| raw:: html

        <a href="https://wordpress.org/support/article/how-to-install-wordpress/" target="_blank">Wordpress documentation</a>


Interview Archive
^^^^^^^^^^^^^^^^^^
Download Interview Archive

.. code-block:: bash

        cd /var/www/html
        sudo git clone https://github.com/mazi-project/archive.git
        cd mazi-princess/src/server/node
        sudo npm install
        sudo npm install pm2 -g
        cp config.default.js  config.js

Start Interview Archive

.. code-block:: bash

        sudo pm2 start main.js


Configure Interview Archive to run at boot time

.. code-block:: bash

        sudo nano /etc/init.d/mazi-princess

Copy and paste the following into your file:

.. code-block:: bash


	#!/bin/sh

	### BEGIN INIT INFO
	# Provides:          interview
	# Required-Start:    $local_fs $remote_fs $network $syslog
	# Required-Stop:     $local_fs $remote_fs $network $syslog
	# Default-Start:     2 3 4 5
	# Default-Stop:      0 1 6
	# Short-Description: Starts main.js script
	# Description:       Service script which starts interview app at boot time
	### END INIT INFO

	start(){
        	cd /var/www/html/mazi-princess/src/server/node/
	        pm2 start main.js
	}
	stop(){
	       cd /var/www/html/mazi-princess/src/server/node/
	       pm2 stop main.js
	}

	case "$1" in
	  start)
	        start
	        ;;
	  stop)
	        stop
	        ;;
	  restart)
	        stop
	        start
	        ;;
	  *)
        	echo $"Usage: $0 {start|stop|restart}"
	        exit 1
	esac
	exit 0


.. code-block:: bash

	sudo chmod +x /etc/init.d/mazi-princess
	sudo update-rc.d mazi-princess defaults
	sudo service mazi-princess start



Limesurvey
^^^^^^^^^^^^^
You can refer to the official |lime_doc| for the installation procedure.


.. |lime_doc| raw:: html

        <a href="https://manual.limesurvey.org/Installation_-_LimeSurvey_CE" target="_blank">Limesurvey documentation</a>

