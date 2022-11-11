Sitemap
=======

A **sitemap.xml** is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them. CodeCube framework provides a default sitemap. You can manually update the sitemap if you want, but the CodeCube framework provides built-in functionalities to manage the sitemap.

To manage the sitemap, include the base Sitemap class in your .php file like below-

.. code-block:: text

	use Base\Sitemap; 

Setting up Sitemap
~~~~~~~~~~~~~~~~~~

To setup Sitemap for the first time or to add multiple new URLs to sitemap, use the ``updateNodes()`` method like below-

.. code-block:: text

	$sitemap = new Sitemap;
	$urls = array();
	$blogs = $this->blog->getBlogs();
	foreach ($blogs as $blog) {
	array_push($urls, [ route('blog/show', ['id' => $blog['id']]), date("Y-m-d", strtotime($blog['updated_at'])) ]);
	}
	$sitemap->updateNodes(['show'], $urls);

Adding an URL to Sitemap
~~~~~~~~~~~~~~~~~~~~~~~~

To add a new URL to the sitemap, use the ``addNode()`` method with ``route()`` method like below-

.. code-block:: text

	$sitemap = new Sitemap;
	$sitemap->addNode(route('blog/show', ['id' => 1]), date('Y-m-d'));

Deleting all URLs in Sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete all URLs in the **sitemap.xml**, use the ``deleteNodes()`` method like below-

.. code-block:: text

	$sitemap = new Sitemap;
	$sitemap->deleteNodes();

Refreshing Sitemap
~~~~~~~~~~~~~~~~~~

To refresh the sitemap, use the ``refreshSitemap()`` method like below-

.. code-block:: text

	$sitemap->refreshSitemap(['show'], $urls);
