Directory Structure
===================

CodeCube follows a similar directory structure to `Laravel framework <https://laravel.com>`_. The directories are structured in a way to provide a standard starting point to use the framework, but with a thorough understanding of the directories, the developers are free to customize the directories anyway he likes without breaking the system:

.. code-block:: text
   :caption: CodeCube Framework Directory Structure

	/app
	    /Console
		 /Handlers
	    /Helpers
	    /Http
	        /Controllers
	        /Guards
	    /Models
	/config
	/database
	/resources
	    /assets
	    /locale
	    /markups
	    /views
	/routes
	/storage
	    /app
	        /public
	    /logs
	/vendor

Below the directories are briefly explained-

* The **app** directory: This is the directory to store all your model, controller, guard and rest of the classes. This directory has three sub directories-

 - **Console:** In this folder all the console commands along with their handlers are stored.

  + **Handlers:** All the console ommand handler classes are stored here.

 - **Helpers:** This is where you store all your helper classes.
 - **Http:** This folder has two sub-classes-

  + **Controllers:** All the controller classes are stored here.
  + **Guards:** All the classes that contain various methods to maintain authentication and access control logic are stored here.

 - **Models:** All your model classes will be included here.

* The **config** directory: This is where you will store various project configuration files. All of these configuration files will return hard-coded data declared by the developer to be used wherever necessary within the system, as array. 
* The **database** directory: In this directory all the files that will be used to run migration are stored. Just like configs, the files will return arrays, but the arrays have various database commands as values instead.
* The **resource** directory: In the directory all the files necessary to generate your views are stored. The directory contains three sub-directories:

 - **Assets:** Contains all the project assets such as images, JavaScript and CSS files. 
 - **Markups:** Contains various XML files to provide necessary design classes, layouts etc. to the system to generate general views such as mail and pagination.
 - **Views:** Contains all your view files.
 
* The **route** directory: This directory contains all the route definitions for your system. Like config and database files, these files will return arrays with keys for route name and values for URL.
* The **storage** directory: This is where all the uploaded files (by default) and log files are stored.
* The **vendor** directory: This folder will be generated once the composer update command is run. This folder contains all the composer dependencies. 