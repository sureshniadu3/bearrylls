import boto3
s3ob = boto3.resource('s3')
for bucket in s3ob.buckets.all():
    print (bucket.name)