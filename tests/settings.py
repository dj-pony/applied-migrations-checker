# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from pathlib import Path
import django
import environ

print(Path.cwd())

DEBUG = True
USE_TZ = True
TIME_ZONE = "UTC"


env = environ.Env()
POSTGRESQL_TEST = env.bool("POSTGRESQL_TEST", default=False)
MYSQL_TEST = env.bool("MYSQL_TEST", default=False)
SQLITE_TEST = env.bool("SQLITE_TEST", default=False)
PYCHARM_TEST = env.bool("PYCHARM_TEST", default=False)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "**************************************************"

if SQLITE_TEST:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
            "TEST": {
                "NAME": ":memory:",
            },
        }
    }
elif POSTGRESQL_TEST:
    from dj_pony.django_docker_test_dbs.docker_db_in_memory import run_testing_database

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "service_core_test",
        }
    }
    DATABASES = run_testing_database(DATABASES)
    print(DATABASES)
elif MYSQL_TEST:
    from dj_pony.django_docker_test_dbs.docker_db_in_memory import run_testing_database

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "service_core_test",
            "HOST": "127.0.0.1",
        }
    }
    DATABASES = run_testing_database(DATABASES)
    print(DATABASES)
if PYCHARM_TEST:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            # "NAME": str(Path.cwd() / "applied_migrations_checker.db"),
            "NAME": ":memory:",
            "TEST": {
                # "NAME": str(Path.cwd() / "test_applied_migrations_checker.db"),
                "NAME": ":memory:",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            # "NAME": ":memory:",
            "NAME": str(Path.cwd() / "applied_migrations_checker.db"),
            "TEST": {
                "NAME": str(Path.cwd() / "test_applied_migrations_checker.db"),
            },
        }
    }

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "dj_pony.applied_migrations_checker",
    "tests",
]

SITE_ID = 1


if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
