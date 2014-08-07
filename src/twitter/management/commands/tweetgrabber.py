#!/usr/bin/python
# -*- coding: utf-8 -*

import logging
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from twitter.tasks import persist_tweet
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


TWITTER_CONSUMER_KEY = getattr(settings, "TWITTER_CONSUMER_KEY", "")
TWITTER_CONSUMER_SECRET = getattr(settings, "TWITTER_CONSUMER_SECRET", "")
TWITTER_ACCESS_KEY = getattr(settings, "TWITTER_ACCESS_KEY", "")
TWITTER_ACCESS_SECRET = getattr(settings, "TWITTER_ACCESS_SECRET", "")


LOGGER = logging.getLogger("grabber")



class GrabberListener(StreamListener):
    """
    Processa recepcao de um tweet no socket HTTP
    """
    def on_data(self, data):
        if data:
            tweet = json.loads(data)
            persist_tweet.delay(tweet)
        return True

    def on_error(self, status):
        LOGGER.error("Twitter Error %s" % status)
        return False
    


class Command(BaseCommand):
    def execute(self, *args, **options): 
        auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)

        keywords = list(args)

        if keywords:
            LOGGER.info("TWITTER SEARCH PARAMS = %s" % keywords)
            listener = GrabberListener()
            stream = Stream(auth, listener)
            stream.filter(track=keywords)
        else:
            LOGGER.info("NO KEYWORDS")