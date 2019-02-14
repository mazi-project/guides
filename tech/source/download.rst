.. _download :

Download a ready-made MAZI image 
================================

In this section you can choose one of the SD card images available from the table below.
The procedure of loading an image on a SD card is straightforward and described in details in :ref:`writingSD`.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                  MAZI toolkit images                                                                                                                                      |
+=========+==========================+===================================================================================================================+==================================+
| Release | Type                     | What's new                                                                                                        | Notes                            |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |3.0.3| | New Features, bug fixes  | Mesh functionality in portal, managed mode in portal, update jquery to 3.3.1, fix connection to SSID with space	 | Development channel              |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 3.0.2   | New features, Security   | Includes the MAZI Wiki in the Admin interface, removes key from root authorized_keys, stopping an application     | Stable, recommended for all      |
|         | fixes, Bug fixes         | disables relevant app instances, other visual fixes                                                               | new installs                     |	
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |3.0.1| | Bug fixes                | Check Internet connection in Dashboard before attempting to check version (improves speed), english message       | Stable                           |
|         |                          | correction	                                                                                                 |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |3.0|   | New Features             | Based on Raspbian stretch, all applications have been updated to their latest stable release, background          | Dev channel                      |
|         |                          | monitoring of Internet connectivity, new languages added (French, Arabic, Turkish, Chinese), update Font Awesome  |                                  |
|         |                          | to 5.5.0, show selected image in Guestbook conf	                                                                 |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.6|   | New Features, Bug Fixes  | Fix bugs in export/import procedure of the entire mazizone, fix bugs in export/import procedure of Guestbook,     | Stable, Major update             |
|         |                          | check user's input for domain url, allowing only valid domains (not special characters, enough dots etc.),        |                                  |
|         |                          | addition of a message informing the user that this is the last jessie image supported and he/she needs            |                                  |
|         |                          | to migrate to v3 images	                                                                                         |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2.5.6   | Bug fixes                | Fix bug regarding custom domain URL which crashes the captive portal                                              | Stable, Major Update             |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2.5.5   | Bug Fixes                | Show enabled instances in default splash page, Add more clients in dnsmasq config file,                           | Stable, Major Update             |
|         |                          | Fix bug in Guestbook snapshot                                                                                     |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2.5.4   | New Features, Bug fixes  | New captive portal functionality with dynamic captive page and improved user experience, Sorting of applications  |                                  |
|         |                          | in the admin interface, Fix bugs regarding application icons, Fix bug in Firefox when start sensing, Content      |                                  |
|         |                          | snapshot for Etherpad, Nextcloud, Wordpress, Overall snapshot export/import to external USB drive, Loading        |                                  |
|         |                          | message when browsing in the Portal, Other typos and bug fixes                                                    | Development channel              |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.5.3| | Bug fixes                | Selecting app instance icon is not obligatory, fix splash page button (bug in Firefox), fix ports                 | Stable,                          |
|         |                          |                                                                                                                   | Recommended for all new installs |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.5.2| | New Features, Bug fixes  | Two update channels (stable/Dev), fix open ports bug                                                              | Stable, Major Update             |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2.5.1   | Bug fixes                | Bug fixes for nodogsplash                                                                                         | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2.5     | New Features             | Nodogsplash, new organization in admin Network tab, location setup at MAZI Zone description is not mandatory,     |                                  |
|         |                          | visual fixes and typo fixes                                                                                       | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.4.6| | Bug fixes                | Fix bugs in setup page and in monitoring page                                                                     | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
|  2.4.5  |  New Features, Bug fixes | Improved performance in monitoring map, fix sensor tab showing data from multiple sensors, update fontawesome,    |                                  |
|         |                          | edit colors and icon in applications tab, new tab in setup page for MAZI Zone details, improved functionality in  |                                  |
|         |                          | monitoring tab, new update system, create custom application button, other bug fixes and typos                    | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.4.4| |  New Features            | Data Collection Framework                                                                                         | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.4.1| |  New Features, Bug fixes | Update Etherpad to latest version (1.6.3), install ep_comments_page plugin for commenting in pads,                | Major Update                     |
|         |                          | update Nextcloud to latest version (13), install app for external storage, create QR Code button, fix english flag|                                  |
|         |                          | , merge admin settings in one menu, configure max file size from admin settings, fix captive portal issue in MAC  |                                  |
|         |                          | devices, fix notification bug, fix multiple issues in sensor backend, typo fixes, monitoring map in user interface|                                  |
|         |                          | , new service for the rest interface                                                                              |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.3|   |  New Features, Bug fixes | Major update of the monitoring framework, New Guestbook admin functionalities, Fix Guestbook error reporting,     | Major Update                     |
|         |                          | New expand filesystem to SD button, full Sensehat support in Portal (gyroscope, accelerometer, compass, pressure),|                                  |
|         |                          | wrong db in sensor user interface bug fix, fix several other bugs                                                 |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.2|   |  New Features            | i18n support to enable translation, update various messages, show exact amount of disk space used.                | Major Update                     |
|         |                          | Backend: full sensehat support, support status in rest calls                                                      |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.1|   |  New Features, Bug fixes | Log section, Fix multiple instances feature, add system info in admin dashboard, multiple fixes                   | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |2.0|   |  New Features, Bug fixes | Monitoring framework (sensors, statistics, applications), Guestbook admin interface, Bug fixes                    | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.8.6   |  New Features            | Configure apps as splash screen, backend of Monitoring API                                                        | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.8.5| |  New Features, Bug fixes |  Configure MAZI domain, new External Router functionality, update User Documentation, export Guestbook content,   | Major Update                     |
|         |                          |  calendar in sensors, default snapshot, other bug fixes                                                           |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.8|   |  New Features            |  Integration of camera functionality (devices tab), fix timezone bug, other bug fixes                             | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.7.1   |  New Features, Bug fixes |  New Devices tab (sensors, camera), bug fixes, new log file, warning message in init page                         | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.7|   | New Features             |  Reboot button, shutdown button, support for more USB Wi-Fi antennas                                              | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.7   | New Features             |  Delete snapshot functionality, connect to hidden network, connect to passwordless network, edit admin username   | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.6   |  New Features, Bug fixes |  New Interview export functionality, bug fixes                                                                    | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.6.5| | New features             | Statistics menu (CPU, RAM, Storage etc.), time/date in user portal                                                | Major Update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.4   | Bug fixes                | Bug fixes in update functionality                                                                                 | Minor update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.3   | New features             | New one-click update functionality for the MAZI Portal                                                            | Minor update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.2   | Visual fixes             |                                                                                                                   | Minor update                     | 
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.6.1   | New features             | New first contact functionality, new configuration menu, merge saving/loading theme with saving/loading settings, | Update                           |
|         |                          | fix application clicks                                                                                            |                                  | 
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.6|   | Stable Release           | User Documentation updated, Admin Documentation updated, Guestbook updated, Etherpad plugins                      | Major update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1.5.5   | Visual/bug Fixes Release | Typos, fixed dual mode box in Networking, no password in demo mode, footer removal                                | Update                           |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.5.4| | New application Release  | Integration of Interview Archive application                                                                      | Minor update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.5.3| | Visual/bug Fixes Release | Typos, Upload/Download snapshot, Visual fixes, new demo mode, Admin change password form                          | Minor update                     |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.5.2| | Visual/bug Fixes Release |                                                                                                                   |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+
| |1.5|   | First Public Release     |                                                                                                                   |                                  |
+---------+--------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. |3.0.3| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v3.0.3.zip" target="_blank">3.0.3</a>

.. |3.0.1| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v3.0.1.zip" target="_blank">3.0.1</a>

.. |3.0| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v3.0.zip" target="_blank">3.0</a>

.. |2.6| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.6.zip" target="_blank">2.6</a>

.. |2.5.3| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.5.3.zip" target="_blank">2.5.3</a>

.. |2.5.2| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.5.2.zip" target="_blank">2.5.2</a>

.. |2.4.6| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.4.6.zip" target="_blank">2.4.6</a>


.. |2.4.4| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.4.4.zip" target="_blank">2.4.4</a>


.. |2.4.1| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.4.1.zip" target="_blank">2.4.1</a>

.. |2.3| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.3.zip" target="_blank">2.3</a>

.. |2.2| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.2.zip" target="_blank">2.2</a>

.. |2.1| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.1.zip" target="_blank">2.1</a>


.. |2.0| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v2.zip" target="_blank">2.0</a>


.. |1.8.5| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v1.8.5.zip" target="_blank">1.8.5</a>

.. |1.8| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v1.8.zip" target="_blank">1.8</a>


.. |1.7| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v1.7.zip" target="_blank">1.7</a>

.. |1.6.5| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v1.6.5.zip" target="_blank">1.6.5</a>

.. |1.6| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/mazizone-v1.6.zip" target="_blank">1.6</a>

.. |1.5.4| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/MAZI-toolkit-v1.5/mazizone-v1.5.4.zip" target="_blank">1.5.4</a>

.. |1.5.3| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/MAZI-toolkit-v1.5/mazizone-v1.5.3.zip" target="_blank">1.5.3</a>

.. |1.5.2| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/MAZI-toolkit-v1.5/mazizone-v1.5.2.zip" target="_blank">1.5.2</a>

.. |1.5| raw:: html

	<a href="http://nitlab.inf.uth.gr/mazi-img/MAZI-toolkit-v1.5/mazizone-v1.5.zip" target="_blank">1.5</a>



.. |images| raw:: html
	
	<a href="http://nitlab.inf.uth.gr/mazi-img/MAZI-toolkit-images.pdf" target="_blank">MAZI toolkit images</a>


.. note::
	You can find here all the credentials needed for the above images.
	
	**root user** and **pi user** password:	mazizone

	**mySQL**: user: root password: m@z1 (editable through the Portal)
	
	**Wi-Fi network**: mazizone (no password)
	
	**Etherpad** user: admin password: mazizone
	
	**NextCloud** user: admin password: mazizone
	
	**Guestbook** user: admin password: mazizone
	
	**Interview Archive** user: admin password: mazizone
	

.. |image| raw:: html

 <a href="http://nitlab.inf.uth.gr/mazi-img/" target="_blank">image</a>

