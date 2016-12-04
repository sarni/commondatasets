#!/usr/bin/env python
"""python-anonymous.py: lists all objects in a bucket on common datasets"""
__author__ = "Sofiane Sarni"
__license__ = "GPL"
__version__ = "0.1"

import boto
import boto.s3.connection

conn = boto.connect_s3(
        anon=True,
        host = 'datasets.iccluster.epfl.ch',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

bucket_name = "reddit"
bucket = conn.get_bucket(bucket_name)

for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
        )
