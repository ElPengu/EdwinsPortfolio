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
23. Create requirements.txt file to make website deployment easier <- WE ARE HERE
24. Publish website for others to access <- WE ARE HERE


Tickets
- Use JavaScript to enable change between English and Kiswahili
- Set a good colour scheme for website
- Investigate how to design a personal website
- Investigate how to design a good website in general
- Find out web design practises with highest ROI by seeing how to 
- Ensure that article, section, and aside do not squash over each other when window changes size
- Require confirmation for update, just like for delete
- Have update item expand editable items when you click (on something)


To deploy site (https://www.youtube.com/watch?v=xtnUwvjOThg&t=473s) DOESN'T WORK:
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

TEST LINE

