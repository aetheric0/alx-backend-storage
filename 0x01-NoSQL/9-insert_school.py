#!/usr/bin/env python3
""" Python function that inserts a new document in
a collection based on `kwargs`
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection
    """
    new_document = dict(kwargs.items())
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
