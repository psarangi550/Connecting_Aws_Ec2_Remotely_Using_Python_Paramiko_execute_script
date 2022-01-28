import paramiko #importing the paramiko module
import os #importing the os module
#here we are trying to dowanlod and upload file from local to remote server using thr sshv2 using sshclient of python paramiko
ssh_client=paramiko.SSHClient() #creating the object of ssh_client
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # here creating a default host_key_policy to avoid client prompt
ssh_client.connect(hostname="13.233.106.53",username="ubuntu",password=os.environ.get("AWS_PASS"),port=22)
sftp_client=ssh_client.open_sftp()#here creating the sftp_client object which will be used for sending the file to remote server and download as well
#fetching the file from remote server into the local one
#here we are providing the full path we can do the same with out providing the full path
# sftp_client.get("/home/ubuntu/generate.txt","local_generate.txt")
# #now closing the sftp connection first as it depends on the ssh object i.e ssh_client
#
# #without providing the fullpath od sftp_object so that we can download the file directly from the remote server
# sftp_client.chdir("/home/ubuntu")#changing the location of the sftp server
# # print()
# # print(sftp_client.getcwd()) #fetching the current location of the sftp object
# sftp_client.get("direct.json","direct.json")
# sftp_client.close()
#here closing the remote ssh client so that traction will be completed
#case:-2
#here we are sending the python script from the local server to the remote server using the sftp object of sshv2
sftp_client.put("Executing_Bash_Script_using_paramiko.py","/home/ubuntu/Executing_Bash_Script_using_paramiko.py")
#by using the put() sending the file to the remote server
sftp_client.close()
#closing the sftp connection over here
ssh_client.close()#closing the ssh connection
print("All Task done")
