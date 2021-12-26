@echo off
python -m venv venv
CALL .\venv\Scripts\activate
pip install -r ./src/requirements.txt
cd .\src
python manage.py migrate
python manage.py runserver
