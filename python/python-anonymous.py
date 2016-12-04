# Example in Python 2
import boto
import boto.s3.connection

conn = boto.connect_s3(
        anon=True,
        host = 'datasets2.iccluster.epfl.ch',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date
        )

bucket_name = "reddit"
bucket = conn.get_bucket(bucket_name)

for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
        )
