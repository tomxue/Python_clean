# Filename: backup_ver4.py  
import os  
import time
import sys
  
# 1.需要备份的文件目录  
source1 = 'C:\\Users\\Administrator\\Desktop'
source2 = r'"C:\Program Files (x86)\Vim"'
source3 = 'D:\\ScrapBook_2013-7-16'
cwd = 'C:\\Program Files\\WinRAR'
  
# 2. 备份文件到目标路径  
target_dir = 'D:\\Dropbox\\VMware_share\\Backup\\'
  
# 3. The files are backed up into a zip file.  
# 4. The current day is the name of the subdirectory in the main directory  
PathOfToday = target_dir + time.strftime('%Y-%m-%d')
print PathOfToday
# The current time is the name of the zip archive  
now = time.strftime('%H-%M-%S')
print now
  
# Take a comment from the user to create the name of the zip file  
comment = raw_input('Enter a comment -->')  
if len(comment)==0:   
    target = PathOfToday+os.sep+now+'.zip'
    print target
else:  
    target = PathOfToday+os.sep+now+'_'+\
             comment.replace(' ','_')+'.zip'
    # Notice the backslash!  
  
# Create the subdirectory if it isn't already there  
if not os.path.exists(PathOfToday):  
    os.mkdir(PathOfToday)  # make directory  
    print('Successfully created directory', PathOfToday)  
  
# 5. 用winrar的rar命令压缩文件，但首先要安装有winrar且设置winrar到环境变量的路径path中
rar_scrapbook = raw_input('Do you want to add Scrapbook to your rar package? (y/n)')
if rar_scrapbook == 'y':
    rar_command = "rar a %s %s %s %s & pause" %(target, source1, source2, source3)
elif rar_scrapbook == 'n':
    rar_command = "rar a %s %s %s & pause" %(target, source1, source2)
else:
    print 'Quit'
    raise SystemExit
  
# Run the backup  
# 设置winrar到path环境中，这里已经手动添加，如图  
# os.system('set Path=%Path%;C:\\Program Files\\WinRAR')
os.chdir(cwd)
ret = os.system(rar_command)
print 'Successful backup to', target, '.', 'And return value =', ret