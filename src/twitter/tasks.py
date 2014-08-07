#!/usr/bin/python
# -*- coding: utf-8 -*
import logging

from celery import shared_task

from .models import Tweet

LOGGER = logging.getLogger("grabber")


@shared_task
def persist_tweet(tweet):
    try:
        Tweet.objects.create(id_str = tweet["id_str"],
                            author = tweet["user"]["screen_name"], 
                            text = tweet["text"])
        LOGGER.info("Tweet %s from %s recorded" % (tweet["id_str"], tweet["user"]["screen_name"]))
    except Exception, e:
        LOGGER.exception(e)
