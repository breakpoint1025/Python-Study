import os
import fileinput
import sys

def processdir(dir):
    file_list = os.listdir(dir)
    for f in file_list:
        file_path = os.path.join(dir, f)
        if os.path.isfile(file_path):
            if f == "TextTemplates_EventTypes.xml":
                
                with open(file_path,'r', encoding = 'utf-8') as r:
                    lines = r.readlines()
                
                with open(file_path,'w', encoding = r.encoding) as w:
                    linenum = 0
                    while linenum <  len(lines):
                        line = lines[linenum]
                        linenum += 1
                        if line.find(strparttern) != -1 and line.find(endTag) != -1:
                            continue
                        if line.find(strparttern) != -1 and line.find(endTag) == -1:
                            while linenum <  len(lines):
                                subline = lines[linenum]
                                linenum += 1
                                if subline.find(endTag) != -1:                                   
                                    break
                        else:
                            w.writelines(line)
                      
        if os.path.isdir(file_path):
            processdir(file_path)


if __name__ == '__main__':

    files_Path = sys.argv[1]
    #files_Path = r"E:\SM7\Git\7.2.2\SystemManager\Main\SMXST\SM.I18N.EN"
    strparttern = r"E100X"
    endTag = r"</TextTemplate>"
    
    if not(os.path.isdir(files_Path)):
        print("Invalid dir!")
        exit
   
    processdir(files_Path)

    print("Search and Remove content done!")
                    





