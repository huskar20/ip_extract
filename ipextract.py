'''
Created on Feb 16, 2018
@author: huseyin k.
'''
import sys
import ipaddress

#First argument: The file contains IP/CIDR 
#Second argument: Output file to append the IP addresses. 
ip_count = 0
ex_ip_count = 0
file_rd = open(sys.argv[1],"r")
for ipr in file_rd.readlines():
    try:
        _network = ipaddress.ip_network(ipr.strip())
        # Get all hosts on that network
        _hosts = list(_network.hosts())
        #open the file to write
        file_wr = open(sys.argv[2],"a")  
        # Print the IP addresses
        for i in _hosts:
            file_wr.write(str(i) + '\n') 
            ip_count+=1
        file_wr.close()
    except:
        e = sys.exc_info()[1]
        file_exp =open("exp_ips","a")
        file_exp.write(str(e) + '\n')
        ex_ip_count+=1
print(str(ip_count) + " IP address are appended to " + sys.argv[2])
print(str(ex_ip_count) + " IP ranges has thrown exception.")
