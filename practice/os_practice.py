import os

os.chdir(r'H:/Repo/')

#0. Change Directory
#print(os.listdir())

#1. File Properties
#print(os.stat(__file__).st_size)
#print(os.stat(__file__).st_uid)

#2. Create Directory
#os.chdir(r'H:/Repo/')
#os.mkdir('NewFolder')

#3. Create Directories
# os.makedirs((r"New1/New2/New3"))
# os.chdir(r'./New1/New2/New3')

#4. Write New file
'''4.1 
fileDescriptor = os.open(r'H:/Repo/new1.txt',os.O_CREAT | os.O_WRONLY)
os.write(fileDescriptor, "Hello Ninja".encode())
4.2
with open(r'H:/Repo/new.txt','w') as fd:
    os.write(fd.fileno(),b'Hello World')
'''

#5.Remove File 
#os.remove(r'H:/Repo/new.txt')

#6. Remove Directory
'''os.mkdir(r'H:/Repo/NewFolder')
print(os.listdir())

os.rmdir(r'H:/Repo/NewFolder')
print(os.listdir())
'''
#7. Rename File
'''with open(r'H:/Repo/New1.txt','w') as fd:
    os.write(fd.fileno(),b'Hello Ninja...')
print(os.listdir())

os.rename(r'H:/Repo/New1.txt',r'H:/Repo/Yakuza.txt') ; print(os.listdir())
'''
#8. File Size
'''fileSize = os.stat(r'H:/Repo/Yakuza.txt').st_size
print(f'File is {fileSize/1000} Kilobytes')

if fileSize >= 1000:
    print('File is Biggeer than 1000 bytes')
else:
    print('File is too small')
 '''   
#9. File Permissions

