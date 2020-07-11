Best Practices in Statistics
============================

Best Practices in Statistics (BPS) is a web application for learning
statistics. Students can learn and practice statistical techniques in
the form of "Blended Learning": step-by-step digital instructions
crafted by the best of statistics teachers, tailored to the contents
of the various statistics courses provided by Tilburg University.

BPS is currently available to Tilburg University students at the
following URL: https://bps.uvt.nl/

This repository contains all the source code of BPS, including the
formerly separately published Autodidact app. Everyone is free to use
this code to built their own blended learning environment! Here's how
to get started:

Installation
------------

Before installing BPS, it is highly recommended to setup a [Python
Virtual Environment](https://docs.python.org/3/tutorial/venv.html):

    mkdir -p ~/.virtualenvs
    python3 -m venv ~/.virtualenvs/bps
    . ~/virtualenvs/bps/bin/activate

Then, simply install this package with pip:

    python3 -m pip install git+https://github.com/rtts/bps

This should automatically get you the latest version of BPS and all
its dependencies. One of these dependencies is [Django
SimpleCMS](https://github.com/rtts/django-simplecms), an elegant and
minimalistic CMS system by the same author as BPS.

Running BPS
-----------

BPS runs like any other Django project. The following commands should
get you started:

    manage.py migrate
    manage.py createsuperuser
    manage.py runserver

BPS should now be up and running! Visit the URL
http://localhost:8000/admin/ and log in with your superuser
credentials to start adding some course content.

Since BPS now includes Django SimpleCMS, logged in users will
automatically see "add" and "edit" buttons in the appropriate places
while visiting the main site. This should make it easier to customize
the pages than by using the admin.

If you have any further questions, don't hesitate to contact me via
jj [at] rtts.eu
