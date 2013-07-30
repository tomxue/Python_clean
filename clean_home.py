import os
import shutil
import sqlite3

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
Dir = "C:\\Users\\Administrator\\AppData\\Local\\Temp"
CleanDir(Dir)
os.system('pause')

# apply database to do something
con = sqlite3.connect("mydb")
cur = con.cursor()
cur.execute('CREATE TABLE if not exists foo(o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')
con.commit()
cur.execute('INSERT INTO foo(o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
con.commit()
print cur.lastrowid

cur.execute('SELECT * FROM foo')
print cur.fetchall()