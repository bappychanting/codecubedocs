CSRF Protection
===============

CodeCube makes it easy to protect your application from `cross-site request forgery(CSRF) <https://en.wikipedia.org/wiki/Cross-site_request_forgery>`_ attacks. Cross-site request forgeries are a type of malicious exploit whereby unauthorized commands are performed on behalf of an authenticated user.

CodeCube automatically generates a **CSRF token** for each active user session managed by the application. This token is used to verify that the authenticated user is the one actually making the requests to the application.

Anytime you define an HTML form in your application, you should include a hidden **_token** field in the form so that the framework can validate the request-

.. code-block:: yaml

	<form method="POST" action="<?php echo route('items/store'); ?>">
	<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>">
	</form>

X-CSRF-TOKEN
------------

In addition to checking for the **CSRF** token as a POST parameter, the framework will also check for the **X-CSRF-TOKEN** request header. You could, for example, store the token in an HTML meta tag:

.. code-block:: yaml

	<meta name="csrf-token" content="<?php echo csrf_token(); ?>">

Then, once you have created the meta tag, you can instruct a library like jQuery to automatically add the token to all request headers. This provides simple, convenient **CSRF** protection for your AJAX based applications-


.. code-block:: yaml

	$.ajaxSetup({
	    headers: {
	        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
	    }
	});