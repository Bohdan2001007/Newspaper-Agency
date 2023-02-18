# Newspaper-Agency
Django project that helps redactors to add/update/delete topics and newspapers in a convenient service
# Base structure of project 
![Base structure](https://github.com/Bohdan2001007/Newspaper-agency/blob/main/drawio.png)
# Installation
- git clone https://github.com/Bohdan2001007/Newspaper-agency
- cd Newspaper-agency
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
# Demo
Use the following command to load prepared data from fixture to test and debug your code:

python manage.py loaddata taxi_service_db_data.json

After loading data from fixture you can use following superuser (or create another one by yourself):

Login: admin.user
Password: bestpassword

python manage.py loaddata taxi_service_db_data.json

After loading data from fixture you can use following superuser (or create another one by yourself):
Login: admin.user
Password: bestpassword
![Landing page](https://github.com/Bohdan2001007/Newspaper-agency/blob/main/Landing%20page.png)
