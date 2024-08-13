import builtwith
from colorama import Fore, Back, Style

def get_services(url='https://www.ugle.org.uk/'):
    data = builtwith.parse(url)
    for key in data:
        #formatedKey = key.replace('-',' ').title()
        #formatedValue = data[key].replace('-',' ').title()
        #for Increase Script performance
        print(Fore.RED + f'{key.replace('-',' ').title()} => ' + Fore.GREEN + f'{data[key]} \n')
    
    return data

# Test function get_services
'''
url = input(Fore.LIGHTYELLOW_EX+Back.BLUE+'Enter Url: , Leave Empty to use default: https://www.ugle.org.uk/ => '+Style.RESET_ALL)
if url == '':
    get_services()
else:
    get_services(url)
'''