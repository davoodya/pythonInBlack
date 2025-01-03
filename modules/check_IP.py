import ipapi
from colorama import Fore
import requests

def check_IP():
    try:
        response = requests.get('https://api.ipify.org', timeout=60)
        countryName = ipapi.location(response.text)['country_name']
        countryCode = ipapi.location(response.text)['country']
        #print(countryCode)
        if countryCode == 'IR':
            print(Fore.LIGHTRED_EX+"You are in iran..."+'\n'+Fore.LIGHTWHITE_EX+"Please turn your VPN ON...")
        else:
            print(Fore.LIGHTGREEN_EX+f"Your country is {countryName} and Ok")
    except ipapi.exceptions.RateLimited:
        print(Fore.LIGHTRED_EX+"Too many requests. You are in Unsupported Country like Iran, Please turn your VPN ON...")
    except:
        print(Fore.LIGHTRED_EX+"Unknown error happened... Please turn your VPN ON...")
        
#test function
check_IP()
