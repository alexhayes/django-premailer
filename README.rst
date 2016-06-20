================
Django Premailer
================

Django template tag that turns CSS blocks into style attributes using premailer_.

.. image:: https://travis-ci.org/alexhayes/django-premailer.png?branch=master
    :target: https://travis-ci.org/alexhayes/django-premailer
    :alt: Build Status

.. image:: https://landscape.io/github/alexhayes/django-premailer/master/landscape.png
    :target: https://landscape.io/github/alexhayes/django-premailer/
    :alt: Code Health

.. image:: https://codecov.io/github/alexhayes/django-premailer/coverage.svg?branch=master
    :target: https://codecov.io/github/alexhayes/django-premailer?branch=master
    :alt: Code Coverage

.. image:: https://readthedocs.org/projects/django-premailer/badge/
    :target: http://django-premailer.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/django-premailer.svg
    :target: https://pypi.python.org/pypi/django-premailer
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/django-premailer.svg
    :target: https://pypi.python.org/pypi/django-premailer/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/dd/django-premailer.svg
    :target: https://pypi.python.org/pypi/django-premailer/
    :alt: Downloads


Install
-------

.. code-block:: bash

    pip install django-premailer

Add ``django_premailer`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        '...',
        'django_premailer'
    )


Example Usage
-------------

Simply use the ``premailer`` template tag around HTML where you need inline CSS: 

.. code-block:: html

    {% load premailer %}

    {% premailer "http://example.com" %}
    <html>
    <style type="text/css">
    h1 { border:1px solid black }
    p { color:red;}
    .c {
      background-color: #FF6600;
    }
    .c td {
      background-color: #CCCCCC;
    }
    </style>
    <h1 style="font-weight:bolder">{{ eggs }}</h1>
    <p><a href="/blah/">Hej</a></p>
    <table class="c">
      <tr>
        <td></td>
      </tr>
    </table>
    </html>
    {% endpremailer %}

The rendered template would look as so;

.. code-block:: html

    <html>
    <head></head>
    <body>
        <h1 style="border:1px solid black; font-weight:bolder">Sausage</h1>
        <p style="color:red"><a href="http://example.com/blah/">Hej</a></p>
        <table style="background-color:#F60" bgcolor="#F60">
          <tr>
            <td style="background-color:#CCC" bgcolor="#CCC"></td>
          </tr>
        </table>
    </body>
    </html>


Settings
--------

If you need more control over premailer's init parameters you can define them using ``PREMAILER_OPTIONS``.

For example, in your settings file;

.. code-block:: python

    PREMAILER_OPTIONS = dict(base_url='http://example.com',
                             remove_classes=False)

See https://github.com/peterbe/premailer/blob/master/premailer/premailer.py#L149 for a list of other possible options.

Thanks
------

- Special thanks to http://roi.com.au for supporting this project.
- Thanks to https://github.com/roverdotcom/django-inlinecss for initial inspiration.

Author
------

Alex Hayes <alex@alution.com>


.. _premailer: https://github.com/peterbe/premailer
