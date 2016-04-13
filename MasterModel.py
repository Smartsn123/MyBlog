#Before you go any further and start creating instances here and there make sure you take the time so set up billing alerts.
#Setup Connection object  using boto
import boto
import numpy as np
from boto.ec2.connection import EC2Connection
conn = EC2Connection('<aws access key>', '<aws secret key>')


#1.Create a Security Group with the inbound and outbound rules

#2 .generate an SSH key pair for accessing the public AMIs without a root password
#key_pair = conn.create_key_pair('gsg-keypair')
#You need to save the private key to a file. Copy everything including the lines starting ----- into a file named id_rsa-gsg-keypair a
#nd then execute the following command to ensure that no-one other than you can read the file:
#$ chmod 600 id_rsa-gsg-keypair ; ls -l id_rsa-gsg-keypair
#-rw------- 1 james james 1672 2007-08-27 13:10 id_rsa-gsg-keypair

urlsList=[]


#Launch a linux instance and associate the security group and key value pair with this instance, 
#(we will use my-ec2.amazonaws.com as the public dns of the instance)
#fetching all available images (AMI)
images = conn.get_all_images()
#booting an Ec2 incstnace image to a particular image using keypair generated
reservation1 = image.run(key_name=ec2_keypair,
                                        security_groups=ec2_secgroups,
                                        instance_type=ec2_instancetype,
                                        min_count=1,
                                        max_count=10)
                                        
                                        
                                        

                                                                   
#monitoring the state of an instance wait until instance is not running as it takes time to boot 
instance.update()
instance.state


#Install scrapy and scrapyd on the EC2 instance



 
