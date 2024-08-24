import requests
import subprocess
import os
from colorama import Fore, Back, Style




def audio_download(url):

    print(Fore.YELLOW+'Start Downloading Audio...'+Fore.RESET)

    try:
        audioDL = requests.get(rf"{audioUrl}").content
        print(Fore.LIGHTGREEN_EX+'Audio Downloaded Succesfully \n'+Fore.RESET)
        
        with open(r"./hiphop.mp3","wb") as f:
            f.write(audioDL)
            print(Fore.LIGHTYELLOW_EX+f'Audio Saved to: {os.getcwd()}\\hiphop.mp3 \n'+Fore.RESET)
        
    except Exception as e:
        print(Fore.RED+"Downloaded Failed \n"+Fore.RESET)
        print(Fore.WHITE+f'{e} \n'+Fore.RESET)

    
    subprocess.Popen(["start",r'./hiphop.mp3'],shell=True)
    
audioUrl = input(Back.YELLOW+Fore.BLACK+"Enter MP3 Audio URL: "+Style.RESET_ALL)
audio_download(audioUrl)