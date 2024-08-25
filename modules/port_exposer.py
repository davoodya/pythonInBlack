import subprocess
import pyngrok
import subprocess  
import webbrowser
from pyngrok import ngrok

#TODO
''' TODO
0. Using ngrok library to established tunnel => Read More => https://dashboard.ngrok.com/get-started/setup/python
0. add AUTH TOKEN to ENV Variable
1. Add Enter Directory Path feature
2. Beaurify Script & Add Banner
3. Check ngrok is Install or Not? if not install it
4. Write out link in txt file
5. Stop Tunnel Feature
'''



ngrokToken = "2kfTOaJZSihzUzxdJutK5Ot1tuv_vfgyNGVmzTMYvm2FdPwB"
class Exposer():
    def __init__(self):
        pass
    def expose_cmd(self, port):
        # Start the local server on port 8099  
        subprocess.Popen(['python', '-m', 'http.server', str(port)])  

        # Start the ngrok tunnel  
        ngrok_process = subprocess.Popen(['ngrok', 'http', str(port)])  

        # Get the public URL for the tunnel  
        public_url = subprocess.check_output(['ngrok', 'http', str(port)]).decode('utf-8').split('\n')[2].split(': ')[1]  

        # Print the public URL and open it in the default web browser  
        print(f"Your public URL is: {public_url}")  
        webbrowser.open(public_url)  
        
        try:  
            ngrok_process.wait()  
        except KeyboardInterrupt:  
            ngrok_process.terminate()  
            print("Shutting down...")

    def expose_pyNgrok(self, port):
        # Start the local server on port 8099  
        subprocess.Popen(['python', '-m', 'http.server', str(port)])  

        # Start the ngrok tunnel  
        public_url = ngrok.connect(str(port), "http")  

        # Print the public URL and open it in the default web browser  
        print(f"Your public URL is: {public_url}")  
        #webbrowser.open(public_url)  

        # Keep the script running until the user terminates it  
        try:  
            ngrok.get_tunnels(public_url).wait()  
        except KeyboardInterrupt:  
            ngrok.kill()  
            print("Shutting down...")

    def stop_ngrok_tunnel(self):  
        if self.ngrok_process:  
            self.ngrok_process.terminate()  
            self.ngrok_process.wait() 
def main():
    port = input("Enter port: ")
    exposer = Exposer()
    exposer.expose_cmd(str(port))
    #exposer.expose_pyNgrok('9983')
    
if __name__ == '__main__':
    print('app start')
    main()

