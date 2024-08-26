from colorama import Fore
import subprocess
import os
import glob

class FileSystem():
    def __init__(self):
        self.systemPartition = []
    
    def list_partitions(self):
        #Way0  to get Partitions on machine
        print(Fore.YELLOW+"---------Way 0----------=> Using subprocess.getoutput('fsutil fsinfo drives')\n"+Fore.RESET)
        result = subprocess.getoutput('fsutil.exe fsinfo drives')
        print(result)

        result = result.replace("Drives: ","").split()
        for part in result:
            print(f'[+] Partitions => {part}')
        print(Fore.BLUE+"-----------------------------------------\n"+Fore.RESET)



        #Way1 to get Partitions and shared objects on machine
        print(Fore.YELLOW+"---------Way 1----------=> Using subprocess.run(['net', 'share'])\n"+Fore.RESET)

        result1 = subprocess.run(['net', 'share'], shell=True,stdout=subprocess.PIPE)
        print(result1.stdout.decode())
        print(Fore.BLUE+"-----------------------------------------\n"+Fore.RESET)


        #Way2 to get Partitions on machine
        print(Fore.YELLOW+"---------Way 2----------=> Using subprocess.Popen(['fsutil.exe', 'fsinfo', 'drives'])\n"+Fore.RESET)

        result2 = subprocess.Popen(['fsutil.exe', 'fsinfo', 'drives'], shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        #formatedResult = result2.stdout.decode('utf-8')
        formatedResult = str(result2)
        formatedResult = formatedResult.replace("Drives: ","").split()

        for part in formatedResult:
            print(f'[+] Partitions => {part}')
        print(Fore.BLUE+"-----------------------------------------\n"+Fore.RESET)

        #print(result.stdout.decode())
        #print(result.stderr.decode())
        
    def file_finder_Drive(self, file_ext, drive):
        # Get all available drives
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        self.systemPartition = drives
        
        print(f'System All Drives: {drives}')
        
        for root, dirs, files in os.walk(drive + ':\\'):
            # Use glob to find files with the specific extension
            for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
                    print(file)
          
        return self.systemPartition      
                
    def file_finder_all(self, file_ext):
        # Get all available drives
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        print(drives)
        
        for drive in drives:
            print(f"Searching in drive {drive}")
            # Use os.walk to iterate through all directories
            for root, dirs, files in os.walk(drive + '\\'):
                # Use glob to find files with the specific extension
                for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
                    print(file)

print("All Drives: ")
os.system('fsutil fsinfo drives')

fileSystem = FileSystem()

drive = input("Select Drive by Enter drive name, Letter Only: ").upper()
ext = input("Enter File Extension you want to find (without dot): ")
fileSystem.file_finder_Drive(file_ext=ext, drive=drive)