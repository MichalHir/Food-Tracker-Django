# project1_foodTracker

<!-- 1. **Create and activate a virtual environment:**
    - python -m venv venv
    - source venv\Scripts\activate
    - pip install -r requirements.txt
2. Create the database and superuser
    - python manage.py migrate
    - python manage.py createsuperuser

4. run the server
    - python manage.py runserver

5. add some products in admin or shell and navigate to 'http://127.0.0.1:8000/products/' -->


Setup environment
Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate

pip freeze > requirements.txt
pip install -r requirements.txt

django:
pip install django
django-admin startproject food_tracker .
python manage.py startapp (name)

Create the database and superuser
python manage.py makemigrations ...
python manage.py migrate
python manage.py createsuperuser

run the server
python manage.py runserver
Python manage.py shell

add some products in admin or shell and navigate to 'http://127.0.0.1:8000/products/'

michal
michal@gmail.com
1234

create a new repository on the command line:
echo "# task-list" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MichalHir/task-list.git
git push -u origin main

push an existing repository from the command line:
git remote add origin https://github.com/MichalHir/task-list.git
git branch -M main
git push -u origin main