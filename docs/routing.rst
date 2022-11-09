Routing
=======

Routes are defined in **routes/web.php** file. As mentioned earlier, routes are basically an array with key names for the URL, and the name of the **Controller** class and method to be called for the URL as value.

Default Routes
--------------

Before defining routes, you may need to declare the default route for landing and error pages. 

To do that, open **config/url.php** file and modify the value of **landing** key for the default landing page, and **error** key for the default error page of the project. 

As value, you must type the name of the controller class first, then method of the class to be called after **@** sign-

.. code-block:: yaml

	HomeController@welcome

Above, ‘HomeController’ is the name of the controller class and ‘welcome’ is the name of the method. 

You can define the URL for accessing database migration page as the value of **migration_url** key. The URL must exclude the domain name and first forward slash. Once you go into your browser and access the URL (by adding a forward slash and the value of the aforementioned key after your domain name) you will see the database migration page.

You can also define the **prefix** for the URLs that will receive API calls in the **api_url** key. The framework will automatically include the prefix at the beginning of the API routes that you have defined.

Defining Web Routes
-------------------

To define web routes, open **routes/web.php** file. There, you can define the URL for the route as a key of the array returned, and name of the controller class along with the method called from the class as its value-

.. code-block:: yaml

	‘welcome’ => 'HomeController@welcome'

In the above example, for the *your-site-url/welcome* URL, **welcome** method from the **HomeController** class is executed. Like default routes, you have to type the method name after the controller class name and **@** sign.

To include SEO friendly URL parameters to your web routes, include curly brackets to each of the route keywords that you want to use as a URL parameter like below-

.. code-block:: yaml

	‘blog/show/{blog_id}’ => 'BlogController@show'

Note that, here, the generated **$_GET** parameter for **{blog_id}** will simply exclude the curly brackets, i.e., it will be **blog_id**. Furthermore, to identify such a route, the route must include at least one route keyword that is not a URL parameter. Finally, if there are a list of routes that only differ by the name of URL parameter(s) inside the curly braces, always the first route from that list will be called to execute the assigned controller method.

Defining API Routes
-------------------

To define API routes, open **routes/api.php** file. There, you can define the API routes similarly to how the web routes are defined above-

.. code-block:: yaml

	'test_api' => 'HomeController@testApi',

It works almost exactly the way as the web routes, except it doesn’t support SEO friendly URL parameters! Notice that you must exclude the API prefix defined in **config/url.php** while defining your API routes. Call *your-site-url/api-prefix/test_api* url from your browser/postman to receive your API data.

Using Routes
------------

CodeCube provides some default functions for working with routes and URLs.

To show a route link in a view, use the **route()** method. The route must be defined in the **routes/web.php** file as a route key, otherwise the framework will report error.

.. code-block:: yaml
	
	echo route('signup'); 

You can add additional parameters to the route as an associative array like below-

.. code-block:: yaml
	
	echo route('items/show', ['id' => $item['id']]);

If your web route includes SEO friendly URL parameters, you can set the value for those parameters defined in the route using the passed associative array like below-

.. code-block:: yaml
	
	echo route('blog/show/{blog_id}', ['blog_id' => 5]);

Here, **{blog_id}** will be replaced by the value of **blog_id** from the associative array that has been passed as the function’s second parameter. Note that, to replace the route keyword with a value from the array, the key name MUST BE the same as the curly bracket excluded keyword from the route. The generated URL will be *your-site-url/blog/show/5*.

To generate API links, use the **api_route()** function. It works almost the same way as the **route()** function, except it doesn’t support SEO friendly URL parameters.

.. code-block:: yaml
	
	echo api_route('sitemap', ['id' => 5]);

It will generate the link *your-site-url/api/sitemap?id=5*. Notice that, similarly to web routes, you can add URL parameters by passing the list of parameters and their names as an associated array as the second argument of the function.

Sometimes during routing you might need to include **$_GET** parameters of the current URL along with additional **$_GET** parameters you want to pass to a URL. You can do this using **routeUrl()** method. The third parameter takes the list of **$_GET** parameters of the current URL you want to exclude, as an array-

.. code-block:: yaml
	
	echo routeUrl('items/show', ['id' => $item['id']], ['item_token]);

If your web route includes SEO friendly URL parameters, in above function, you can set the value for those parameters defined in the route in a similar fashion as the **route()** function-

.. code-block:: yaml
	
	echo routeUrl('blog/show/{blog_id}', ['blog_id' => 5, 'keyword' => 'author'], ['blog_id']);

It URL it will generate is *your-site-url/blog/show/5?keyword=author*.

To check whether the current URL is a specific route, use the **route_is()** method.

.. code-block:: yaml
	
	echo route_is('home') ? 'active' : ‘’;

In the above code, the framework checks whether the current route is **home** and if it is, shows **active**.

To exclude specific keywords from route during checking, add curly braces to the route keywords like below-

.. code-block:: yaml
	
	echo route_is('blog/show/{blog_id}/author') ? 'active' : ‘’;

In the above example, the function will automatically exclude the **{blog_id}** keyword and check whether the position of rest of the parameters match with current URL keywords, and return **TRUE** if they do.

To get the route from the current URL, use **get_route()** method. For URL *your-site-url/home*, this method will extract the route **home**-

.. code-block:: yaml
	
	echo get_route();

You can replace certain keywords of the URL by passing the list of keywords and their position as parameter to get a more precise route-

.. code-block:: yaml
	
	echo get_route(['2' => '{blog_id}']);

Above for URL *your-site-url/blog/show/45*, the function will return “blog/show/{blog_id}”.

To get the URL of the current page use the following function-

.. code-block:: yaml
	
	echo get_url();

To redirect from controller to the last visited URL of the site from where some form data was submitted, use **back()** function-

.. code-block:: yaml
	
	echo back();