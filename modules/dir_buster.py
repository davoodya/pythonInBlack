from colorama import Fore, Back, Style
import requests
import socket
from banner_print import print_dir_banner 
from security import safe_requests

'''
dirList = open('dirlist_small.txt', 'r').read()
#dirListFormated = dirList.split('\n') 
dirListFormated = dirList.splitlines() # Formating each word in list
attackResult = {'dir':'url'}
inputUrl = input('Enter url with http:// or https:// => ')
'''

menuOptions = """
[1]-Normal Attack Mode, Only Print Founded Directories
[2]-Verbose Mode, Print Founded and Invalid Directories
[3]-Advance Attack Mode, Select Wordlist for Attack
[99]-Exit
"""

def dir_buster():
    # Infinity Input until Enter 99
    while True: 
        # Open dir list file and splited each word in new line
        try:
            inputList = input(Back.LIGHTWHITE_EX+Fore.RED+'Enter list full path:  Leave empty to use default list(SecList-dir-medium). Also Enter 99 to exit: '+Style.RESET_ALL+'\n')
            formatedInputList = inputList.replace("\\","\\\\") # Path Compatible for Windows
            if inputList == '99':
                print(Fore.CYAN + Style.BRIGHT + f'Exitting. Goodluck!! 👋 \n')
                exit()
            elif inputList == "":
                dirList = open(r'H:/Repo/black_python/mini_projects/wordlists/dirlist_medium.txt', 'r').read()
                dirListFormated = dirList.splitlines() # Formating each word in new Line
                #dirListFormated = dirList.split('\n')
            elif inputList != '':
                try:
                    dirList = open(formatedInputList, 'r').read()
                    dirListFormated = dirList.splitlines()
                except FileNotFoundError:
                    print(Fore.RED + f'File not found \n')
                    continue
                except:
                    print(Fore.RED + f'Unknown Error \n')
                else:
                    print(Fore.GREEN+Style.DIM+f'{inputList}'+Style.RESET_ALL+'\n')
                    print(Back.GREEN+Fore.BLACK+Style.DIM+f'Wordlist Loaded Succesfully'+Style.RESET_ALL+'\n')
                    
                    # Wordlist Imported End
                    
            attackResult = {'dir':'url'} # Save founded dir and url
            inputUrl = input(Back.BLUE+Fore.WHITE+Style.BRIGHT+'Enter url with http:// or https:// => , Enter 99 to exit:'+Style.RESET_ALL+'\n')
            if inputUrl == '99': # Exit if Enter 99
                print(Fore.CYAN + Style.BRIGHT + f'Exitting. Goodluck!! 👋 \n')
                exit()
        except KeyboardInterrupt:
            print(Fore.CYAN + Style.BRIGHT + f'Exitting. Goodluck!! 👋 \n')
            exit()
        
        print(Back.GREEN+Fore.BLACK+Style.DIM+'...Attack is Statring ...'+Style.RESET_ALL+'\n')
        for word in dirListFormated: 
            try: # Formating URL and Send Request to URL with directory in file
                url = inputUrl+'/'+word
                response = safe_requests.get(url)
                if response.status_code == 200:
                    print(Fore.GREEN + f'Directory found => {word} \n')
                    print(Fore.GREEN + f'Directory Full URL => {url} \n')
                    attackResult.update({word, url})
                    try:
                        writeRes = open('H:\\Repo\\black_python\\mini_projects\\modules\\result.txt', 'a')
                        writeRes.write(f'dir: {word} , url => {url} \n')
                        writeRes.close()
                    except:
                        print(Fore.RED + f'Error while writing result \n')
                elif response.status_code == 404:
                    print(Fore.RED + f'{url} => {response.status_code} \n')
                else:
                    print(Fore.LIGHTYELLOW_EX + f'{url} => {response.status_code} \n')
            
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f'Internet Connection Error !!! \n')
                print(Fore.LIGHTRED_EX+'Error Message: '+Fore.LIGHTWHITE_EX+f' {e} \n')
                break #exit()
                #continue #use while and an input to inifinite request try
                
            except KeyboardInterrupt:
                if len(attackResult) > 1:
                    for result in attackResult:     
                        writeResult = open('H:\\Repo\\black_python\\mini_projects\\modules\\result2.txt', 'a')
                        writeResult.write(f'dir => {result} , url => {attackResult[result]} \n')
                        print(Fore.LIGHTGREEN_EX + f'dir => {result} , url => {attackResult[result]} \n')
                    writeResult.close()
                else:
                    print(Fore.RED + f'No directories found \n')
                    
                print(Fore.CYAN + f'Exitting. Goodluck!! 👋 \n')
                exit()
                
            except:
                print(Fore.LIGHTYELLOW_EX + f'dir: {word} => {url}'+ Fore.LIGHTRED_EX +f'Status Code: {response.status_code} \n')
                print(Fore.LIGHTYELLOW_EX + f'Unknown Error \n')
                
        
        if len(attackResult) > 1:
            for result in attackResult:
                writeResult = open('H:\\Repo\\black_python\\mini_projects\\modules\\result2.txt', 'a')
                writeResult.write(f'dir => {result} , url => {attackResult[result]} \n')
                print(Fore.LIGHTGREEN_EX + f'dir => {result} , url => {attackResult[result]} \n')
            writeResult.close()
            return attackResult
        elif len(attackResult) == 1:
            print(Fore.RED + f'No directories found \n')
            #continue => 
            #after define function use while for infinity input url and check exit by 99, so this continue back to start loop
                
        
            

#test function dir_buster()
def main():
    try:
        print_dir_banner()
        input(Back.WHITE+Fore.BLACK+ "Welcom to 'Dir Bsuter' Ninja 🥷 "+ Back.RESET+Fore.LIGHTWHITE_EX+' Press Enter to Start...'+Style.RESET_ALL+'\n')
        dir_buster()
    except:
        print(Fore.LIGHTRED_EX + '[-] CTRL+C Detecting => Exit !!!'+Style.RESET_ALL)

if __name__ == '__main__':
   main()
   
   
#TODO
# Fix Writing Result => Replace Line 67 to 104, 86
# Add Options Menu for applet
# Add a banner
# Return results
