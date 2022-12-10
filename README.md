# first_webapp

### Django project
First web application using Django

* Creating Virtual Environment 

    `$ python3 -m venv <name>`

* Activate virtual environment 

    `$ source <name>/bin/activate`
    
* Deactivate virtual environment
    
    `$ deactivate`
    
* Store Installed package

    `$ pip3 freeze > requirements.txt`
    
* To see installed packages.

    `$ cat requirements.txt` 

* Install Django

    `$ pip3 install Django`

* Create a Project in Django 

    `$ django-admin startproject <folder_name> .`

* Create the Database 

    `$ python3 manage.py migrate`

* Run the server / view the project using local host (127....)

    `$ python3 manage.py runserver`


* Starting Application

    `$ python3 manage.py start.app <unique foldernames>`

* Tell Djanjo to modyfing Database

    `$ python3 manage.py makemigrations <unique foldernames>`

* setup a superuser

    `$ python3 manage.py createsuperuser`

* The Django shell

    `$ python manage.py shell`

### Git command

* Setting the name for commit transactions

    `$ git config --global user.name <name>`

    For example:

    `$ git config --global user.name labhiCS`

* Setting the email for commit transactions

    `$ git config --global user.email <email>`

    For example:

    `$ git config --global user.email lamichhaneabhi10@gmail.com`

* For colorization of commandline output

    `$ git config --global color.ui auto`

* To see running networkstatus.

    `$ sudo netstat -lpn`

* To kill the running tab(program).

    `$ kill -9 <PID/Program name>`