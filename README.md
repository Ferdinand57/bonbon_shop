Create a README.md that contains a link to the PWS application that has been deployed, as well as answers to the following
=

link to the PWS application that has been deployed: http://ferdinand-bonfilio-bonbonshop3.pbp.cs.ui.ac.id/ 

Deployment credential:

Username: ferdinand.bonfilio

Password: 7JXF1pfW50QGYbzwQhTK6lBc04pVu3Qq


Explain how you implemented the checklist above step-by-step (not just following the tutorial).
=

Create a new Django project.
=

1. create a new directory and give it your project name (in this example i used "bonbon_shop")
2. open command prompt
3. the the cd command to your directory, example >cd C:\Users\ferdi\OneDrive\Desktop\bonbon_shop
4. if done correctly your cmd will looks like this (C:\Users\ferdi\OneDrive\Desktop\bonbon_shop>)
5. Initializing a Django Project

   a. run the following command on cmd
   ```
   >python -m venv env
   ```
   b. run the following command on cmd
   ```
   >env\Scripts\activate
   ```

   c. if done correctly your cmd will looks like this: (env) C:\Users\ferdi\OneDrive\Desktop\bonbon_shop>

   d. create a text file and name it requirements, should look like this: requirements.txt or requirement (have .txt attribute in it's properties)

   e. put all the following each on a different line without any space

   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```

   f. run the following command on cmd
   ```
   >pip install -r requirements.txt
   ```
   g. run the following command on cmd
   ```
   >django-admin startproject "project name here" .

   !!! yes the "." is necessary, example >django-admin startproject bonbon_shop .
   ```



   h. go inside (using file explorer not with cmd) your project directory (the one with your project name that you've just created) and find the settings.py

   j. somewhere inside settings.py there is ALLOWED_HOSTS = ['there might be somthing here'], modify it (not add another ALLOWED_HOSTS) to look like this

   ```
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
   
   k. if done correctly your terminal/cmd still looks like this: (env) C:\Users\ferdi\OneDrive\Desktop\bonbon_shop>

   l. run the following command on cmd
   ```
   >python manage.py runserver
   ```
   m. http://localhost:8000 check here, if there is a rocket ship then you've succesfully create a new django project

   n. manually press ctrl + c on the command prompt to stop server


Create an application with the name main in the project.
=

1. if you've done the previous steps correctly your terminal/cmd still looks like this: (env) C:\Users\ferdi\OneDrive\Desktop\bonbon_shop>

2. run the following command on cmd
```
>python manage.py startapp main

!!! (folder named main should show up on your root directory)
```
3. using your file explorer, find the settings.py inside your project directory just like we did previously

4. inside settings.py, find INSTALLED APPS just like we did previously in settings.py with ALLOWED_HOSTS, and append the following 'main', (the quotation and ',' is necessary)

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
```

5. now from root directory, go inside main, in main create a new folder named templates, inside templates create main.html filled with the following

```
<h1>Bonbon's Shop</h1> <!-- Change according to your project name -->

<h5>NPM: </h5>
<p>{{ npm }}<p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

6. next we modify models.py in the main directory (same directory as settings.py and templates folder) to the following

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
```

7. run the following command on cmd
```
>python manage.py makemigrations
```
8. run the following command on cmd
```
>python manage.py migrate

!!! (Every time you make changes to the model, such as adding or changing attributes, you MUST perform migrations to reflect these changes.)
```

Perform routing in the project so that the application main can run.
=
1. create urls.py in the same directory as views.py (inside main directory) and fills it with the following
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```





Create a model in the application main with the name Product and have the mandatory attributes as follows: name, price, description
=
1. go to your root directory, go to your main directory, go inside models.py and add the following class
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
'''
REMINDER: if changed run the following on local repo folder
>python manage.py makemigrations
>python manage.py migrate
'''
```

Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.
=
1. modify the views.py (located in the same directory as models.py, and templates folder) to the following

from django.shortcuts import render
```
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```


Create a routing in urls.py for the application main to map the function created in views.py.
=

1. now find urls.py inside our project directory (the one that has our project name in this case bonbon_shop) and modify the area around urlpatterns to look like this (the "from django.urls import path, include" is necessary)
```
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```


2. run the following command on cmd
```
>python manage.py runserver
```
3. Open http://localhost:8000/ in your favorite web browser to view the page you have created.



Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
=

1. go here https://pbp.cs.ui.ac.id
2. login
3. create new project in this case bonbonshop
4. save the deployment credential and add https://pbp.cs.ui.ac.id/ferdinand.bonfilio/bonbonshop2 to ALLOWED_HOSTS on project directory settings.py
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1","https://pbp.cs.ui.ac.id/ferdinand.bonfilio/bonbonshop2"]
```
5. if all done correctly our terminal should looks the same all this time, that is: (env) C:\Users\ferdi\OneDrive\Desktop\bonbon_shop>
6. add a .gitignore file on our root directory (the same directory as main folder, project folder, manage.py) filled with this

``` code

# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml
.DS_Store

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history



```

7. activate the link betweenn local repo to git repo:

   a. run the following command on cmd
   ```
   >git init
   ```
   b. run the following command on cmd
   ```
   >git branch -M main

   ```
   c. run the following command on cmd
   ```
   >git remote add origin https://github.com/Ferdinand57/bonbon_shop.git
   ```
   d. run the following command on cmd
   ```
   >git add .
   ```
   e. run the following command on cmd
   ```
   >git commit -m "insert something here"
   ```
   f. run the following command on cmd
   ```
   >git branch

   !!! (to make sure you are on main branch, if not run >git branch -M main)
   ```
   g. run the following command on cmd
   ```
   >git push -u origin main
   ```

9. run the following command on cmd
```
>git remote add pws https://pbp.cs.ui.ac.id/ferdinand.bonfilio/bonbonshop2
```
10. run the following command on cmd
```
>git branch -M master
```
11. run the following command on cmd
```
>git push pws master
```


Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.
=

from client point of view

[client request] --> [django web server] --> [response]

inside website server:

[client request] --> [[url.py] --> [views.py] --> [models.py] --> [html file]] --> [response]

Client request: Imagine you are visiting a website. When you type a URL (like http://ferdinand-bonfilio-bonbonshop3.pbp.cs.ui.ac.id) and press enter, what you are doing is you are making a request to the website's server

1. urls.py: 
    The first stop for your client request is the urls.py file, this file acts like a guide or a map that tells the server "When a user visits this URL, send them to the appropriate part of the brain to be processed" it matches the URL to a function in views.py

2. views.py: 
    Think of views.py as the brain behind the scenes, when the client request reaches this part, it figures out what needs to be done, it could be as simple as showing a page or it could involve doing some work like pulling information from a database or performing calculations

3. models.py: 
    If the brain (views.py) needs to talk to the website's memory (the database), it uses models.py. This file defines the structure of the data the website uses (like class in python), so if you’re looking at a list of products or blog posts, models.py helps fetch that information from the database

4. HTML File: 
    Once the brain (views.py) has done its work, it needs to send a response back to you. This response is usually a webpage written in HTML, which is a language used to create the structure of websites. The HTML file organizes the information into something you can see, like text, buttons, and images

HTML Response: Finally, the server sends this webpage back to your browser, and you see it displayed on your screen

It's like buying a sandwich in a restaurant: 
    the server (urls.py) listen to the request and deliver it to the appropriate sandwich department, the chef (views.py) review the order and begin to make the sandwich, the chef retrieves the ingredients from the database (in this analogy the models.py), and then the HTML brings you the sandwich

Explain the use of git in software development!
=

Git is a version control system (VCS) used in software development to help manage and track changes to our code over time. It has several uses in software development including but not limited to:

1. Tracking Changes

   Writing code is never a once and done thing. Due to multiple reasons such as adding more features or bug fixing, the code we start with is often not the same code we end up with and if we want to keep every version then we will end up with multiple versions of the same files which can be confusing, this is where repository comes in.
Our project's folder, when tracked by Git, is called a repository. It stores all our files and remembers all of their different versions. You can think of it as the project history that tracks all edits and saves over time, which is useful to keep track of all the changes we made without having to keep multiple versions of the same files manually.

2. Collaboration

   In software development, multiple people often work on the same codebase. Without a centralised version control system, it would be difficult to coordinate changes. 
Git allows us to create separate branches to work on different features or fixes without affecting the main code. Once the work is done, we can merge our branch back into the main one. This is helpful when working on different features in parallel.
Using this, git allows multiple developers to work on the same project simultaneously without overwriting each other's work. 

3. Basic git command:

   a. Clone: We can copy an existing Git repository from a remote server (like GitHub) to our computer using the git clone command.

   b. Stage Changes: When we make changes to your files, Git doesn’t automatically track them. We need to add them to something called the staging area using the git add command. This tells Git which changes we want to commit.

   c. Commit Changes: Once the changes are staged, we use git commit to save a snapshot of the current state of our project. This saves a description of the changes and updates our project’s history.

   d. Push Changes: After committing, if we're working with a team, we'll want to share our changes with others. This is done using git push, which uploads our changes to a remote repository like GitHub.

   e. Pull Changes: If others have pushed their changes, we can pull their changes into our local repository using git pull, keeping our project up-to-date with the latest work from our team.


In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?
=

From external sources and my own experience, i think django is used as the starting point because of how easy it is to learn and how versatile it is. Because django is open source and have been around since 2003, there is so many improvement made to the framework, and adding to that django also has relatively big community that makes a lot of tutorial and learning material, adding to that add, django also use python who we (and many beginner software developer) have learned before, making it easier to be learned and used, which is why i think we used django.

source: https://codeinstitute.net/global/blog/what-is-django/

Why is the Django model called an ORM?
=

Django's model is called an ORM(Object-Relational Mapping) because it helps us work with databases using normal Python code instead of complicated database language such as SQL. It lets us treat database tables like regular Python objects, so we can easily add, update, or retrieve data without needing to know how to write database commands. It makes database work much easier for developers.

source: https://www.doprax.com/tutorial/django-tutorial-for-beginners-part-6/