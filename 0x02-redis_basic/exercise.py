#!/usr/bin/env python3
""" Creates a Cache class that instantiates
a redis session and stores key
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        """ Instantiates the session
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores the key with the data supplied
        """
        key = str(uuid4())
        self.__redis.set(key, data)
        return key
