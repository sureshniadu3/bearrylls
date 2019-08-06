# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 00:43:47 2019

@author: DELL 5578
"""

import boto3
import csv
#import pprint
session = boto3.Session(profile_name="default",region_name="us-east-1")
ec2_res = session.resource("ec2")
ec2_cli = session.client("ec2")
fd = open("ec2_inv1.csv","w")
csv_wd = csv.writer(fd)
ll =[]
header =["SNO","Private Ip", "instance_arch", "instance_type"]
sno =1
csv_wd.writerow(["SNO","Private Ip", "instance_arch", "instance_type"])

#import pandas as pd

#a = pd.DataFrame()
for each_in in ec2_res.instances.all():
  #  print (dir(each_in))
    private_ip = each_in.private_ip_address
    instance_arch = each_in.architecture
    instance_type = each_in.instance_type
    ll = [sno,private_ip,instance_arch,instance_type]
    csv_wd.writerow(ll)
    
  #  ec2_inv = ll.append({'private_ip':private_ip,'instance_arch':instance_arch,'instance_type':instance_type})
  #  a = pd.DataFrame([ec2_inv])
    
#ec2_inv.dtype

#a.to_csv("ec2_inv.csv",index = False)

#import pandas as pd

#import os
#os.chdir(r"D:\AWS-PRACTICE\aws-sdk-scripts")