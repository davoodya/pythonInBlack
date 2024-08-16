'''TODO
0. add translator for Scam Detecion Result
1. Add Option Menu
2. Completed & Packaged Class to Use in Yakuza T-Rat as Internet Enumeration Module
3. Complete Scam Detection..
Until => Scam Detection Function
'''

import requests
import json
import time
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup

class InternetEnumer():
    def __init__(self):
        self.viewDnsToken = '8b68262a1806e38816e34b9aca3cf11106bf08d2'
        self.result = ''
    
    def reverse_ip_finder(self, url):
        try:
            reqUrl = 'https://domains.yougetsignal.com/domains.php'
            payload = {'remoteAddress':url, 'key':''}
            response = requests.post(reqUrl, data=payload)
            resAsDict = json.loads(response.content.decode())
            
            if resAsDict['status'] == 'Success':
                print(Fore.YELLOW+f'[+] Result: Founded {resAsDict['domainCount']} Websites in same host with https://{resAsDict['remoteAddress']}'+Style.RESET_ALL)
                
                for domain in resAsDict['domainArray']:
                    self.result += f'{domain}\n'
                    print(Fore.LIGHTCYAN_EX+f'[+] {domain}'+Style.RESET_ALL)
                
                return self.result, True
                self.result = ''
            else:
                print(Fore.LIGHTRED_EX + '[-] Reverse IP Finder: Domain Wronge or Not Found!!!'+Style.RESET_ALL)
                return False
            
        except requests.RequestException or requests.ConnectionError:
            print(Fore.LIGHTRED_EX + '[-] Reverse IP Finder: Internet Connection Error!!!'+Style.RESET_ALL)
            return False
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Reverse IP Finder: Unknown Error happened!!!'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False

    def whois_small(self, url):
        '''Summary
        this function give a domain and 
        return whois information of domain
        '''
        try:
            reqUrl = 'https://www.yougetsignal.com/tools/whois-lookup/php/get-whois-lookup-json-data.php'
            payload = {'remoteAddress':url}
            
            response = json.loads(requests.post(reqUrl, data=payload).content.decode())
            
            if response['status'] == 'Success':
                #Formating whois result 
                whois = str(response['whoisData']).replace('<br />','').replace('%','[+] ')
                
                #Formating whois result and then 
                whoisNotes, whoisData = whois.split('\n\n\n',1)
                whoisNotes = whoisNotes.split('\n')
                
                #print whoisNotes & whoisData 
                print(Fore.YELLOW + f'Whois Record founded for => ' + Fore.LIGHTGREEN_EX + response['remoteAddress']+Style.RESET_ALL)
                print(Fore.LIGHTRED_EX+ 'Whois Notes: \n'+ Fore.LIGHTYELLOW_EX + f'{whoisNotes}' + Style.RESET_ALL+'\n')
                print(Fore.LIGHTRED_EX+ 'Whois Data: \n' + Fore.LIGHTCYAN_EX + f'{whoisData}' + Style.RESET_ALL)
                
                #return whoisData, whoisNotes, True
                return {'success':True,'whoisData':whoisData, 'whoisNotes':whoisNotes}
            else:
                print(Fore.LIGHTRED_EX + '[-] Whois Record: Wrong Domain or Host Not Founded!!!'+Style.RESET_ALL)
            
        except requests.RequestException or requests.ConnectionError:
            print(Fore.LIGHTRED_EX + '[-] Whois Record: Internet Connection Error!!!'+Style.RESET_ALL)
            return False
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Whois Record: Unknown Error!!!'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False
    
    def open_ports(self, url):
        '''summary
        this function get host open ports
        and return as dict have openPorts & closedPorts Keys
        '''
        
        reqUrl = f'https://api.viewdns.info/portscan/?host={url}&apikey={self.viewDnsToken}&output=json'
        #payload = {'host':url,'output':'json','apikey':self.viewDnsToken}
        try:
            respose = requests.get(reqUrl).text
            respose = json.loads(respose)
            
            result = {'openPorts':[],'closedPorts':[]}
            
            for x in respose['response']['port']:
                
                if x['status'] == 'closed':        
                    print(Fore.YELLOW + f'[+] Service: {x['service']} On ' + Fore.LIGHTCYAN_EX + \
                    f'Port: {x['number']} and ' + Fore.LIGHTRED_EX + f'Port is  {x['status']}'+ Style.RESET_ALL+'\n')
                    
                    result['closedPorts'].append(f'{x['service']}-{x['number']}')
                    
                elif x['status'] == 'open':
                    print(Fore.YELLOW + f'[+] Service: {x['service']} On ' + Fore.LIGHTCYAN_EX + \
                    f'Port: {x['number']} and ' + Fore.LIGHTGREEN_EX + f'Port is {x['status']}' + Style.RESET_ALL+'\n')
                    
                    result['openPorts'].append(f'{x['service']}-{x['number']}')
                    
                else:
                    print(Fore.YELLOW + f'[+] Service: {x['service']} On ' + Fore.LIGHTCYAN_EX + \
                    f'Port: {x['number']} and ' + Fore.LIGHTYELLOW_EX + f'Port is Unknown {x['status']}'+ Style.RESET_ALL+'\n')
                    
                    result['closedPorts'].append(f'{x['service']}-{x['number']}')
        except requests.RequestException or requests.ConnectionError:
            print(Fore.LIGHTRED_EX + '[-] Port Scanner: Internet Connection Error!!!'+Style.RESET_ALL)
            return False
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Port Scanner: Unknown Error!!!'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False    
        return result
    
    def scam_detection(self, url):
        '''summary
        this function detect scam website
        '''
        reqUrl = f'https://scamminder.com/websites/{url}/' 
        #secondReqUrl = 'https://www.scamadviser.com/check-website'
        
        try:
            response = requests.get(reqUrl)
            soup = BeautifulSoup(response.content.decode(),'html.parser')

            #Find div tag contain Result of Response
            aiResult = str(soup.findAll('div',attrs= {'class':'card-text p-10'}))[29:-7]
            aiAnalyze, aiReason  = aiResult.split('<br/><br/><b>', 1)
            print(Fore.GREEN + f'[+] AI Analyze => \n' + Fore.WHITE + f'{aiAnalyze}'+Style.RESET_ALL+'\n')
            print(Fore.GREEN + f'[+] AI Reason for this Analyze => \n' + Fore.WHITE + f'{aiReason}'+Style.RESET_ALL+'\n')
            
            negativePoint = soup.findAll('table', attrs={'class':'table table-borderless'})
            negativePoint2 = soup.findAll('p', attrs={'class':'mb-0 fw-medium'})
            
            print(Fore.GREEN +'\n[+] Negative and Positive pointof Website'+Style.RESET_ALL+'\n')
            
            for x in negativePoint:
                tableRow = x.findAll('td')
                for y in tableRow:
                    formatedRes = str(y.text).replace('  ','\n')
                    print(Fore.YELLOW + f'[+] {formatedRes} \n'+Style.RESET_ALL)
                
        
        except requests.RequestException or requests.ConnectionError:
            print(Fore.LIGHTRED_EX + '[-] Scam Detection: Internet Connection Error!!!'+Style.RESET_ALL)
            return False
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Scam Detection: Unknown Error!!!'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False
        
        
    def phone_locator(self):
        pass

class main():
    internetEnum = InternetEnumer()
    #res = internetEnum.whois_small('sabzlearn.ir')
    #print(res[1])
    internetEnum.scam_detection('toplearn.com')
    
if __name__ == '__main__':
    main()