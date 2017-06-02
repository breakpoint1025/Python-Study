import re
import time
import os
import random
import shutil
import pyodbc




def deal_walkfiles(root_dir, filestream, cursor):
    file_list = os.listdir(root_dir)
    for f in file_list:
        file_path = os.path.join(root_dir, f)
        if os.path.isfile(file_path):
            if f.endswith(".var"):
                os.remove(file_path)
                print (file_path + " removed!")
            elif f.endswith(".txt"):
                file = open(file_path, 'r')
                devinfo = ""
                for line in file.readlines():
                    if line.find('1.3.6.1.2.1.1.2.0') != -1:
                        oid = line[line.rfind(',') + 1:].strip()
                        cursor.execute("select Model, ManufacturerID, AlgorithmNumber from ProprietarySwitchInfo where oid = '%s'" %(oid))
                        row = cursor.fetchone()
                        if row:
                            devinfo = oid + ","  + row.Model + "," + str(row.ManufacturerID) + "," + str(row.AlgorithmNumber) + "," + "false"
                        else:
                            devinfo = oid + ","  + "" + "," + "" + "," + "" + "," + "false"

                    if (line.find('1.3.6.1.2.1.105.1.1.1.10') != -1) and (devinfo != ""):
                        devinfo = devinfo.replace("false", "true", 1)
                        break
                if len(devinfo) > 0:
                    fo.write(devinfo + "\n")
                    print(devinfo)
        elif os.path.isdir(file_path):
            deal_walkfiles(file_path, filestream, cursor)




if __name__ == '__main__':

    connStr = 'DRIVER={SQL Server};SERVER=192.168.200.246\SMSQL2008;DATABASE=SNMPSiteData;UID=sa;PWD=SM7sm7!@#$%12345'
    saved_path = os.getcwd()
    dir = os.path.dirname(os.path.abspath(__file__))
    cnxn = pyodbc.connect(connStr)
    cursor = cnxn.cursor()
    fo = open(".\switch_PoE_list.csv", "w+")
    fo.write("OID,Switch Model, ManufacturerID, AlgorithmNumber" + "\n")
    deal_walkfiles(dir, fo, cursor)
    fo.close()
    cnxn.close()
    print("Get PoE switch list done!")
    os.chdir(saved_path)


