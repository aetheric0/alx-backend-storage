#!/usr/bin/env python3
""" Python script that provides some stats about
Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    no_of_documents = collection.count_documents({})
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = []
    for method in methods_list:
        method_count.append(collection.count_documents({"method": method}))
    print("{} logs".format(no_of_documents))
    print("Methods:")
    i = 0
    for method in methods_list:
        print("\t method {}: {}".format(method, method_count[i]))
        i += 1
    get_count_with_status = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(get_count_with_status))
