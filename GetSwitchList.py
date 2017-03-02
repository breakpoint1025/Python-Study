import urllib.request 
import re
import time
import os

working_dr = r"E:\SNMPUpdate\SimpleSoftConfig\map"
#开始计时
start = time.clock()

saved_path = os.getcwd()
os.chdir(working_dr)

for filename in os.listdir():
    f = open(filename, 'r')
    for line in f.readlines():
        if line.find('Name') != -1:
            a = line.find('\"')
            b = line.rfind('\"')
            ip = line[line.find('\"')+1:-line.rfind('\"')]



os.chdir(saved_path)
#结束计时
end = time.clock()
print("Time spent:%f seconds" %(end-start))