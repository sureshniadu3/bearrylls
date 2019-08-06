import boto3
session = boto3.Session(profile_name="default",region_name="us-east-1")
client = session.client('ec2')

list_of_regions = []
for each_reg in client.describe_regions()['Regions']:
    print(each_reg['RegionName'])
    list_of_regions.append(each_reg['RegionName'])

for each_reg in list_of_regions:
    session = boto3.Session(profile_name="default",region_name=each_reg)
    resou = session.resource('ec2')
    for each_in in resou.instances.all():
        print(each_in.id,each_in.state["Name"])