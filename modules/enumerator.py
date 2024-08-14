import builtwith
from colorama import Fore, Back, Style
import getpass, platform, time
import requests

class Enumerator():
    def __init__(self):
        self.url = 'https://www.ugle.org.uk/'
        self.servicesInfo = {}
        self.systemInfo = {}
        self.userInfo = []
        

    def get_services(self):
        data = builtwith.parse(self.url)

        for key in data:
            print(Fore.RED + f'{key.replace('-',' ').title()} => ' + Fore.GREEN + f'{data[key]} \n')
            self.servicesInfo.update({key.replace('-',' ').title():data[key]})  
        return self.servicesInfo

    
    def get_system(self):
        osName = platform.uname()
        timeZone = time.tzname
        ip = requests.get('https://api.ipify.org').text
        userName = getpass.getuser()
        password = getpass.getpass()

        self.systemInfo.update({'OS IP':ip, 
                                'OS Name':osName.system, 
                                'OS Release':osName.release, 
                                'OS Version':osName.version, 
                                'OS Machine':osName.machine, 
                                'OS Processor':osName.processor, 
                                'OS Timezone':timeZone[0],
                                'OS User':userName, 
                                'OS Password':''.join('*' for _ in password)})
        return self.systemInfo

    
def main():
    enumerator = Enumerator()
    services = enumerator.get_services()
    system = enumerator.get_system()
    print(services)
    print(system)

if __name__ == '__main__':
    main()
    




