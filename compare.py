import sys
import ipaddress

firstlist=[]
secondlist=[]
# open file and read the content in a list
with open('firstlist', 'r') as filehandle:
    firstlist = [current_place.rstrip() for current_place in filehandle.readlines()]

# open file and read the content in a list
with open('secondlist', 'r') as filehandle:
    secondlist = [current_place.rstrip() for current_place in filehandle.readlines()]



#Compares the lists
def comp(list1, list2):
    for val in list1:
        if val in list2:
            print(str(val))
            return True
    return False

comp(firstlist, secondlist)
print("bitti")
