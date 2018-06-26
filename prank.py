import os
from string import digits
list_files=os.listdir("C:\\Users\\Lab7\\Downloads\\prank\\prank")
os.chdir("C:\\Users\\Lab7\\Downloads\\prank\\prank")
#Repeat the following steps for all the files in prank directory
for file in list_files:
    #get oldname of file
    old_name=file
    print old_name
    #newname of file=oldname-number
    new_name=old_name.lstrip(digits)
    print new_name
    os.rename(old_name,new_name)