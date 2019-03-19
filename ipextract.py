'''
Created on Feb 16, 2018
@author: huseyin k.
'''
import sys
import ipaddress

#First argument: The file contains IP/CIDR 
#Second argument: Output file to append the IP addresses. 
#If any error happens in CIDR notation the code writes them into the "exp_ips" file.
ip_count = 0
ex_ip_count = 0
file_rd = open(r"ipaddress_range.txt","r")
for ipr in file_rd.readlines():
    try:
        _network = ipaddress.ip_network(ipr.strip())
        # Get all hosts on that network
        _hosts = list(_network.hosts())
        #open the file to write
        file_wr = open(r"ip_results.txt","a")  
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
print(str(ip_count) + " IP address are appended to " + "ip_results.txt")
print(str(ex_ip_count) + " IP ranges has thrown exception.")
