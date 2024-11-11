# Django project.

web application and its API!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Introduction

This project is a Django project that was created using the Cookiecutter Django project. It is a sample web and rest api Django project where 
- upon successful login into the web application, a sample D3 chart is rendered on web page.
- upon successful authentication into the Rest API, the data for the same chart can be requested via the API command.

## Instructions to run the project locally:

- create your preferred folder for the project:

      mkdir folder_name

- create an environment for the project:

      pyenv virtualenv 3.10.0 your_project_env

- activate the environment:

      pyenv activate your_project_env

- clone the project:

      git clone https://github.com/your_username/your_project_name.git

- change the directory to the project:

      cd your_project_name

- to create a superuser:

      python manage.py createsuperuser
      ( follow the instructions )

- install the requirements:

      pip install -r requirements.txt

      npm install

- run the project:
      python manage.py runserver

- open the project in your browser:

      http://127.0.0.1:8000/ ( depends on your settings )

- to access the admin panel, go to:

      http://127.0.0.1:8000/admin/

- to access the api endpoints, go to:

      http://127.0.0.1:8000/charts/api/chart/


