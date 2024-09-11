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

To connect database to Django app
- Create database on pgadmin
- Update settings to connect to database
- Create model on desired models.py ENSURING that we have a meta class for tables that we 
want to manage on the backend only
- Update admin.py with model imported so that you can see it on admin page
- To access it, you must use pgadmin to grant privileges on that table to the user 
in settings.py
- Also grant privilege to the same one on user_id_seq tab of public in that database on pgadmin

Tasks to make website
1. Add database for users on postgresql <- 10/9/2024
2. Connect Django app to postgresql database WITHOUT managing table <- 10/9/2024
3. Add basic functionality for a user to optionally register <- 11/9/2024
4. Add basic functionality for a user to optionally log in <- WE ARE HERE
5. Add front-end for to-do list for a user (ADD, DATE MADE, NAME, DESCRIPTION (OPTIONAL), COMPLETION)
6. Add back-end for to-do list *- user
7. Store password as environment variable
8. Find out how to make migrations AUTOMATIC!