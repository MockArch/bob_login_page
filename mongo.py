# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient


# set up your db credentials here!!

MONGODB_HOST = xxxxxxx
MONGODB_PORT = xxxxxxxxx
MONGO_USERNAME = xxxxxxxxx
MONGO_PASSWORD = xxxxxxxx
MONGODB_NAME = xxxxxxxx


class Conn(MongoClient):
    

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._get_connection()

        return cls._instance

    @classmethod
    def _get_connection(self):
        if MONGO_USERNAME and MONGO_PASSWORD:
            conn_string = 'mongodb://%s:%s@%s:%s/%s' % (
                MONGO_USERNAME, MONGO_PASSWORD, MONGODB_HOST, MONGODB_PORT,MONGODB_NAME)
        else:
            conn_string = 'mongodb://%s:%s/%s' % (MONGODB_HOST, MONGODB_PORT,MONGODB_NAME)
        c = MongoClient(conn_string)[MONGODB_NAME]

        return c
