import os

def file_creator():
    if os.path.exists(r'H:/Repo/NewFolder'):
        os.chdir(r'H:/Repo/NewFolder')
        for x in range(4):
            open(rf'./ransomware{x}.txt', 'w').close()
        print('Files Created\n')
    
    else:
        print('Creating Directory...\n')
        os.makedirs(r'H:/Repo/NewFolder')    
        os.chdir(r'H:/Repo/NewFolder')
        for x in range(4):
            open(rf'./ransomware{x}.txt', 'w').close()
        print('Files Also Created\n')

def ransomware():
    os.chdir(r'H:/Repo/NewFolder')
    fileList = os.listdir()
    for file in fileList:
        print(f'Dir List => \n{os.listdir()}')
        if file.endswith('.txt'): #if file[-3] == "txt":
            os.remove(file)
            print(f'{file} has been deleted\n')
        
    print(f'Final Directory List: \n{os.listdir()}')

def main():
    file_creator()
    ransomware()
if __name__ == '__main__':
    main()