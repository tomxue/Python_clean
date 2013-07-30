import os
import shutil

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
os.system('pause')