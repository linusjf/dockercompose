#!/usr/bin/env python
"""
App.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : app
# @created     : Wednesday Sep 24, 2025 17:52:46 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello from Docker! I have been seen {count} times.\n'
