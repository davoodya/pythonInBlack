import requests
from colorama import init, Fore, Style, Back
import pyfiglet

# Initialize colorama
init(autoreset=True)

def print_banner():
    # Create banners using pyfiglet
    main_banner = pyfiglet.figlet_format("IP Locator", font="slant")
    small_banner = pyfiglet.figlet_format("Written by D.Yakuza", font="small")

    # Print the banners with color
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+main_banner)
    #print(main_banner)
    print(f"{Back.BLACK+Fore.WHITE}{Style.BRIGHT}"+small_banner+Style.RESET_ALL)
    #print(small_banner)
    print(f"{Back.WHITE+Fore.BLACK}{Style.BRIGHT}" + "=" * 50)
    print(Style.RESET_ALL)

def get_user_ip():
    ipUser = input(Fore.GREEN + "Enter your IP address: " + Style.RESET_ALL)
    return ipUser

    # # Send a request to ipify to get the user's IP address
    # response = requests.get('https://api.ipify.org?format=json')
    # ip_data = response.json()
    # return ip_data['ip']

def get_ip_location(ip):
    # Send a request to ipapi to get the location data for the IP address
    response = requests.get(f'https://ipapi.co/{ip}/json/', timeout=60)
    location_data = response.json()
    return location_data

def print_location_data(location_data):
    # Print the location data with colors
    print(f"{Fore.CYAN}{Style.BRIGHT}\nIP Location Data:\n")
    for key, value in location_data.items():
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{key.capitalize()}: {Fore.WHITE}{value}")

def main():
    # Print the banners
    print_banner()
    
    # Get the user's IP address
    ip = get_user_ip()
    print(f"{Fore.YELLOW}{Style.BRIGHT}Your IP Address: {Fore.WHITE}{ip}")
    
    # Get the location data for the IP address
    location_data = get_ip_location(str(ip))
    
    # Print the location data
    print_location_data(location_data)

if __name__ == "__main__":
    main()
