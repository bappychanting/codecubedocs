Database
========

CodeCube provides some built in mechanisms for easier database interaction.

Configuring Database
--------------------

As discussed in :doc:`configuration` chapter, you can configure the database connection by changing the ``DB_`` constants in **env.php** file like below-

.. code-block:: text

    const DB_CONNECTION = 'mysql'; 
    const DB_HOST = '127.0.0.1'; 
    const DB_PORT = '3306'; 
    const DB_DATABASE = 'codecube'; 
    const DB_USERNAME = 'root'; 
    const DB_PASSWORD = '1234'

Query Builders
--------------

You can use CodeCube’s built in functionalities to perform **CRUD** (Create, Retrieve, Update, Delete) functions on database. To access those functionalities, you must use the base **DB** class at the top of your PHP file.

.. code-block:: text

    use Base\DB; 

Retrieving Results
------------------

To read a table from database, use the ``table()`` method of the **DB** class to begin query, and ``read()`` method to get the result.

.. code-block:: text

    $db = new DB; 
    $items = $db->table('items')->read(); 

Aggregation
~~~~~~~~~~~

To get the sum of the last set of values returned by ``read()`` method, use the ``getTotal()`` method-

.. code-block:: text

    $total_items = $db->getTotal(); 

Add Conditions
~~~~~~~~~~~~~~

To apply the SQL **where** clause on records, combine the ``where()`` method with other clauses-

.. code-block:: text

    $items = $db->table('items')->where('user_id', '=',  1)->read(); 

You can use the ``or()`` method, ``and()`` method or ``not()`` method along with ``where()`` method like below-

.. code-block:: text

    $items = $db->table('items')->where('user_id', '=',  1)->and(‘price’, ‘<’, ‘250’)->or(‘price’, ‘>’, ‘50’)->where()->not('name', '=', 'buy')->and()->not('name', '=', 'buying')->read(); 

To add extra conditions use the ``condition()`` method-

.. code-block:: text

    $db->table('items')->where('user_id', '=', 1)->condition('AND price > 50')->read(); 

Ordering
~~~~~~~~

Use the ``orderBy()`` method at the end of your conditions to order your results-

.. code-block:: text

    $items = $db->table('items')->where('user_id', '=', 1)->orderBy('created_at', 'desc')->read(); 

Pagination
~~~~~~~~~~

To get paginated data from the database, use the ``limit()`` method before ``read()`` method-

.. code-block:: text

    $items = $db->table('items')->limit(2)->read(); 

Afterwards, you can get a pagination of your query using the ``pagination()`` method-

.. code-block:: text

    $pagination = $db->pagination(); 

Additionally, you can use the ``paginationData()`` method to get necessary pagination data as array-

.. code-block:: text

    $data = $db->paginationData()

Afterwards, pass the array values as parameters to ``generatePages()`` method to generate the pagination-

.. code-block:: text

    $pagination = $db->generatePages($data['page'], $data['totalPages'], $data['url'])

Inserting Data
--------------

To insert data in the database, use the ``create()`` method in combination with ``table()`` method, and ``data()`` method to pass input data array, where keys are the name of the table columns and their values are the input values-

.. code-block:: text

    $db->table('items')->data(['name' => ‘Human’, 'price' => ‘500’])->create(); 

Updating Data
-------------

To update data of a row in the database, use the ``update()`` method in combination with ``table()`` method, and ``set()`` method to pass update data array, where keys are the name of the table columns and their values are the updated values-

.. code-block:: text

    $db->table('items')->set(['name' => ‘update name’])->where('id', '=', 1)->update();

Deleting Data
-------------

Before deleting, CodeCube checks whether ``deleted_at`` column exists in a table. If it does, instead of deleting the column completely, the framework updates the column value to current date-time, and ignores the rows with NOT NULL values for ``deleted_at`` column in ``read()`` method. If the column doesn’t exist, the framework deletes the row completely. To delete a row from a table, use the ``delete()`` method.

.. code-block:: text

    $db->table('items')->where('id', '=', 1)->delete(); 

Raw SQL Query
-------------

You can use the ``get()`` method to directly input a SQL read command-

.. code-block:: text

    $db->get('SELECT name, username FROM users'); 

You can use the ``write()`` method to write raw SQL command to insert, update or delete data into the table.

.. code-block:: text

    $db->write(‘INSERT INTO items (‘name’, ‘price’) VALUES (‘New Item’, ‘100’)’); 

Using SQL Views
---------------

The framework puts extra emphasis on database views for more effective retrieval of database tables. ​You can use the SQL views in combination with CodeCube built-in query builder functions to perform more complex queries.

As an example, you can join **users** and **items** table and save the query as a SQL view-

.. code-block:: text

    CREATE VIEW `items_view` AS SELECT i.id AS id, i.name as name, i.price as price, i.user_id as user_id, u.username AS username, i.created_at AS created_at, i.updated_at AS updated_at, i.deleted_at AS deleted_at FROM items i, users u WHERE i.user_id = u.id

And later, use query builder to read data from the view-

.. code-block:: text

    $items = $db->table('items_view')->where('user_id', '=', 1)->orderBy('created_at', 'desc')->limit(2)->read(); 

Return SQL Command
------------------

To find the last executed SQL command string, use the ``getLastSQL()`` method-

.. code-block:: text

    logger($db->getLastSQL()); 

.. _database-migration:

Migration
---------

Migrations are like version control for your database, allowing your team to easily modify and share the application’s database schema. CodeCube provides a convenient way of migrating your database.

Before migration, you have to create/modify your migration files. To start working on migration files, go to **database** folder. There you will find 4 files for creating and removing tables and views-

.. code-block:: text

    1_drop_view_statements 

    2_drop_table_statements 

    3_create_table_statements 

    4_create_table_statements

There migration files return SQL commands as an associative array and each command with an identifying key. Write your SQL create and drop table/view commands there for all the tables and views you want to create and drop. Make sure to maintain proper order while writing your SQL commands so that the system won’t face conflicts related to foreign key checks while performing migration.

.. code-block:: text

    'create_users' => "CREATE TABLE `users` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL, `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL, `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL, `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL, `created_at` timestamp NULL DEFAULT NULL, `updated_at` timestamp NULL DEFAULT NULL, PRIMARY KEY (`id`), UNIQUE KEY `users_username_unique` (`username`), UNIQUE KEY `users_email_unique` (`email`))"

To insert values to your tables, create new insert files, with an identifying number at the beginning of migration file name to maintain order.

.. code-block:: text

    5_insert_users 

Like the create/drop migration commands, place your insert commands inside a returning array from the migration files with identifying keys for each.

.. code-block:: text

    'insert_users' => 'INSERT INTO `users` VALUES (1,"Default User","codecube","codecube@gmail.com","secret", NULL, NULL);', 

To migrate your database, open terminal in your project root directory and execute the below command.

.. code-block:: text

    php index.php migrate reset

To note, add the second argument ``reset`` only if you want to reset your previously migrated table.
