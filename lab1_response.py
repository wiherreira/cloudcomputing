#This code was used to complete Lab1, it prints the endpoint and Region
#Name of Amazon's servers.

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
#print(response)
for k in response['Regions']:
    print('Endpoint is: ', k['Endpoint'], 'Region name is: ', k['RegionName'])
    