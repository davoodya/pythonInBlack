from googletrans import Translator
from colorama import Fore, Back, Style

def text_translator():
    optionList = Fore.LIGHTYELLOW_EX+"""
    ✅✔️ Options => Select Language by Language Numer, Enter 99 to exit
    ---------
    [1]-Persian 1️⃣
    [2]-English 2️⃣
    [3]-Hebrew 3️⃣
    [4]-France 4️⃣
    [5]-Spain 5️⃣
    [6]-Arabic 6️⃣
    ---------
    [99]-exit 9️⃣9️⃣ 👋

    Written By D.Yakuza 🥷
    """
    
    translator = Translator()
    #salam =translator.translate('hello', dest='fa')
    ValidOptions = ['1', '2', '3', '4', '5', '6', '99']  # Menu options
    print(optionList)
    
    while True:
        userInput = input(Fore.LIGHTCYAN_EX+'Select Your Destination Language using Language Number: ')
        if userInput == '99':
            print(Fore.LIGHTRED_EX+'GoodBye!!! 👋👋👋 Exiting...')
            exit()
        elif userInput not in ValidOptions:
            print(Fore.LIGHTRED_EX+'🔴 Invalid Option 🔴 , Try Again!')
            continue
        
        inputText = input(Fore.LIGHTGREEN_EX+'Enter Phrase to be translate: ')
        if userInput == '1':
            print(Fore.LIGHTWHITE_EX+'Text translated to Persian => \n')
            translated = translator.translate(inputText, dest='fa')
            print(translated.text)
        elif userInput == '2':
            print(Fore.LIGHTWHITE_EX+'Text translated to English => \n')
            translated = translator.translate(inputText, dest='en')
            print(translated.text)
        elif userInput == '3':
            print(Fore.LIGHTWHITE_EX+'Text translated to Hebrew => \n')
            translated = translator.translate(inputText, dest='iw')
            print(translated.text)
        elif userInput == '4':
            print(Fore.LIGHTWHITE_EX+'Text translated to French => \n')
            translated = translator.translate(inputText, dest='fr')
            print(Fore.LIGHTWHITE_EX+translated.text)
        elif userInput == '5':
            print(Fore.LIGHTWHITE_EX+'Text translated to Spanish => \n')
            translated = translator.translate(inputText, dest='es')
            print(translated.text)
        elif userInput == '6':
            print(Fore.LIGHTWHITE_EX+'Text translated to Arabic => \n')
            translated = translator.translate(inputText, dest='ar')
            print(translated.text)
        else:
            print('Unexcepted Error')

#Test Function text_translator()
text_translator()

#TODO
# Add Source Language select
# Add Auto Language Detection
# Add more languages to the menu
