import requests
import json
import time
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup

class InternetEnumer():
    def __init__(self):
        self.result = ''
    
    def reverse_ip_finder(self, url):
        try:
            reqUrl = 'https://domains.yougetsignal.com/domains.php'
            payload = {'remoteAddress':url, 'key':''}
            response = requests.post(reqUrl, data=payload)
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

    def whois_small(self, url):
        '''Summary
        this function give a domain and 
        return whois information of domain
        '''
        reqUrl = 'https://www.yougetsignal.com/tools/whois-lookup/php/get-whois-lookup-json-data.php'
        payload = {'remoteAddress':url}
        response = json.loads(requests.post(reqUrl, data=payload).content.decode())
        if response['status'] == 'Success':
            whois = str(response['whoisData']).replace('<br />','').replace('%','[+] ')
            whoisNotes, whoisData = whois.split('\n\n\n',1)
            whoisNotes = whoisNotes.split('\n')
            print(Fore.YELLOW + f'Whois Record founded for => ' + Fore.LIGHTGREEN_EX + response['remoteAddress']+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+ 'Whois Notes: \n'+ Fore.LIGHTYELLOW_EX + f'{whoisNotes}' + Style.RESET_ALL+'\n')
            print(Fore.LIGHTRED_EX+ 'Whois Data: \n' + Fore.LIGHTCYAN_EX + f'{whoisData}' + Style.RESET_ALL)
            
        
    
    def phone_locator(self):
        pass

class main():
    internetEnum = InternetEnumer()
    res = internetEnum.whois_small('sabzlearn.ir')
    #print(res[1])
    
if __name__ == '__main__':
    main()