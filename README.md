# css475finalproject
Project Documentation

#SETUP:


Install django
Pip install psyocpg2
(Recommended) Virtual environment folder ```- python -m venv django env```
Run VE:  ```source./django env/bin/activate```
Rest Framework


How to Run: 

Take the tutordb.txt, and create it as a database within postgres
You can use tutordbvalues.txt to input test values into your database, or create your own


In the terminal, write:

1.) python manage.py makemigrations
2.) python manage.py migrate
3.) python manage.py runserver
4.) open the provided url

When opening the url you should see a page with all the tables listed, you can click on each table to go to it’s page 
(NOTE: As of right now, the User login system isn’t complete, so in order to access the data, you need to first create a super user, and login from your url/admin before you can view the files, otherwise the database will not grant you permission)

In addition you can use 

'student-grades/<int:student_id>/'
'class-info/<int:class_id>/'

To access different methods, though they also require admin. 
