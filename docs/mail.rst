Mail
====

CodeCube provides a base​ Mail (built on top of ​PHPMailer class) class to make sending emails easier. Before sending mail, you must provide your mail configuration values to the Mail Constants in the ​env.php​ file to configure mail.

const MAIL_DRIVER='smtp'; 
const MAIL_HOST='smtp.mailtrap.io'; 
const MAIL_PORT='2525'; 
const MAIL_USERNAME= ‘codecube’; 
const MAIL_PASSWORD= ‘pass’; 
const MAIL_ENCRYPTION= ‘ssl’; 

You can also provide values for the XML tags in the resources/markups/mail.xml file to send a stylized email with header and footer.

<mail> 
<style>body {background-color: lightblue;}</style> 
<header>Email Header</header> 
<footer>Email Footer</footer> 
</mail>

Once everything is set up, use the setter methods to set up mail receivers, sender, carbon copies, blind carbon copies, subject and message like below. You need to pass an array consisting of appropriate emails as parameter for setting up receivers, carbon copies or blind carbon copies. Use the createMessage() method to include the XML layout. If you want to include any XML file other than resources/markups/mail.xml containing tags for mail (the file must be in the resources/markups directory), you can pass the name of the file as the parameter of this method. Finally use​ send() method to send the mail.

use Base\Mail; 
$mail = new Mail;  
$mail->setReceivers($receivers);  
$mail->setSender($sender); 
$mail->setCarbonCopies($cc); 
$mail->setBlindCarbonCopies($bcc); 
$mail->setSubject($subject); 
$mail->setMessage($message);  
$mail->createMessage()->send(); 

