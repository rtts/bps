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

The easiest way to install this is using `pip`:

    pip3 install git+https://github.com/rtts/bps

This should automatically get you the latest version of BPS and all
its dependencies.

Alternatively, you can install BPS from [Tilburg University's Debian
repository](https://non-gnu.uvt.nl/). First, add the following lines
to `/etc/apt/sources.list`:

    deb http://non-gnu.uvt.nl/debian buster uvt
    deb-src http://non-gnu.uvt.nl/debian buster uvt

Second, add the Tilburg University signing key to your apt key store:

    curl https://non-gnu.uvt.nl/debian/uvt_key.asc | apt-key add -

Now you can install the `bps` package with `apt`:

    apt install bps

Deploying the BPS project
-------------------------

First, open the configuration file `/etc/bps/config.ini` and check if
the default values are suitable for your situation (for testing
purposes they are, but for a production server you probably want to
use a "real" database and adjust the `allowed_hosts` setting). Now the
database tables can be created with the following commands:

    manage.py migrate

Second, you will have to create at least one superuser:

    manage.py createsuperuser

Finally, Apache needs to be configured to serve BPS. For this purpose,
a basic configuration file has already been installed in
`/etc/apache2/conf-available/bps.conf`. If you want to use it, first
install the mod_wsgi module:

    apt-get install libapache2-mod-wsgi

Then, all you need to do is enable the BPS configuration and restart
Apache:

    cd /etc/apache2/conf-enabled
    ln -s ../conf-available/bps.conf
    service apache2 reload

BPS should now be up and running! Visit the URL /admin/ and log in
with your superuser credentials to start adding users and course
content!
