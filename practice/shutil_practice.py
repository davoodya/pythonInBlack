import shutil
import os

#os.mkdir(r'../practice/')
os.chdir(r'../practice/')
open('test.txt','w').close()

'''Copy File

1. Copy file into new file
shutil.copy(r'../modules/exposer.py',r'./exposer.py')

1.2 Copy file into directory
shutil.copy(r'./test.txt',r'../resources/')

1.3 copy file into new file if directory not exists
shutil.copy(r'./exposer.py',r'../NewFolder')

1.4 if directory in path don't exist, so got error
shutil.copy(r'./exposer.py',r'../NewFolder/exposer.py')

'''

'''#2. Copy whole directory

#shutil.copytree(r'../modules',r'./NewModules')

#if NewModules Exist we got FileExistError, But we can use dirs_exists_ok=True
#shutil.copytree(r'../modules',r'./NewModules',dirs_exist_ok=True)'''


'''#3.1 Move Files/Dirs
Move file into existing directory
#shutil.move(r'./exposer.py',r'../resources')

#3.2 Move file into new file 
#shutil.move(r'./exposer.py',r'../resources/NewExposer.py')

#3.3 copy file into new file if directory not exists
#shutil.move(r'./exposer.py',r'../NewFolder')

#3.4 Move all files in dirctory to new directory
shutil.move(r'./', r'../new')
'''
#4. Get file size
print(shutil.disk_usage(__file__))
