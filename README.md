# ip_extract
Reads a file contains ip addresses with CIDR notation, then extracts each of them to given second file.
At the end, you have one new file with all the IP addresses extracted. However, if you have any incorrect notation in the given file you will also have a second file with the thrown exception files. 

#First argument: The file which contains IP/CIDR     
#Second argument: the output file to append the IP addresses after extraction process. 
#If any error happens in CIDR notation the code writes them into the "exp_ips" file.

