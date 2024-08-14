import requests, time, getpass
from colorama import Fore, Back, Style

url = 'https://dl.sabzlearn.ir/lab/pycrack-v1/login.php'
class BruteForcer():
    def __init__(self):
        self.url = 'https://dl.sabzlearn.ir/lab/pycrack-v1/login.php'
        self.data = {'username':'admin', 'password':'admin','sub':''}
        self.result = ''
        self.response = requests.get(url, data=self.data)
    
    def send_request(self):
        response = requests.post(self.url, data=self.data)
        self.result = str(response.text)
        return response.content.decode()
    
    def print_text(self):
        print(f'POST Request: {self.result} ')
        print(f'GET Request: {self.response.status_code} ')
        
        

def main():
    bruteforce = BruteForcer()
    bruteforce.send_request()
    bruteforce.print_text()
        
if __name__ == '__main__':
    main()