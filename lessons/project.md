# DRAFT - Might still change

## Task 1 - Registration
Write a Python console application called ```register_user.py``` that when executed offers the user a menu with 3 options:
1. List all users 
2. Add new user  
3. Exit

The application uses a CSV file called ```users.csv``` that has the following format:
~~~
user1@mail.ru,Pazhalooysta1
user2@mail.in,Namaste2
~~~
Use proper exit codes if something goes wrong while using the CSV file. Use functions as much as possible to make your code more readable and proper DocStrings to document each function.

### List all users
Lists all the user in the CSV file in a numbered, one user per line as shown below:
~~~
1. user1@mail.ru
2. user2@mail.in
~~~

### Add new user
Asks the user to enter an email and a password and appends them to the CSV file. Specifications:
* Perform some basic validation on the email, at least you should have 5 validation rules.
* The password cannot be shorter than 5 characters and must contain all of the following:
    * lowercase letter
    * uppercase letter
    * number
* Keep asking the user to enter the details again, until they are valid.

## Task 2 - Drive scanning module
Write a Python module ```dirscanner.py``` that contains a function ```scan()``` which takes two parameters:
1. A directory path (e.g.: 's:\myfiles')
1. An extension (e.g.: '.txt')
The function should return a list of file names found in the directory that have been modified within the last 24 hours. Use proper DocString to document your module.

## Task 3 - Web server
Write a final script ```server.py``` that will act as a web server running on localhost:8080 with the following specifications:
* Listens only for GET requests (ignore POST etc.)
* Create a Login Page (a file called ```login.html```) containing a HTML form with input fields for email and password. Show this login page by default (if GET does not specify file to show). The form action should be ```/login```.
* Takes a path as a command line argument, this will be the referred to as **base directory**. Do not run the server if this is missing or invalid.
* Credential validation: Your script must contain a function called ```valid_creds(email, pw)``` that opens ```users.csv```, checks if any row matches the parameters and returns True/False accordingly
* Use functions as much as possible to make your code more readable and proper DocStrings to document each function.

### Login feature (/login): 
* Receives requests from the login form
* Uses ```valid_creds()``` to check if the credentials match:
    * Show the main page if they match
    * Else show the login page again.

### Main page: 
* Available only after valid login (no direct URL)
* Contains a list of all TXT files in the base directory that changed in the last 24 hours (using ```dirscanner.scan()```) 

### Download file (/getfile?f=xyz.txt): 
* Both lists in the main page should be made up of links that allows the user to download the files.
* When one of these links are clicked, you need to fetch the specified file from the base directory:
    * If found, open it and send it to the user
    * If not found, send a 404.
