import subprocess
from colorama import Fore, Style, init
import pyfiglet
import os

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("Route Adder")
    sub_banner = pyfiglet.figlet_format("Written by Davood Yakuza", font="small")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + sub_banner)

def add_route():
    print_banner()
    print(os.system('netsh interface ipv4 show interfaces'))
    # Get user input
    ip = input(Fore.GREEN + "Enter the IP address: " + Style.RESET_ALL)
    subnet = input(Fore.GREEN + "Enter the subnet mask: " + Style.RESET_ALL)
    gateway = input(Fore.GREEN + "Enter the gateway: " + Style.RESET_ALL)
    interface_number = input(Fore.GREEN + "Enter the interface number: " + Style.RESET_ALL)
    metric = input(Fore.GREEN + "Enter the metric number: " + Style.RESET_ALL)

    # Construct the route add command
    command = f"route add {ip} mask {subnet} {gateway} IF {interface_number}"

    # Execute the command
    try:
        subprocess.run(command, check=True, shell=True)
        print(Fore.LIGHTGREEN_EX + "Route added successfully.")
    except subprocess.CalledProcessError as e:
        print(Fore.LIGHTRED_EX + f"Failed to add route: {e}")

if __name__ == "__main__":
    add_route()
