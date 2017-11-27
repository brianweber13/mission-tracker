Includes everything needed, from front to back.

Uses:
  - python/Django backend using postgreSQL
  - JQuery and Bootstrap frontend

react-native-app is not currently used. There will eventually be a mobile app

How to Set Up:
  - Install python3
  - Install postgres
  - create a table named mission_tracker and a user named python_app with full
    permissions on mission_tracker.
  - create an environment variable PYTHON_APP_DB_USER_PASSWORD set to the
    password for the python_app user
  - clone the repository
  - in the root directory of the repository, run 'python3 manage.py migrate'

Todo:
  - write python backend (see #1)
  - create frontend form with JQuery and promises for http requests
  - use bootstrap to make it pretty
