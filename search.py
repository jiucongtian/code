# -*- coding: cp936 -*-

#############################################
#   Written By Qian_F                        #     
#   2013-08-10                               #
#   ��ȡ�ļ�·���б���д�뵽��ǰĿ¼����test.txt #
#############################################

import os
FILENUMBER = 0

def getfilelist(filepath, tabnum=1):
    global FILENUMBER
    simplepath = os.path.split(filepath)[1]
    returnstr = simplepath+"Ŀ¼<>"+"\n"
    returndirstr = ""
    returnfilestr = ""
    filelist = os.listdir(filepath)
    for num in range(len(filelist)):
        filename=filelist[num]
        if os.path.isdir(filepath+"/"+filename):
            returndirstr += "\t"*tabnum+getfilelist(filepath+"/"+filename, tabnum+1)
        else:
            returnfilestr += "\t"*tabnum+filename+"\n"
            print "found file path is:"+filepath+"/"+filename
            FILENUMBER += 1
    returnstr += returnfilestr+returndirstr
    return returnstr+"\t"*tabnum+"</>\n"
            

path = raw_input("�������ļ�·��:")
usefulpath = path.replace('\\', '/')
if usefulpath.endswith("/"):
    usefulpath = usefulpath[:-1]
if not os.path.exists(usefulpath):
    print "·������!"
elif not os.path.isdir(usefulpath):
    print "����Ĳ���Ŀ¼!"
else:
    filelist = os.listdir(usefulpath)
    o=open("test.xml","w+")
    o.writelines(getfilelist(usefulpath))
    o.close()
    print "�ɹ�����鿴test.xml�ļ�"
    print "file number is:"FILENUMBER
	
raw_input("--click return button exit--")
