# DRAFT - Might still change

## Task 1 - Registration
Write a Python console application called ```register_user.py``` that when executed offers the user a menu with 3 options:
1. List all users 
2. Add new user  
3. Exit

The application uses a CSV file called ```users.csv``` that has the following format:
~~~
user1@mail.ru,Pazhalooysta
user2@mail.in,Namaste
~~~
Use proper exit codes if something goes wrong while using the CSV file.

### List all users
Lists all the user in the CSV file, one user per line. At the end, print out the total number of users.

### Add new user
Asks the user to enter an email and a password and appends them to the CSV file. Specifications:
* Perform some basic validation on the email, at least you should have 5 validation rules.
* The password cannot be shorter than 5 characters and must contains 2 of the following:
  * lowercase letter
  * uppercase letter
  * number
* Keep asking the user to enter the details again, until they are valid.

## Task 2 - Drive scanning module
Write a Python module ```dirscanner.py``` that contains a function ```scan()``` which takes two parameters:
1. A directory path (e.g.: 's:\myfiles')
1. An optional extention (e.g.: '.txt')
The function should return a list of files found in the directory. Use proper DocString to ducument your module.

## Task 3 - Web server
Write a final script ```server.py``` that will act as a web server running on localhost:8080 with the following specifications:
* Listens only for GET requests (ignore POST etc.)
* Create a Login Page form (a file called ```login.html```) with input fields for email and password. Show this login page by default (if GET does not specify file to show). The form action should be '/login'
* Takes a path as a command line argument, this will be the referred to as **base directory**.
* Credential validation: Your script must contain a function called ```valid_creds(email, pw)``` that opens ```users.csv```, checks if any row matches the paameters and returns True/False accordingly

### Login feature (/login): 
* Recieves requests from the login form
* Uses ```valid_creds()``` to check if the credentials match:
    * show the main page if they match
    * else show the login page again.

### Main page: 
* Available only after valid login (no direct URL)
* Contains the following lists (using ```dirscanner``` module):
  1. List of all TXT files in the base directory
  1. List the TXT files in the base directory that changed in the last 24 hours

### Download file (/getfile?f=xyz.txt): 
* Both lists in the main page should be made up of links that allows the user to download the files.
* When one of these links are clicked, you need to fetch the specified file from the base directory:
    * If found, open it and send it to the user
    * If not found, send a 404.
