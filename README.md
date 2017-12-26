# What is it?
This webapp is designed to be administered by a stake high-council person
assigned to oversee mission work. User accounts are created for each ward 
mission leader, who can log in and report goals and key indicators for their
ward. The high-council person can then view trends on a ward-by-ward or 
aggregate basis

# Goals
I recently did a complete Re-evaluation of Goals. Our new goals are as follows:
  - use django full-stack. This means the backend will be less modular, and if
    I ever create a mobile app, the backend will need to be edited. However, I
    will develop the webapp with a "mobile-first" mentality so that it can be
    used easily on mobile devices.
  - develop the application on a page-by-page basis. This fits better with the
    django mentality.

# Further Information:
## Technologies:
  - python/django front to back
  - posgreSQL database

## How to Set Up:
  - Install python3
  - Install postgres
  - create a databse named mission_tracker and a user named python_app with
    full permissions on mission_tracker.
  - create an environment variable PYTHON_APP_DB_USER_PASSWORD set to the
    password for the python_app user
  - clone the repository
  - in the root directory of the repository, run 'python3 manage.py migrate'

## Todo:
  - customize (and simplify) admin page
    - user: everything in advanced settings except basic information and ward
      - this can be done by adding to UserAdmin in KeyIndicators/admin.py
  - design a 'template' with a navbar, header, and footer that can be included
    in all Django templates. Some resources have been listed below:
      - https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#include
      - https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template

Note: with my recent reevaluation of goals, issue #1 is (temporarily?) being
ignored. It will most likely be closed soon, as the issue is no longer
relevant: we are developing the app on a page-by-page basis instead of backend
and then frontend.
