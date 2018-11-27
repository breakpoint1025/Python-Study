import os
import fileinput
import sys

def processline(line):
    if line.find(strparttern1) != -1 and line.find("//") == -1:
        oldstr = line[line.find(strparttern1):line.find(")")+1]
        newstr = "{0}{newver}".format(strparttern1, newver = new_ver)
        line = line.replace(oldstr, newstr)
    if line.find(strparttern2) != -1 and line.find("//") == -1:
        oldstr = line[line.find(strparttern2):line.find(")")+1]
        newstr = "{0}{newver}".format(strparttern2, newver = new_ver)
        line = line.replace(oldstr, newstr)
    print(line, end='')

def processdir(dir):
    file_list = os.listdir(dir)
    for f in file_list:
        file_path = os.path.join(dir, f)
        if os.path.isfile(file_path):
            if f == 'AssemblyInfo.cs':
                with fileinput.input(file_path, inplace=True) as f:
                    for line in f:
                        processline(line)
        if os.path.isdir(file_path):
            processdir(file_path)

if __name__ == '__main__':

    snmpserver_source_code_dir = sys.argv[1]
    new_ver = "(\"{0}\")".format(sys.argv[2])
    strparttern1 = "AssemblyInformationalVersion"
    strparttern2 = "AssemblyVersion"
    
    if not(os.path.isdir(snmpserver_source_code_dir)):
        print("Invalid snmpserver_source_code_dir!")
        exit  

    processdir(snmpserver_source_code_dir)

    print("Snmp Server AssemblyVersion Replace Done!")
                    





