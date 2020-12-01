=============================
DJ Pony Applied Migrations Checker
=============================

.. image:: https://badge.fury.io/py/dj-pony.applied-migrations-checker.svg
    :target: https://badge.fury.io/py/dj-pony.applied-migrations-checker

.. image:: https://travis-ci.org/techdragon/dj-pony.applied-migrations-checker.svg?branch=master
    :target: https://travis-ci.org/dj-pony/dj-pony.applied-migrations-checker

.. image:: https://codecov.io/gh/techdragon/dj-pony.applied-migrations-checker/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dj-pony/dj-pony.applied-migrations-checker

An Applied Migrations Checker for Django to assist with rolling out django in environments like Kubernetes.

Documentation
-------------

The full documentation is at https://dj-pony-applied-migrations-checker.readthedocs.io.

Quickstart
----------

Install DJ Pony Applied Migration Checker::

    pip install dj-pony.applied-migrations-checker

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_pony.applied_migrations_checker.apps.DjPonyAppliedMigrationsCheckerConfig',
        ...
    )



Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
