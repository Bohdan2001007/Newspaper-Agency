# Newspaper-Agency
Django project that helps redactors to add/update/delete topics and newspapers in a convenient service
# Base structure of project 
![Base structure](https://github.com/Bohdan2001007/Newspaper-agency/blob/main/drawio.png)
# Installation
git clone https://github.com/Bohdan2001007/Newspaper-agency
cd Newspaper-agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver # starts Django Server
