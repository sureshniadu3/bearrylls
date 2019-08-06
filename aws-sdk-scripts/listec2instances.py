import boto3
session = boto3.Session(profile_name="default", region_name="us-east-1")
ec2_res = session.resource('ec2')
ec2_cli = session.client('ec2')

#printing instances using resource 
'''
for each_in in ec2_res.instances.all():
    print(each_in)
    print(each_in.id,each_in.state)

'''
#Printing using the client object  (it is a low lvwl object that gives the values in dictionary , key and value pair)

for each_instance in ec2_cli.describe_instances()["Reservations"]:
    for each_in in each_instance['Instances']:
        print(each_in["InstanceId"], each_in['State']['Name'])



