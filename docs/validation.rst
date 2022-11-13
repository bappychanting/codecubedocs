Form Validation
===============

You can define form validation roles in either model or controller. To set the validation roles, you can declare an array, and then define each validation error text as a key of the array like below-

.. code-block:: text

    $errors = array(); 
 
    if($_POST[‘name’]){ 
     $errors['name'] = "Name can not be empty!"; 
    }  
     
    if($_POST[price]){ 
     $errors['price'] = "Price can not be empty!"; 
    } 

Once you’ve defined each validation roles, you have to pass the array to ``setErrors()`` method as parameter to get the errors in the view page.

To show the error in the view page, use the ``field_err()`` method like below-

.. code-block:: text

    <span><?php echo field_err('name'); ?></span> 

To get all the errors found in the view page they were submitted from, use the ``getErrors()`` method.

.. code-block:: text

    <p><?php print_r(getErrors()); ?></p>

Get Previously Submitted Values
-------------------------------

To get the submitted post values back in the view page they were submitted from, use the ``field_val()`` method.

.. code-block:: text

    <input type="text" name="name" value="<?php echo field_val('name'); ?>"