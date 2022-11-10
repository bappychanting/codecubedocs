Helpers
=======

Helpers are classes with functions that help you to avoid repetition of codes and perform certain tasks easier within the application. CodeCube supplies some built-in helper functions and developers can easily add helpers of their own. All helper classes are stored in ​app/Helpers​ directory.

By default, CodeCube provides tree helper classes- ApiHelper, Misc & Upload. To access their functionalities, include the classes at the top of your PHP file.

use App\Helpers\ApiHelper; 
use App\Helpers\Misc;  
use App\Helpers\Upload; 

Their functions are explained below

    ApiHelper::request() Method: Returns all the parameters received from an API call (headers, params and body) as an array. 

print_r(ApiHelper::request());

    ApiHelper::validator() Method: Returns the input validation messages in intended API format. 

ApiHelper::validator(['email' => 'email required'], 'Validation failed!');

    ApiHelper::success() Method: Returns the requested data along with a success message in intended API format . 

ApiHelper::success(['users' => $all_users], 'Success!');

    ApiHelper::fail() Method: Returns a failure message in intended API format . 

ApiHelper::fail('Exception found!', ['auth' => 'api authentication failed'], 5001, 401);

    ApiHelper::response() Method: Here you can define the format for showing your API results. You can also call this method directly if you need to show data that are not compatible with aforementioned helper methods.

ApiHelper::response(['message' => 'The requested user has not been verified!', 'error' => ['email' => 'email address not found'], false, 400);

    Misc::pluck() Method: Returns an array consisting of values of a key from a multidimensional array. 

Misc::pluck($users, ‘name’); 

    Misc::randInt() Method: Creates a random number of specific length

Misc::randInt(10)

    Misc::randStr()​ Method: Creates a random string of given length. 

Misc::randStr(10);

    Misc::urlString()​ Method: Creates an SEO friendly URL of a given text. 

Misc::urlString(‘New Item’, ‘-’);

This will return string new-item.

    Misc::substrwords()​ Method: Will cut a string to the given length.

Misc::substrwords(‘Keeps the first five letters’, 5); 

    Misc::generateColor()​ Method: Generates random html colors.

    Misc::generateYearArray() Method: Returns start and end ​UNIX timestamp of all the months from this year to the number of previous years passed as parameter.

Misc::generateYearArray(1); 

Misc::createCalendarDateRange() Method: Returns an array containing all the days of the week and all the dates of a given date range. This method helps to create a PHP calendar.

Misc::createCalendarDateRange(‘2019-01-01’, ‘2019-12-31’); 

    Upload::fileUpload() Method: Will upload files to the server and return the upload directory. 

Upload::fileUpload($_FILES['file'], $app['upload'].'/myfiles'); 

    Upload::imageUpload() Method: Resizes and uploads image while checking file format. If you want to keep the original image aspect ratio while resizing, set the final parameter as true . It returns the upload directory.

Upload::imageUpload($_FILES['file'], $app['upload'].'/myfiles', 640, 480, true); 

    Upload::imageUploadWithThumb() Method: Resizes and uploads full size image while checking file format and adds a thumbnail of the image of given size afterwards. Set the thumbnail extension word, thumbnail width and height by passing arguments. If you want to keep the original image aspect ratio while resizing, set the final parameter as true . It returns the upload directory.

Upload::imageUploadWithThumb($_FILES['file'], $app['upload'].'/myfiles', '_thumb', 640, 480, true); 

    Upload::resizeImage() Method: Resizes an uploaded image. 

Upload::fileUpload($app['upload'].'/myimages/uploaded.jpeg', 640, 480, true); 

