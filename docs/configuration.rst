Configuration
=============


Environment Configuration
-------------------------

If you go to project folder, you’ll find there is a project configuration file titled **env.example.php**. Make a copy of the file and rename it to **env.php**. You can either do it manually via file manager or run the following command in the previously opened terminal/git bash window-

.. code-block:: text
	
	cp env.example.php env.php

Open the **env.php** file in a text editor and change the values of the constants to set up your project. The setup constants are explained below-

Set Application Values
~~~~~~~~~~~~~~~~~~~~~~

* ``APP_NAME``: Defines application name e.g. if you are creating a blog you can rename the constant into “My Blog”. 
* ``APP_URL``: Defines the application default URL. By default it is set to local server address *http://localhost:8000*. You should set it to domain/subdomain address once deployed in an online server. You can set the protocol dynamically using this code: ``(isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] == 'on' ? 'https' : 'http').'://localhost:8000'``.
* ``APP_ENV``: Defines the current application environment. BY default it is set to development environment- ‘dev’. You should change the value once you deploy the project in production server.
* ``APP_KEY``: The key will be used to enforce security in various project functionalities in development mode, such as for running migrations.  

Set Database Values
~~~~~~~~~~~~~~~~~~~

* ``DB_CONNECTION``: Defines your database driver/what database you are using. Default value is ‘mysql’. You can change it if you are using any other database instead such as MariaDB or SQLite.
* ``DB_HOST``: Defines your database host address. Default value is ‘127.0.0.1’. 
* ``DB_PORT``: Defines the port of your database host address. Default value is ‘3306’. 
* ``DB_DATABASE``: Defines the database name. Default value is ‘homestead’. Change it to the name of the database schema you are going to use for your project.
* ``DB_USERNAME``: Defines the database username. Default value is ‘homestead’. Change it to the username to access your database schema, for example ‘root’.
* ``DB_PASSWORD``: Defines the database password. Change it to the password to access your database schema. If there is no password keep it empty.

Set Mail Values
~~~~~~~~~~~~~~~

* ``MAIL_DRIVER``: Defines you mail driver. By default it is set as ‘smtp’. If you are using any other mail driver such as ‘pop3’, change it accordingly.
* ``MAIL_HOST``: Defines your mail host URL. Default value is ‘smtp.mailtrap.io’.
* ``MAIL_PORT``: Defines the port of your mail host URL. Default value is ‘2525’.
* ``MAIL_USERNAME``: Defines the username for your mail settings.
* ``MAIL_PASSWORD``: Defines the password for your mail settings.
* ``MAIL_ENCRYPTION``: Defines the type of encryption you will use for sending mails. Default value is ‘ssl’.

Application Configuration
-------------------------

Before starting up your application, you may want to checkout the application configuration. Open **config/app.php** in a text editor to checkout or change the basic configuration of application. Below the keys of the array returned from the file are explained-

* ``auth_time``: Declares how long a login session will last. To update the value, change the default integer and define whether it will be in hours, minutes or seconds. 
* ``remember_me``: Declares how long the remember me cookie will last. Follow the same strategy as ``auth_time`` settings to update this value.
* ``update_session_cookie_settings``: Declares whether the previously declared auth time will be actually activated and updated in php settings. Default value is ‘no’, setting it to ‘yes’ will update the php session settings. 
* ``upload``: Declares where the uploaded files will be saved. By default the system will upload the files in **storage/app/public** folder.
* ``auto_logging``: Declares whether the system will save various errors, warning etc. messages from the system or logs declared by you in various log files. By default it is ‘on’, changing the value to anything else will turn off auto-logging. The system saves the log files in **storage/logs** folder.

Additionally you can run the migration files if you want to checkout the demo application ported with the framework. Go to *your-server-url/database_migration*, provide your application key you’ve set in the **env.php** file and click on the proceed button to create the necessary tables and Views for the demo application.
