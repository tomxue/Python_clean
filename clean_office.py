import os
import shutil
import time

def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                #    autoRun.exception( "remove %s error." %filePath )   #引入logging
                    print 'exception occurs'
            elif os.path.isdir( filePath ):
                #if filePath[-4:].lower() == ".svn".lower():
                #    continue
                shutil.rmtree(filePath,True)
    return True

Dir = "C:\\Windows\\temp"
CleanDir(Dir)
Dir = "C:\\Users\\tomxue\\AppData\\Local\\Temp"
CleanDir(Dir)
Dir = "C:\\Users\\xuejd1\\AppData\\Local\\Temp"
CleanDir(Dir)
os.system('pause')


####### kill the target proress ######### 
ret = 0
 
while(1):
    if ret==0:
        print u'目标进程存在，杀死该进程'   
        os.system('TASKKILL /F /IM qq.exe')
        ret = 1
        continue
    else:
        print u'目标进程不存在'   
    print time.strftime("%Y-%m-%d %H:%M:%S")
    ret = os.system('tasklist | find /i "qq.exe"')  # 不区分大小写
    print ret
    print '-'*50
 
    time.sleep(5)