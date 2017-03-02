import urllib.request 
import re
import time
import os

#working_dr = r"E:\SNMPUpdate\SimpleSoftConfig\map"
working_dr = r"C:\GitHub\TestData\SimpleSoftConfig\map"
#开始计时
start = time.clock()

saved_path = os.getcwd()
os.chdir(working_dr)

devinfo_list = []
fo = open("devices_list.txt", "w+")
for filename in os.listdir():
    f = open(filename, 'r')
    for line in f.readlines():
        if line.find('Name') != -1:
            devinfo = ""
            devinfo = line[line.find('\"')+1:line.rfind('\"')]
        if line.find('ReadCommunity') != -1:
            devinfo = devinfo + ":" + line[line.find('\"')+1:line.rfind('\"')]
        if line.find('WriteCommunity') != -1:
            devinfo = devinfo + ":" + line[line.find('\"')+1:line.rfind('\"')]
            devinfo_list.append(devinfo)
            fo.write(devinfo + "\n")
            print(devinfo)

print("We have [%d] simulators" %(len(devinfo_list)))
fo.close()
        



os.chdir(saved_path)
#结束计时
end = time.clock()
print("Time spent:%f seconds" %(end-start))