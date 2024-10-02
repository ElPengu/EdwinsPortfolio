Notes when creating this website
- Created virtual environment with Python
-->py -m venv project-name
-->project-name\Scripts\activate.bat (each time!)

- Pip installed Django onto Python (each time!)
-->py -m pip install Django
- startproject in correct directory
- check server by "python manage.py runserver #PORTNUMBER"
- configure settings - this will allow us to run server with Django directly
- Created playground app
- Added urls.py file
- Map a view (lets say "hello") in views.py to urls.py
- Go to store front and to settings
- We include URLconf that was made in playground/urls.py
- Now default page has no response, but if you navigate to /playground/hello/ you will see a response!
- Go to playground directory, create templates/X.html

-Always set required installations and packages with "pip freeze > requirements.txt"

To connect database to Django app
- Create database on pgadmin
- Update settings to connect to database
- Create model on desired models.py ENSURING that we have a meta class for tables that we 
want to manage on the backend only
- Update admin.py with model imported so that you can see it on admin page
- To access it, you must use pgadmin to grant privileges on that table to the user 
in settings.py
- Also grant privilege to the same one on user_id_seq tab of public in that database on pgadmin

Test user:
Username: test
password: test
email: test@test.com
name: test


Set up env file
pip install dotenv

In file:
"from dotenv import load_dotenv"
"import os"
Create .env file
Put data in new lines in .env file, e.g.... 
USERNAME=GoodName 
API_KEY=1234
Add line
load_dotenv('.env')
To get details in file, if string
username: str = os.getenv('USERNAME')
API_KEY: int = os.getenv('API_KEY')
Add env file to .gitignore file at root directory of github



Tasks to make website
1. Add database for users on postgresql <- 10/9/2024
2. Connect Django app to postgresql database WITHOUT managing table <- 10/9/2024
3. Add basic functionality for a user to optionally register <- 11/9/2024
4. Add basic functionality for a user to optionally log in <- 13/9/2024
5. Create a dash board for logged in users to create a to-do list if they want <- 16/9/2024
6. Extend html for user and add dashboard <- 16/9/2024
7. Add basic front-end for website in general <- 17/9/2024
8. Implement buttons for navigation bar (front-end stuff) <- 18/9/2024
9. Implement front end on to-do list page for a user to delete an item (front-end stuff) <- 18/9/2024
10. Implement front end on to-do list page for a user to edit an item (front-end stuff) <- 20/9/2024
11. Implement JS so that a user must confirm before deleting an item  <- 20/09/2024
12. Add back-end for to-do list *- user <- 20/09/2024
13. Find out how to make migrations (front-end -> back-end) AUTOMATIC! <- 20/09/2024
14. Store password as environment variable <- 20/09/2024
15. Lock out users from the playground app <- 23/09/2024
16. Prevent an already logged in user from logging another account <- 23/09/2024
17. Recorded website to show how it looks as of now! <- 23/09/2024
18. Alter navigation bar based on whether you are signed in or signed out <- 23/09/2024
19. Optimise main page by removing the filler stuff <- 24/09/2024
20. Add a dividing line between rows in to-do list <- 26/09/2024
21. When you 'complete' task, set Date completed to the chosen date <- 26/09/2024
22. Require confirmation on update <- 26/09/2024
23. Create requirements.txt file to make website deployment easier <- 30/09/2024
24. Publish website for others to access <- 30/09/2024
25. Set up database to work with published website <- 1/10/2024
26. Set article, section, and aside to squash correctly <- 1/10/2024
27. Set table to scroll if too big <- 1/10/2024
28. Find out how to how two slightly different branches with GitHub (this allows me to work on the website on my local host as well as on PythonAnywhere whilst they are slightly different) <- 1/10/2024
29. Ensure that article, section, and aside do not squash over each other when window changes size <- 1/10/2024
30. Set up username and password and secret key for online database in hidden .env file <- 1/10/2024
31. Set contact us form for email where subtitle and message can be sent to my address <- 1/10/2024
32. Fixed email filtering so that all the messages from my site are filtered out of my own inbox (so that my inbox is not filled with those test messages!) <- 1/10/2024
33. Made input fields required across all forms (e.g. sending message, logging in, etc.)<- 1/10/2024
34. Set password to be hidden instead of in plaintext <- 2/10/2024
35. Set email to field to require input of type email <- 2/10/2024
36. Set a fake account for curious people to explore the capabilities of the to-do list <- 2/10/2024

Tickets
- Re-introduce Kiswahili button + adjust CSS for navbar elements to fit 3 elements instead of 2 (50% -> 33.33%)
- Use JavaScript to enable change between English and Kiswahili
- Set a good colour scheme for website
- Investigate how to design a personal website
- Investigate how to design a good website in general
- Find out web design practises with highest ROI by seeing how to 
- Have update item expand editable items when you click (on something)
- Let user know when an email has been successfully sent (HINT: use JavaScript, HTML/CSS isn't working)
- Allow users to view their password
- Investigate why only parts of hidden .env file work
- Add page for users to see their credentials
- Allow users to update their credentials
- Add an image of a donkey for donkey site
- Extend message entry box



To deploy site (https://www.youtube.com/watch?v=xtnUwvjOThg&t=473s):
Ensure that settings.py in Django project will correctly route to base.html
Log into pythonanywhere
Go to bash console
"pwd"
"git clone repository"
Delete all irrelevant directories
"mkvirtualenv venv"
"pip install -r requirements.txt"
Open new tab 2 and go to dashboard
ENTER TAB 2- Add a new web app
Select python 3.10
Manual configuration
Scroll down to virtualenv
Input venv
Go to wsgi configuration file, should be above the virtualenv section
Remove all but top to end of general debugging tips, and the Django section (so about lines 74-89)
Uncomment lines according to video
ENTER ORIGINAL TAB -Bash console
cd into app so you see "db.sqlite3  manage.py"
pwd and copy path, something like "/home/Pingu03/FirstFullWebsiteEdwin"
ENTER TAB 2
Set path = '/home/Pingu03/FirstFullWebsiteEdwin'
SET TAB 3 -  WEB
ENTER TAB 3
Copy url, found somewhere like "Configuration for Pingu03.pythonanywhere.com"
Copy url
Go to Files
Go to settings.py
Update lines:
"DEBUG = False

ALLOWED_HOSTS = ['Pingu03.pythonanywhere.com']"
ENTER TAB 2
Set line to something like "os.environ['DJANGO_SETTINGS_MODULE'] = 'FirstFullWebsiteEdwin.settings'"


SETTING UP DATABASE ON PYTHONANYWHERE
Go to bash
Activate venv
pip install --upgrade pip
pip install pymysql
Go to databases, then MySQL
Set a password and initialise MySQL
Copy database host address, this is HOST
Copy username, this is USER
Copy Name, this is NAME
Open a text editor and write the following, filling in where appropriate
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': '...',
'USER': '...',
'PASSWORD': '...',
'HOST': '...',
'PORT': '3306',
'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
}
}
Add new lines for DATABASES in settings.py to reflect these changes
Comment out original DATABASES in settings.py
Go to __init.py__
Add following lines
import pymysql

pymysql.install_as_MySQLdb()

Now we run the migrations and create a superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver <- Unneeded line, the web server already uses the port
