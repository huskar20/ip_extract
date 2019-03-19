# ip_extract
Reads a file contains ip addresses with CIDR notation, then extracts each of them to given second file.
At the end, you have one new file with all the IP addresses extracted. However, if you have any incorrect notation in the given file you will also have a second file with the thrown exception files. 

ipaddress_range.txt: Used to include IP/CIDR 
ip_result.txt: IP addresses. This is the result file. 
#If any error happens in CIDR notation the code writes them into the "exp_ips" file.

*This is a python3 script. It does not work for python2.

