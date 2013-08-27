#!/usr/bin/python
# -*- coding: utf-8 -*
import simplejson
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import settings


class GrabberListener(StreamListener):
    """
    Processa recepcao de um tweet no socket HTTP
    """
    def on_data(self, data):
        tweet = simplejson.loads(data)
        if not tweet:
            return True
        print data
        return True

    def on_error(self, status):
        return False


if __name__ == "__main__":
    TWITTER_CONSUMER_KEY = getattr(settings, "TWITTER_CONSUMER_KEY", "")
    TWITTER_CONSUMER_SECRET = getattr(settings, "TWITTER_CONSUMER_SECRET", "")
    TWITTER_ACCESS_KEY = getattr(settings, "TWITTER_ACCESS_KEY", "")
    TWITTER_ACCESS_SECRET = getattr(settings, "TWITTER_ACCESS_SECRET", "")
    KEYWORDS = getattr(settings, "KEYWORDS", [])

    print "SEARCH KEYWORDS=", KEYWORDS

    auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)

    listener = GrabberListener()
    stream = Stream(auth, listener)
    stream.filter(track=KEYWORDS)
    