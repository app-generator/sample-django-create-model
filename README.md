# Create Model in Django

Open-source sample that explains **how to create and USE a model in Django**. All commands used to code the project and also the relevant updates are listed below. For newcomers, **Django** is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. 

> **For support and more [Django Samples](https://appseed.us/admin-dashboards/django) join [AppSeed](https://appseed.us).**

<br />

**Chech Python Version**

```bash
$ python --version
Python 3.8.4 <-- All good
```

<br />

**Create/activate a virtual environment**

```bash
$ # Virtualenv modules installation (Unix-based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows-based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

**Install Django**

```bash
$ pip install django
```

<br />

**Create Django Project**

```bash
$ mkdir django-create-model
$ cd django-create-model
```

Inside the new directory, we will invoke `startproject` subcommand

```bash
django-admin startproject config .
``` 

> Note: Take into account that `.` at the end of the command.

<br />

**Setup database**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

**Start the app**

```bash
$ python manage.py runserver 
```

<br />

**Create sample app**

```bash
$ python manage.py startapp sample
```

<br />

**Visualize the default SQL settings** - `config/settings.py`

```python
# File: config/settings.py (partial content)
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
...
```

<br />

**Define a new model** `Books` in `sample` application. The below changes should be added to `sample/models.py`:

```python
# File: sample/models.py

from django.db import models                       

class Book(models.Model):                                 # <- NEW
    title            = models.CharField(max_length=100)   # <- NEW 
    author           = models.CharField(max_length=100)   # <- NEW
    publication_date = models.DateField()                 # <- NEW 
```

<br />

**Update Project Configuration** to use the new model - The `sample` application must be added in the project configuration to `INSTALLED_APPS` section.

```python
# File: config/settings.py (partial content)
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sample'                        # <- NEW 
]
...
```

**Tip** - for a quick check over latest changes we can run `check` subcommand. 

```bash
$ python manage.py check
System check identified no issues (0 silenced).  
```

<br />

> Generate the SQL code 

```bash
$ python manage.py makemigrations  # generate the SQL code
Migrations for 'sample':
  sample\migrations\0001_initial.py
    - Create model Book
```

> Apply changes on database

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sample, sessions
Running migrations:
  Applying sample.0001_initial... OK
```

<br />

**Use the model via CLI**

Once the model is created we can use it via the Django shell

```bash
$ python manage.py shell
>>> 
>>> from sample.models import Book     # import the Book model in our context
>>> from django.utils import timezone  # used to provide the value for publication_date
>>>
>>> book1 = Book(title='The Adventures of Tom Sawyer', author='Mark Twain', publication_date=timezone.now() )
>>> book1.save()                       # save the new book
```

**List all books** (using the CLI)

```bash
$ python manage.py shell
>>> 
>>> from sample.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
```

We can see our new book retuned by the query. Let's improve the information that describe the object.

<br />

**Django Model** - add text representation of an object

To achieve this goal, we should define the `__str__()` method for the `Book` model

```python
# File: sample/models.py

from django.db import models                       

class Book(models.Model): 
    title            = models.CharField(max_length=100) 
    author           = models.CharField(max_length=100)
    publication_date = models.DateField() 

    def __str__(self):       # <- NEW
        return self.title    # <- NEW
```

Let's restart the Django console and check the results:

```python
$ python manage.py shell
>>> 
>>> from sample.models import Book
>>> Book.objects.all()
<QuerySet [<Book: The Adventures of Tom Sawyer>]>
```

<br />

**Use the model via Admin Section**

Django comes with an `admin` section our-of-the box that allows us to manage with ease all models defined in project. 
To manage the `Book` model in the administration console we need to create a `superuser` (aka the admin) and after `register` the `Book` model to be visible in the admin section.

> Create the superuser 

```bash
$ python manage.py createsuperuser
sername (leave blank to use 'sm0ke'): admin
Email address: admin@appseed.us
Password: 
Password (again):
Superuser created successfully.
```

<br />

> Register `Book` model to be visible in the `admin` section - Edit `sample/admin.py` as below:

```python
# File: sample/admin.py

from django.contrib import admin

from .models import Book        # <- NEW

admin.site.register(Book)       # <- NEW
```

<br />

> Authenticate as admin - `http://localhost:8000/admin/`

At this point we should see the `Books` model in the UI and able to execute CRUD operations. 

<br />

![Create Model Django - The Book model is visible in the admin interface.](https://user-images.githubusercontent.com/51070104/122179419-2c5f7d00-ce90-11eb-84ad-d51fb05d5521.png)

<br />

![Create Model Django - Books Model has all items listed by the admin interface.](https://user-images.githubusercontent.com/51070104/122179527-4bf6a580-ce90-11eb-91f2-6f1c19a57bec.png)

<br />

![Create Model Django - Item details defined by the Book model.](https://user-images.githubusercontent.com/51070104/122179742-78122680-ce90-11eb-81bb-42477db9460b.png)

<br />

> **For support and more [Django Samples](https://appseed.us/admin-dashboards/django) join [AppSeed](https://appseed.us).**

<br />

---
Create Model in Django - Open-source Sample provided by [AppSeed](https://appseed.us/app-generator).
