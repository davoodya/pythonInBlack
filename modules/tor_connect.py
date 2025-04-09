import stem.control
from stem import Signal
import time
import requests
from colorama import Fore
import argparse


def ip_changer(password, control_port, socks_port, sleeptime):
    '''summary: 
    this function changed ip using tor proxy every 10 second
    TOR Configure must be matched to script'''
    while True:
        time.sleep(sleeptime) #Every 10 Seconds TOR Change IP
        with stem.control.Controller.from_port(port=control_port) as controller:
            controller.authenticate(password)
            
            time.sleep(controller.get_newnym_wait())
            
            controller.signal(Signal.NEWNYM)
            print(Fore.YELLOW+"IP Changed... \n Current IP Address => "+Fore.RESET)
        
            proxies = {
                'http':f'socks5h://127.0.0.1:{socks_port}',
                'https':f'socks5h://127.0.0.1:{socks_port}'
            }

            ip = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=60).json()['origin']
            print(Fore.GREEN+ ip +Fore.RESET)

def main():
    parser = argparse.ArgumentParser(description='TOR IP Changer')

    parser.add_argument('-t',type=int,help='Time to change IP',default=10)
    parser.add_argument('-p',type=str,help='TOR Password',default='1234567')
    parser.add_argument('-pp',type=int,help='TOR Proxy Port',default='9999')
    parser.add_argument('-cp',type=int,help='TOR Control Port',default='8888')
   

    args = parser.parse_args()
    try:
        password = args.p
        sleeptime = args.t
        ctrlPort = args.cp
        socksPort = args.pp         
        ip_changer(password=password, control_port=ctrlPort, socks_port=socksPort, sleeptime=sleeptime)
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX+"Exiting... Goodbye & Goodluck 👋👋")
    except Exception as e:
        print(Fore.LIGHTRED_EX+"Unknown Error Happened... \n"+Fore.LIGHTWHITE_EX+f'Error Content: {e}'+Fore.RESET)
        
if __name__ == '__main__':
    main()

'''TOR Configuration file for this scrip => 
SOCKSPort 9999
ControlPort 8888
HashedControlPassword 16:EC10061D9381938260D8DECA1918C97E542DAD3DC57FF6A31BA8E7C863
'''
