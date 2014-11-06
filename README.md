Utah Python Users Group November 2014 Example
=============================================

This repo contains an example of a very basic (Hello Worldesque) website.  The site has a single route that allows you to get a Fibonacci number given an index.

This website has two implementations.  One using the Flask framework and the other using the Django framework.

Requirements
------------

1. Flask
2. Django
3. Python
4. Django Fixtureless

Clone this Repo
---------------

Ensure you have Git installed on your machine.

    $ sudo apt-get install git
    
Clone this repo to your local system.

    $ git clone git@github.com:ricomoss/upug-november-2014.git
    

Virtual Environment
-------------------

You should always have a virtual environment for anything Python related - it's just best practice!  It prevents overlapping of library requirements and will make you a much happier developer in the long run.

There are many options available for setting up a virtual environment.  One is provided below.

- Ensure you have the necessary libraries.
    $ pip install virtualenv
    $ pip install virtualenvwrapper
    
- Source the wrapper in your local rc file.  (*~/.bashrc*, *~/.zshrc*, etc)
    $ source /usr/local/bin/virtualenvwrapper.sh
    
- Create your virtual environment  (for Python 2.7.x and Python 3.x, respectively):
    $ mkvirtualenv upug_example
    $ mkvirtualenv upud_example -p /usr/bin/python3


Flask
-----

It is very simple to run Flask.

    $ python flask_example/flask_ex.py
    
It should start your runserver on port 5000.  Open your browswer and go to *http://127.0.0.1:5000/fib-num/?fib_index=0* and you should see *0* on the page.

You can edit the value of *fib_index* and you should see the corresponding Fibonacci number.

Django
------

You'll need to initialize the Django project.  Once this step is complete you won't have to do it again (unless you modify the models).

    $ python django_example/example_project/manage.py syncdb
    
You will get a series of questions about a root user.  Just answer them as you want - there is no user authentication for this example project.

Again, the above step should only need to be run once to initialize this project on your machine.  Once that is complete you only need to do the next step to run the site.

    $ python django_example/example_project/manage.py runserver
    
It should start your runserver on port 8000.  Open your browswer and go to *http://127.0.0.1:8000/fib-num/?fib_index=0* and you should see *0* on the page.

You can edit the value of *fib_index* and you should see the corresponding Fibonacci number.

Differences
-----------

You can see the difference between the Flask and Django implementations when you enter a *fib_index* large enough you notice a wait for it to process (probably around 500000 or more).  Then try the same number for both Flask and Django and you'll notice Django returns immediately with the result.  This is due to Django storing the value in the local SQLite database for quick access.

Django Fixtureless
------------------

If you inspect the Django code you'll see a few dumby methods throughout.  This is so we have **something** to test.  Open *django_example/example_project/example_app/tests.py* to see how Django Fixtureless can be used in an application.

Play with it!  Change things and see how it works.  You can always run the tests with the following command to see what your changes did.  First, change directories into *example_project*

    $ cd django_example/example_project
    $ python manage.py test --settings=example_project.settings
    
You should see something like the following:

    Creating test database for alias 'default'...
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s
    
    OK
    Destroying test database for alias 'default'...
    
As you change (or break) tests you may see a different output.
