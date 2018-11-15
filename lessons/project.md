# DRAFT - Might still change

## Task 1 - Registration
Write a Python script called ```register_user.py``` that asks the user to enter an email and a password and appends them in ```users.csv``` in the following format:
~~~
user1@mail.ru,Pazhalooysta
user2@mail.in,Namaste
~~~
Specifications:
* Perform some basic validation on the email, at least you should have 5 validation rules.
* The password cannot be shorter than 5 characters and must contains 2 of the following:
  * lowercase letter
  * uppercase letter
  * number
* Keep asking the user to enter the details again, until they are valid
* Use proper exit codes if something does wrong while using the CSV file

## Task 2 - Drive scanning module
Write a Python module ```dirscanner.py``` that contains a function ```scan()``` which takes two parameters:
1. A directory path
1. An optional extention (e.g. .txt)
The function should return a list of files found in the directory. Uswe proper DocString to ducument your module

## Task 3 - Web server
Write another script ```server.py``` that will act as a web server running on localhost:8080  
Specifications:
* Listen only to GET requests
* Show the login page by default
* Takes directory path a command line argument, this will be the base directory.

### Credential validation
Your script must contain a function called ```valid_creds(email, pw)``` that opens ```users.csv```, checks if any row matches the paameters and returns True/False accordingly

### Login page (/login): 
* Display a Login Page form (```login.html```) with input fields for email and password.
* If the credentials match, using ```valid_creds()```, show the main page, else show the login page again.

### Main page: 
* Available only after valid login (no direct URL)
* Contains the following lists (using ```dirscanner``` module):
  1. List of all base directory TXT files
  1. List of the base directory TXT files that changed int he last 24 hours
* Both lists should be made up of links that allows the user to download the files
