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
    print(f"{Fore.YELLOW}{Style.BRIGHT}" + main_banner)
    print(f"{Back.BLACK}{Fore.WHITE}{Style.BRIGHT}" + small_banner + Style.RESET_ALL)
    print(f"{Back.WHITE}{Fore.BLACK}{Style.BRIGHT}" + "=" * 50 + Style.RESET_ALL)

def get_ip_input():
    ip_input = input(Fore.GREEN + "Enter IP address (or 1 for your current public IP): " + Style.RESET_ALL)
    if ip_input.strip() == "1":
        # Get the user's current public IP from ipify
        try:
            response = requests.get('https://api.ipify.org?format=json')
            response.raise_for_status()
            return response.json().get('ip')
        except requests.RequestException as e:
            print(f"{Fore.RED}Error retrieving current IP: {e}")
            return None
    else:
        return ip_input.strip()

def get_ip_location(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"{Fore.RED}Error retrieving location data: {e}")
        return None

def print_location_data(location_data):
    if not location_data:
        print(f"{Fore.RED}No location data available.")
        return

    print(f"{Fore.CYAN}{Style.BRIGHT}\nIP Location Data:\n")
    for key, value in location_data.items():
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{key.capitalize()}: {Fore.WHITE}{value}")

def main():
    print_banner()

    ip = get_ip_input()
    if not ip:
        print(f"{Fore.RED}Invalid input. Exiting.")
        return

    print(f"{Fore.YELLOW}{Style.BRIGHT}Target IP Address: {Fore.WHITE}{ip}")
    
    location_data = get_ip_location(ip)
    print_location_data(location_data)

if __name__ == "__main__":
    main()
