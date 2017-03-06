import urllib.request 
import re
import time
import os
import pyodbc
import random
import shutil

working_dr = r"E:\SNMPUpdate\SimpleSoftConfig\map"
#working_dr = r"C:\GitHub\TestData\SimpleSoftConfig\map"
#开始计时
start = time.clock()

saved_path = os.getcwd()
os.chdir(working_dr)

devinfo_list = []
fo = open("..\devices_list.txt", "w+")
for filename in os.listdir():
    f = open(filename, 'r')
    for line in f.readlines():
        if line.find('Name') != -1:
            devinfo = ""
            if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', line[line.find('\"')+1:line.rfind('\"')]):
                devinfo = line[line.find('\"')+1:line.rfind('\"')]          
        if (line.find('ReadCommunity') != -1) and (devinfo != ""):
            devinfo = devinfo + ":" + line[line.find('\"')+1:line.rfind('\"')]
        if (line.find('WriteCommunity') != -1) and (devinfo != ""):
            devinfo = devinfo + ":" + line[line.find('\"')+1:line.rfind('\"')]
            devinfo_list.append(devinfo)
            fo.write(devinfo + "\n")
            print(devinfo)

print("We have [%d] simulators" %(len(devinfo_list)))
fo.close()


#Remove all the harnessfiles at beginning
shutil.rmtree(r"E:\SM7\Git\SNMPService 7.2\SNMPService\SourceCode\SNMPServer.Service\bin\Debug\TestData")
        
#Prepare deviceinfo in SQL Server for sync
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=SNMPSiteData;UID=sm7user;PWD=1')
cursor = cnxn.cursor()

#Truncate relevant table first
cursor.execute("truncate table [dbo].[SNMPSwitchProfiles]")
cursor.execute("truncate table [dbo].[SNMPCommProfiles]")
cursor.execute("truncate table [dbo].[SNMPSwitches]")
cursor.execute("truncate table [dbo].[SNMPTasks]")
cursor.execute("truncate table [dbo].[SNMPTaskChanges]")
cnxn.commit()

#insert SNMPCommProfiles SNMPSwitchProfiles SNMPSwitches and SNMPTasks
profId = random.randint(0, 10000000)

#hard code the SNMPCommProfiles and SNMPSwitchProfiles first-- enhance laster
sqlstr = ("insert into SNMPCommProfiles(id, target, security) values (%d , '<Target><Timeout>3</Timeout><Retries>3</Retries></Target>', '<SecInfo><V2><ReadCommunityString>307300331071011540F900DB00FC0C9C207F093F60760277</ReadCommunityString><WriteCommunityString>307300331071001340F909D910FC049E207F013F7076047640FA00DF</WriteCommunityString></V2></SecInfo>')" %(profId))
cursor.execute(sqlstr)

sqlstr = ("insert into SNMPSwitchProfiles(id, SyncProfileData) values (%d , '<Options><VirtualNetworks>2</VirtualNetworks><PortDesc /></Options>')" %(profId))
cursor.execute(sqlstr)

#insert switches and sync tasks one by one
for dev in devinfo_list:

    #insert switche
    ip = dev[0:dev.find(":")]
    sqlstr = ("insert into SNMPSwitches(Enabled,IPAddress,Configuration,Devices,SNMPCommProfileID,SNMPSwitchProfileID) values(1, '%s','<SyncSwitch />','<DiscDevicesSwitch />',%d,%d)" %(ip,profId,profId))
    cursor.execute(sqlstr)
    cursor.execute('SELECT @@IDENTITY')
    switchId = cursor.fetchone()[0]

    #insert task
    taskId = random.randint(0, 10000000)
    sqlstr = ("insert into SNMPTasks(ID, ActionType, ObjectID, ScheduledDateTime, Priority, InProgress, Options) values(%d, 'SyncSwitch', %d, '2017-01-01 0:0:0.0', 1, 0, '<Options><FullConfigSync /></Options>')" %(taskId,switchId))
    cursor.execute(sqlstr)

cnxn.commit()


os.chdir(saved_path)
#结束计时
end = time.clock()
print("Time spent:%f seconds" %(end-start))