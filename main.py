from modules import enumerator
from modules import translator
from modules import banner_print
from modules import dir_buster


def main():
    banner_print.print_banner()
    option = input("Select Module: ")
    if option == 1:
        dir_buster.dir_buster()
    elif option == 2:
        enumerator.get_services()
    elif option == 3:
        translator.translator()

#TODO
'''
0. Develop and Import banner_print.print_options()
1. Add IP Validator Module
2. Add Cheatsheet Module
3. Create Other Service Option and move Cheatsheet & Translator Modules to this menu
'''