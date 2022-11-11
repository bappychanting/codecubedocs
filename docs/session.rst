Session Requests
================

Base **Request** class is used to access various session data. All data that are controlled using **Request** class are stored in the **Request** key of session array. To use the **Request** class, call it on top of your class like below-

.. code-block:: text

	use Base\Request;

Once called, you can access various methods of the class to control session data. Below how the session data can be accessed and modified using **Request** class is explained-

Reading and Writing Session data
--------------------------------

You can input new data into session using the ``Request::setData()`` method like below-

.. code-block:: text

	Request::setData(‘color-green’, ‘green);

Here, **color** is the name (key) of session and green is the value. To read the input value you can use ``Request::getData()`` method like below-

.. code-block:: text

	echo Request::getData(‘color-green’);

Additionally you can use ``Request::put()`` method to store associative arrays in session like below-

.. code-block:: text

	Request::put(‘winners’, [‘first’ => ‘John’, ‘second’=> ‘doe’]);

You can get the array using ``Request::show()`` method. The data will be returned as a PHP stdClass Object-

.. code-block:: text

	<?php 
		$winners = Request::show(winners);
		echo winners->first;
	?>

Destroying Session Data
-----------------------

To destroy a session data, use ``Request::destroy()`` method like below-


.. code-block:: text
	
	Request::destroy(‘winners’);

Flashing Session Data
---------------------

Sometimes you might need to flash session data to display alerts, warnings etc. Flashing session data means destroying session data automatically right after it has been used.  To set session flash data, use ``Request::setFlash()`` like below-

.. code-block:: text

	Request::setFlash([‘success’ => ‘Item added!’]);

To flash the session data, use ``Request::getFlash()`` like below-

.. code-block:: text

	print_r(Request::getFlash());

Handling Cookies
----------------

Base Request class provides you with some built in methods to conveniently handle cookies.

To add a new cookie, use ``Request::setCookie()`` like below-

.. code-block:: text
	
	Request::setCookie('hello', 'Hello World', 300);

Here, ‘hello’ is the name of the cookie, ‘Hello World’ is the value and 300 is how long the cookie will last in seconds.

To get the cookie value, use ``Request::getCookie()`` like below-

.. code-block:: text

	echo Request::getCookie('hello');

To delete a cookie, use ``Request::deleteCookie()`` like below

.. code-block:: text

	Request::deleteCookie('hello');

Get HTTP Headers
----------------

You can access all the HTTP headers using ``Request::headers()`` method

.. code-block:: text

	print_r(Request::headers());

Above method will show all the information related to HTTP headers.