import requests
from bs4 import BeautifulSoup
import html
from colorama import Fore, Back, Style

''' parse_html_response() Summary
    Parses the HTML response from the given URL and extracts the networking commands from the cheat sheet.
    
    Returns:
        None. Prints the command, description, and example for each networking command found in the cheat sheet.
        Skips lines that do not have exactly three tab-separated parts.
'''
yakuzaBanner = f"""{Fore.LIGHTRED_EX}
╭╮╱╱╭╮╱╭╮              ...............{Fore.LIGHTBLUE_EX}
┃╰╮╭╯┃╱┃┃              ....-*###+.....
╰╮╰╯╭┻━┫┃╭┳╮╭┳━━━┳━━╮  ...%@@-.@@.....
╱╰╮╭┫╭╮┃╰╯┫┃┃┣━━┃┃╭╮┃  ..*@@@%#*-  :..{Fore.CYAN}
╱╱┃┃┃╭╮┃╭╮┫╰╯┃┃━━┫╭╮┃  ..=@@=..    :..
╱╱╰╯╰╯╰┻╯╰┻━━┻━━━┻╯╰╯  .. =%:..  .....
{Fore.YELLOW}Written By: D.Yakuza{Fore.RESET}   .... :.........
{Fore.LIGHTRED_EX}you say DAYA  {Fore.RESET}
"""



def parse_html_response():
    testUrl = 'https://www.geeksforgeeks.org/linux-commands-cheat-sheet/'
    response = requests.get(testUrl)
    soup = BeautifulSoup(response.text, 'html.parser') #also use content
    
    networkingSection = soup.find('h2',string='6. Networking Commands')
    if networkingSection:
        networkingTable = networkingSection.find_next('table')
        if networkingTable:
            #parsedNetworkingTable = html.unescape(str(networkingTable)) #Parse HTML Codes
            table_text = networkingTable.get_text(strip=True)
            print(networkingTable.prettify()) #Pring page html code's
            lines = table_text.split('\n') # Split each line
            for line in lines:
                parts = line.split('\t') #Split each word by tab
                if len(parts) == 3:
                    command, description, example = line.split('\t')
                    print(f'Command: {command} \n')
                    print(f'Description: {description} \n')
                    print(f'Example: {example} \n')
                    print()
                else:
                    print(f'Line Content \n {line}')
                    print(f"Skipping lines: {len(line)} \n")
        else:
            print('Network Command Section Tables Not Found')
    else:
        print('Network Command Section Not Found')
    
    
    #print(soupRes)
    #print(response.content.decode().find('List files and directories'))

def option_selector():
    options = """ Select language you want get usage Cheatsheet 
    [0]- Shell commands
    [1]- Python
    [2]- GoLang
    [3]- JavaScript
    [4]- Rust
    [5]- Cpp
    [6]- Csharp
    [99]- Exit
    """
    print(options)

    while True:
        selectedOpt = input("Select Option by Number: ")
        print(f"OK You slected {selectedOpt}")
        if selectedOpt == '99':
            print('Exit; Goodbye & Goodluck 👋 !!!')
            exit()
        elif selectedOpt not in ['0', '1', '2', '3', '4', '5', '6', '99']:
            print('Invalid Option, Enter again')
            continue
        else:
            try:
                return int(selectedOpt)
            except TypeError:
                print("Enter Number of Option,  Enter again")
                continue
            except ValueError:
                print("Enter Number of Option, Enter again")
                continue

def get_cheatsheet(cmd):
    url = 'https://cheat.sh' #    url1 = 'https://cht.sh'
    # ----------------- Formatting Example ----------------- 
    #url2 = 'cheat.sh/python/built+in+methods' #get language methods cheatsheet
    #url2 = 'cheat.sh/nmap' #get commands cheatsheet
    try:
        response = requests.get(f'{url}/{cmd}')
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.status_code == 200:
            print(response.text) #print(soup.prettify())
            return response.text
        else:
            print(f"Error: {response.status_code}")
    except:
        print(f'Unknown Error')


def main():
    print(yakuzaBanner)
    command = input(Back.LIGHTMAGENTA_EX+Fore.WHITE+"Enter a command to get cheatsheet: "+Style.RESET_ALL)
    get_cheatsheet(command)
    
if __name__ == '__main__':
    main()