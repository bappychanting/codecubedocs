Installation
============

Server Requirements
-------------------

The CodeCube framework has a few system requirements. Installing Apache distribution packages such as Xampp, Wamp, Laragon (for windows) or a standard Lamp stack setup (for Linux) will satisfy most if not all requirements. If you are setting up an Apache server manually, make sure your server meets the following requirements:

* PHP >= 7.2.0
* BCMath PHP Extension
* Ctype PHP Extension
* JSON PHP Extension
* Mbstring PHP Extension
* OpenSSL PHP Extension
* PDO PHP Extension
* Tokenizer PHP Extension
* XML PHP Extension

Additional Requirements
-----------------------

* Relational database such as MySQL
* Git
* Composer
* A standard HTML supported browser 

You can follow `this tutorial <https://www.linkedin.com/pulse/full-web-development-environment-setup-step-guide-php-mahadi-hasan/>`_ while setting up Lamp server in Debian based Linux distro to ensure your server setup is up to the standard.

Installing Codecube
-------------------

First make sure you have Git installed. Go to your server root directory (for example **var/www/html** in Lamp depending on your settings), open it in terminal (or gitbash if you’re in windows) and run the following command-

.. code-block:: yaml

	composer create-project codecube/codecube

Running this command will automatically setup all composer dependencies.

Alternatively, you can run the following command to clone from the GitHub repository directly.

.. code-block:: yaml

	git clone https://github.com/bappychanting/codecube.git

You will see it has created a folder titled **codecube**. Customize the folder name to what you want to set your project name as. 

You can run the following command and change **my-folder-name** to set your desired folder name directly- 

.. code-block:: yaml

	git clone https://github.com/bappychanting/codecube.git my-folder-name

Once done navigate to the folder and update composer via following command-

.. code-block:: yaml

	composer update

Afterwards, go to the terminal, make sure the path is set to your project folder and run below command to start your project-

.. code-block:: yaml

	php -S localhost:8000
