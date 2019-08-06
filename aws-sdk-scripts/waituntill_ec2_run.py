import boto3
session = boto3.Session(profile_name="default", region_name="us-east-1")
ec2_resource = session.resource('ec2')

my_in = ec2_resource.Instance(id="i-02ee2605fd6431992")
print(dir(my_in))
#my_in.start()
#my_in.wait_untill_running()