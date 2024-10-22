#!/usr/bin/env python3
""" Python function that returns the list of
school having a specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ retrieves schools in a list that offer topic
    """
    result = mongo_collection.find({"topics": {"$in": [topic]}})
    document = list(result)
    return document
