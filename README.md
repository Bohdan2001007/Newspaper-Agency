# Newspaper-Agency
Django project that helps redactors to add/update/delete topics and newspapers in a convenient service
# Base structure of project 
![Base structure](/static/drawio.png)
# Installation
- git clone https://github.com/Bohdan2001007/Newspaper-agency
- cd Newspaper-agency
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

# Secret information in .env file

- SECRET_KEY

- PASSWORD_DB

- You need to create .env file to store secret information

# Website

Link of website: https://newspaper-agency-06io.onrender.com

Use the following command to load prepared data from fixture to get demo access to the system:

python manage.py loaddata Newspaper_Agency_db_data.json.

After loading data from fixture you can use following superuser (or create another one by yourself):

login: user

password: user12345

# Landing page
![Landing page](/static/Landing_page.png)
