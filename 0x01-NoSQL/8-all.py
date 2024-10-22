#!/usr/bin/env/python
""" Using Pymongo client to list all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Connects to Database `my_db` and retrieves documents
    in collection passed as argument
    """
    result = mongo_collection.find()
    documents = list(result)
    if not documents:
        return []
    return documents
