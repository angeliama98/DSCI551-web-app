# DSCI551-web-app

Run program: python manage.py runserver

Open ‘localhost:8000/dsci551/‘ to see the web app

To-do:
1) base.html: Search tab: dsci551_search url needs to be linked
2) dsci551_index.html: Import table, read query, display result
3) Link search page to main page (link jump)
4) Search page: add result box


quick ref:

1)connect mysql to django

modify settings.py -> database

python3 manage.py inspectdb (check conenction)

python3 manage.py inspectdb > blog/models.py (import models to models.py)

2)connect firebase to django

use pyrebase to implement; documentation: https://github.com/thisbejim/Pyrebase
