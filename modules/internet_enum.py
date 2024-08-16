import requests
import json
import time
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup

class InternetEnumer():
    def __init__(self):
        self.reqUrl = 'https://domains.yougetsignal.com/domains.php'
        self.result = ''
    
    def reverse_ip_finder(self, url):
        try:
            payload = {'remoteAddress':url, 'key':''}
            response = requests.post(self.reqUrl, data=payload)
            resAsDict = json.loads(response.content.decode())
            
            if resAsDict['status'] == 'Success':
                print(Fore.YELLOW+f'Result: Founded {resAsDict['domainCount']} Websites in same host with https://{resAsDict['remoteAddress']}'+Style.RESET_ALL)
                
                for domain in resAsDict['domainArray']:
                    self.result += f'{domain}\n'
                    print(Fore.LIGHTCYAN_EX+f'[+] {domain}'+Style.RESET_ALL)
                
                return self.result, True
                self.result = ''
            else:
                print(Fore.LIGHTRED_EX + 'Domain Wronge or Not Found!!!'+Style.RESET_ALL)
                return False
            
        except requests.RequestException or requests.ConnectionError:
            print(Fore.LIGHTRED_EX + 'Internet Connection Error!!!'+Style.RESET_ALL)
            return False
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + 'Unknown Error in Reverse IP Finding happened...'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False

    def whois(self):
        pass
    
    def phone_locator(self):
        pass

class main():
    internetEnum = InternetEnumer()
    res = internetEnum.reverse_ip_finder('sabzlearn.ir')
    #print(res[1])
    
if __name__ == '__main__':
    main()