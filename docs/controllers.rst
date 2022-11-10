Controllers
===========

Controller classes are stored in **app/Https/Controllers** folder. All new controller classes declared by the developer must extend the default **Controller** class in the folder which itself inherits the **BaseController** class to access various **base** controller methods. Default **Controller** class can also be used to write custom methods that will be used throughout different controller classes. 

Below is an example of a basic controller class-

.. code-block:: text

	<?php

	namespace App\Http\Controllers;

	class HomeController extends Controller
	{
	    public function home() 
	    {
	        $this->guard('CheckAuth');
	        return $this->view('home');
	    }
	}

Here are the **BaseController** class methods that can be used in controller classes:

The **config()** Method: This method can be used to call configuration files from the **config** directory. If the config file is nested inside directories, the directory tree of the config file is represented via (.) dots. Below the **config/dev/app.php** file is called by this method and saved in ``$app`` variable.

.. code-block:: text    

	$app = $this->config('dev.app');

The **view()** Method: This method is used for calling view files at the end of controller method and pass data to them. The directory tree of the view file is represented via (.) dots. 

.. code-block:: text

	public function home() 
    {
        $auth = $request->auth();
        return $this->view('front.home', compact(‘auth’));
    }

In the above example, **views/front/home.php** view file is called in the ``HomeController::home()`` method and the authentication data is passed in the view.

The **redirect()** Method: Used for redirecting to different route urls. 

.. code-block:: text

	public function redirect() 
    {
            $this->redirect('items/show', ['id' => 1]);
    }

In the above example, the ``HomeController::redirect()`` method redirects to **items/show** route with id parameter.

The **abort()** Method: This method is used to redirect to error pages. 

.. code-block:: text

	public function error() 
    {
        $this->abort(404);
    }

In the above example, the ``HomeController::error()`` method shows the **404** error page to the user.