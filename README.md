# DSCI551-web-app

Run program: python manage.py runserver

Open ‘localhost:8000/dsci551/‘ to see the web app

quick ref:

1)connect mysql to django

modify settings.py -> database

python3 manage.py inspectdb (check conenction)

python3 manage.py inspectdb > dsci551/models.py (import models to models.py)

2)connect firebase to django

use pyrebase to implement; documentation: https://github.com/thisbejim/Pyrebase
