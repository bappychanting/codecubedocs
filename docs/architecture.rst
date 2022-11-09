Architecture Concept
====================

The entry and exit point of the whole framework is **index.php** file. This file includes the application configuration files to configure the settings, autoload files to include all the base classes and functions, and route files to call method of a controller class defined for the current URL. All of these are done within a **try catch** function, which reports error if any exception is found while performing an action.  

The framework follows **MVC** (Model, View, Controller) pattern. How the general flow of activities follows this design pattern within this framework is explained below-

* Models are where all the classes based on the real life entities associated with the program, their relations, objects and methods are defined, and **OOP** (Object Oriented Programming) concept is applied on top of them. This is where different **CRUD** (create, retrieve, update, delete) actions are generally performed and passed to the Controller.  
* Controllers retrieve data returned from model, perform necessary actions on them and pass it to the view. Generally access control logic is applied here as well. 
* Views are used to construct visual layout and present the data to the user. 

Additionally, apart from working on models, views and controllers: 

* Various base classes and functions from **base** folder (located in **vendor/codecube** directory) can be called to follow the standard way of accessing database, input validation, defining layouts, connecting models , controllers and views etc.
* Methods from helper classes, or classes included by composer dependency can be called to perform certain actions on the data anywhere within the system.
* Controller will call method from guard classes to implement access control logic.