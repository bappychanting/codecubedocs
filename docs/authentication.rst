Authentication
==============

CodeCube provides built-in Authentication class for easier implementation of authentication. To access its functionalities, call the class at the top of your PHP file like below-

use Base\Authenticable; 

Sign In/Sign out

Once called, you can use its ​signin() function to authenticate a user to the system. The method will check whether any user’s email or username matches with the passed identity, and if found, signs the user in to the system.

$auth = new Authenticable; 
$auth->signin(‘identity’, ‘password’); 

You can pass in the name of your “remember me” checkbox as the third parameter to the signin() method if you want to enable persistent login cookies for your authentication.

$auth->signin(‘identity’, ‘password’, 'remember'); 

Once authenticated, you can use the ​getAuth()​ method to get authenticated user data.

$auth_user = $auth->getAuth(); 

You can use the ​check() method to check whether a user is authenticated.

echo $auth->check() ? ‘authenticated’ : ‘not authenticated’; 

You can sign out the user using the ​signout()​ method.

auth->signout(); 

Password Reset

While resetting password, use the​ storelink() method with a unique string and user Id as its parameters to store reset links. The unique string will be stored as password reset link parameter to make the link only accessible by the requesting user-

$auth->storeLink(md5(uniqid()), 1); 

Pass the token as a parameter to the ​getLink() method to check whether the token exists and get other information for the requesting user once the user clicks on the unique password reset link. ​

$auth->​getLink​($_GET[‘token’]); 

Once the user resets his password, you can set the unique token invalid using the updateValidity()​ method so that it won’t be accessible anymore.

$auth->updateValidity($token);

