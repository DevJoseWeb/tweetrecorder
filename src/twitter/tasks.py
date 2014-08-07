#!/usr/bin/python
# -*- coding: utf-8 -*
import logging

from celery import shared_task

from .models import Tweet

LOGGER = logging.getLogger("grabber")


@shared_task
def persist_tweet(tweet):
    try:
        id_str = tweet["id_str"]
        author = tweet["user"]["screen_name"]
        text = tweet["text"]

        Tweet.objects.create(id_str = id_str,
                            author = author, 
                            text = text)
    
        LOGGER.info("Tweet %s from %s recorded" % (id_str, author))
    
    except Exception, e:
        LOGGER.exception(e)
