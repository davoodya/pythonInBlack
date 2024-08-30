from colorama import Fore, Style, Back, init
import subprocess
import os
import glob
import pyfiglet
import multiprocessing

from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

init(autoreset=True)

class FileFinderMultiCore():
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
        
    def search_directory(self, root, file_ext):
        return glob.glob(os.path.join(root, f'*.{file_ext}'))

    def file_finder_Drive(self, file_ext, drive):
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        systemPartition = drives

        with ThreadPoolExecutor() as executor:
            futures = []
            for root, dirs, files in os.walk(drive + ':\\'):
                futures.append(executor.submit(self.search_directory, root, file_ext))
            
            for future in as_completed(futures):
                for file in future.result():
                    print(file)

        return systemPartition

    def file_finder_all(self, file_ext):
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]

        with ThreadPoolExecutor() as executor:
            futures = []
            for drive in drives:
                print(f"Searching in drive {drive}")
                for root, dirs, files in os.walk(drive + '\\'):
                    futures.append(executor.submit(self.search_directory, root, file_ext))
            
            for future in as_completed(futures):
                for file in future.result():
                    print(file)
    

class FileFinderSingleCore():
    def __init__(self):
        pass
    def file_finder_Drive(self, file_ext, drive):
        # Get all available drives
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        self.systemPartition = drives
        
        #print(f'System All Drives: {drives}')
        
        for root, dirs, files in os.walk(drive + ':\\'):
            # Use glob to find files with the specific extension
            for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
                    print(file)
          
        return self.systemPartition      
                
    def file_finder_all(self, file_ext):
        # Get all available drives
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        #print(drives)
        
        for drive in drives:
            print(f"Searching in drive {drive}")
            # Use os.walk to iterate through all directories
            for root, dirs, files in os.walk(drive + '\\'):
                # Use glob to find files with the specific extension
                for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
                    print(file)

class FileFinderVerbose():
    def __init__(self):
        pass
    
    def search_directory(self, root, file_ext):
        results = []
        for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
            results.append(file)
        return results

    def file_finder_Drive(self, file_ext, drive):
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        self.systemPartition = drives
        print(f'System All Drives: {drives}')

        pool = multiprocessing.Pool()
        search_func = partial(self.search_directory, file_ext=file_ext)
        
        for root, dirs, files in os.walk(drive + ':\\'):
            results = pool.apply_async(search_func, (root,))
            for file in results.get():
                print(file)
        
        pool.close()
        pool.join()
        return self.systemPartition

    def file_finder_all(self, file_ext):
        drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
        print(drives)

        pool = multiprocessing.Pool()
        search_func = partial(self.search_directory, file_ext=file_ext)

        for drive in drives:
            print(f"Searching in drive {drive}")
            for root, dirs, files in os.walk(drive + '\\'):
                results = pool.apply_async(search_func, (root,))
                for file in results.get():
                    print(file)

        pool.close()
        pool.join()


def print_banner():
    banner = pyfiglet.figlet_format("Yakuza File Engine", font="slant")
    print(Style.BRIGHT+Fore.BLUE + banner + Style.RESET_ALL)
  
def print_menu():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "1. Find files in a specific drive")
    print(Fore.YELLOW + "2. Find files in all drives")
    print(Fore.YELLOW + "3. List partitions")
    print(Fore.YELLOW + "4. Exit")
    print(Fore.CYAN + "=" * 50)
    
    print("All Drives: ", end="")
    os.system('fsutil fsinfo drives')

def main():
    fileFinderMC = FileFinderMultiCore()
    
    while True:
        print_banner()
        print_menu()
        
        choice = input(Fore.GREEN + "Enter your choice (1-4): " + Fore.RESET)
        
        if choice == '1':
            drive = input(Fore.MAGENTA + "Enter drive letter: " + Fore.RESET).upper()
            ext = input(Fore.MAGENTA + "Enter file extension (without dot): " + Fore.RESET)
            print(Fore.CYAN + "\nSearching files...\n")
            fileFinderMC.file_finder_Drive(file_ext=ext, drive=drive)
        elif choice == '2':
            ext = input(Fore.MAGENTA + "Enter file extension (without dot): " + Fore.RESET)
            print(Fore.CYAN + "\nSearching files in all drives...\n")
            fileFinderMC.file_finder_all(file_ext=ext)
        elif choice == '3':
            print(Fore.CYAN + "\nListing partitions...\n")
            fileFinderMC.list_partitions()
        elif choice == '4':
            print(Fore.RED + "\nExiting Yakuza File Engine. Goodbye!")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.")
        
        input(Fore.GREEN + "\nPress Enter to continue..." + Fore.RESET)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()  


