import subprocess  
import webbrowser  
import threading  
import time  

class Exposer:  
    def __init__(self):  
        pass  

    def start_local_server(self):  
        # Start the local server on port 9980  
        self.local_server_process = subprocess.Popen(['python', '-m', 'http.server', '9980'])  

    def start_ngrok_tunnel(self):  
        # Start the ngrok tunnel  
        self.ngrok_process = subprocess.Popen(['ngrok', 'http', '9980'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  

        # Get the public URL for the tunnel  
        while True:  
            output = self.ngrok_process.stdout.readline()  
            if output == b'' and self.ngrok_process.poll() is not None:  
                break  
            if output:  
                line = output.decode('utf-8').strip()  
                if 'Forwarding' in line:  
                    self.public_url = line.split('Forwarding')[1].strip().split(' ')[0]  
                    print(f"Your public URL is: {self.public_url}")  
                    webbrowser.open(self.public_url)  
                    break  

    def run(self):  
        # Start the local server in the main thread  
        self.start_local_server()  

        # Start the ngrok tunnel in a separate thread  
        ngrok_thread = threading.Thread(target=self.start_ngrok_tunnel)  
        ngrok_thread.start()  

        try:  
            # Wait for the local server to be terminated  
            self.local_server_process.wait()  
        except KeyboardInterrupt:  
            # Terminate the ngrok process and the local server  
            self.ngrok_process.terminate()  
            self.local_server_process.terminate()  
            print("Shutting down...")  

def main():  
    exposer = Exposer()  
    exposer.run()  

if __name__ == '__main__':  
    print('app start')  
    main()