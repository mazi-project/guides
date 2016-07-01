# MAZI Documentation

This is the documentation of the MAZI project, written with the Sphinx documentation tool.

Here you can find the source files of the documentation, for making any changes or additions you want.

Clone the guides repository to your computer
--------------------------------------------

	% git clone git@github.com:mazi-project/guides.git

Modify the files
----------------

The source folder is where all the files you need are stored.
The index.rst file is the skeleton of the documentation. You can add another section below the "Making a Wi-Fi Access Point".
Each .rst file is another page in the documentation. Regarding the formatting, you can see the existing files as examples.

Build the results
-----------------

After any changes you make, you need to execute the following command, inside the root folder of the repository, in order to build the source files to html format.

	% sphinx-build -b html source/ folder_for_placing_the_html_files/

Then go to the folder where you placed the html files and open the index.html file, to see your changes.
