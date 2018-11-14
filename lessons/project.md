# DRAFT - DO NOT START

## Task 1 - Registration
Write a Python script called ```register_user.py``` that asks the user to enter an email and a password and appends them in ```users.csv``` in the following format:
~~~
user1@mail.ru,Pazhalooysta
user2@mail.in,Namaste
~~~
Specifications:
* Perform some basic validation on the email (at least check for 5 properties)
* The password cannot be shorter than 5 characters and must contains 2 of the following:
  * lowercase letter
  * uppercase letter
  * number
* Keep asking the user to enter the details again, until they are valid
* Use proper exit codes if something does wrong while using the CSV file

## Task 2 - Web Server
Write another script ```server.py``` that will act as a web server running on localhost:8080  
Specifications:
* Listen only to GET requests
* Show the login page by default
* Takes directory path a command line argument, this will be the base directory.

### Login Page (/login): 
* Display a Login Page form (```login.html```) with input fields for email and password
* If the credentials match one of the entries in ```users.csv``` show the welcome page
* Show the login page again if login fails

### Welcome Page: 
* Available only after valid login (no direct URL)
* Contains the following links:
  1. List of all base directory TXT files
  2. List of the base directory TXT files that changed int he last 24 hours
* Both lists should be made up of links that allows the user to download the files
