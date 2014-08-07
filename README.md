tweetrecorder
=============

SIMPLE REAL TIME TWEET RECORDER

- Create a copy of settings_SAMPLE.py and name it settings.py
- Define your Twitter OAuth Credentials
- Define your keyword search list

- Setup your virtualenv:

> virtualenv . --no-site-packages
> source bin/activate

- Install dependencies

> pip install -r dependencies.pip

Run the grabber

> python recorder.py > dump.txt

