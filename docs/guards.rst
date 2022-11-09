Guards
======

**Guard** classes allow to perform actions such as request checking, filtering, redirection etc. conveniently before executing a controller method. It encapsulates these filtering logic, and as such, helps to perform actions such as authentication or access control while called, without repeating codes in different controller classes. 

.. code-block:: yaml

	<?php
	namespace App\Http\Guards;
	use Base\Request;
	use Base\BaseController as base; 
	class CheckGuest
	{
	    public function __construct()
	    {
	        $request = new Request();
	        if($request->auth()){
	            base::redirect('home');
	        }
	    }
	}

Guard classes are defined in **app/Http/Guards** folder. Below is an example of a guard class that checks whether a user is authenticated, and if so, redirects him to home page, thus preventing him from accessing the function.

This guard can be called within a controller method like below-

.. code-block:: yaml

	$this->guard('CheckGuest');