Localization
============


Introduction

CodeCube’s localization features provide a convenient way to retrieve strings in various languages, allowing you to easily support multiple languages within your application. Language strings are stored in files within the resources/locale directory. Within this directory there should be a subdirectory for each language supported by the application:

/resources
    /locale
        /en
            message.php
        /es
            message.php

All language files return an array of keyed strings. For example:

<?php
return [
    'info' => 'This is a info alert!',
];

Configuring The Locale

The default language for your application is stored in the config/app.php configuration. You can change your preferred language by changing value of the locale key, which is set as en (English) by default. Here en is the name of the folder containing your language files.

'locale' => 'en', // configuration for default locale

Retrieving Translation Strings

You can retrieve texts from the language files using the locale() method. Pass the name of the file as the first parameter and the name of the key as the second parameter.

echo locale('message', 'info');

Above code will display ‘This is a info alert!’ text from the message language file.

If you wish, you may define placeholders inside any of the array of strings inside a locale file. All placeholders are prefixed with a :. For example, you may define a validation message with a placeholder ‘:data’:

'empty' => ':data can not be empty!',

To replace the placeholders when retrieving the string, pass an array of replacements as the second argument to the locale() method.

echo locale('validation', 'empty', ['data' => 'Name']);

Above code will display “Name cannot be empty”, replacing the ‘:data’ placeholder.
