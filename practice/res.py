import os
import glob

def file_finder(file_ext):
    # Get all available drives
    drives = [d + ':' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(d + ':')]
    print(drives)
    drive = input("Enter drive name, Letter Only: ")
    for root, dirs, files in os.walk(drive + ':\\'):
        # Use glob to find files with the specific extension
        for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
            print(file)
    
    
    # for drive in drives:
    #     print(f"Searching in drive {drive}")
    #     # Use os.walk to iterate through all directories
    #     for root, dirs, files in os.walk(drive + '\\'):
    #         # Use glob to find files with the specific extension
    #         for file in glob.glob(os.path.join(root, f'*.{file_ext}')):
    #             print(file)

fileExt = input('Enter File Extension you want to find (without dot): ')
file_finder(fileExt)
