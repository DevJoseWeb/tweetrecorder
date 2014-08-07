tweetrecorder
=============

SIMPLE REAL TIME TWEET RECORDER

- Install REDIS (http://redis.io)
- Create a copy of local_settings.py.SAMPLE and name it local_settings.py
- Save your Twitter OAuth Credentials

- Setup your virtualenv:

> virtualenv . --no-site-packages

> source bin/activate


- Install dependencies

> pip install -r dependencies.pip


Run the grabber

> cd src

> redis-server

> celery -A grabber worker

> python manage.py tweetgrabber <keyword1> <keyword2> <...>

