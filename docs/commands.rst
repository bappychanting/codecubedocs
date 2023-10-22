Command Line
====================

Console commands are stored in the **app/Console/commands.php** file, and their handler classes are stored in the **app/Console/Handlers** folder.

you can define a command in the **commands.php** file as a key of the returning array and name of the handler class as its value-

.. code-block:: text

	‘migrate’ => 'Migrate'

Above,  ‘migrate’ is the console command and ‘Migrate’ is its hanlder class.

Each hanlder class must extend the **Base/BaseConsole** class and have a ``handler()`` method defined, within which the codeblock to be executed is written.

To use the command line arguments passed, use the ``$args`` variable defined in **BaseConsole** class like below-

.. code-block:: text

	echo $this->args[1];
