import paramiko
import os

#creating the ssh client object where all the ssh client will be saved
ssh =paramiko.SSHClient()
#creating the ssh client object which will be responsible to connect to the AWS ec2 ubuntu instance using 2 approach
#1:-using the username and password approach
#here we are setting the host key policy as AutoAddpolicy so that it will not prompt for yes/no question
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=os.environ.get("AWS_HOST"), username="ubuntu", password=os.environ.get("AWS_PASS"),port=22)
ssh.connect(hostname=os.environ.get("AWS_HOST"), username="ubuntu", key_filename=os.environ.get("AWS_KEY_PATH"),port=22)
#:-2 now handling with id_rsa private key path
##ssh-cpy-id <username>@<ec2 host> for setting up the is_rsa.pub to the ec2 instance
#now allowing the user to run the stdin stdout and stderr command without logging in to the remote server
stdin,stdout,stderr = ssh.exec_command("whoami")
stdin.close()
print(stdout.read())
print(stderr.read())
