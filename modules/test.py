
import subprocess  
import webbrowser  
import os

# # Start the local server on port 8099  
# subprocess.Popen(['python', '-m', 'http.server', '8999'])  

# # Start the ngrok tunnel  
# ngrok_process = subprocess.Popen(['ngrok', 'http', '8999'])  

# # Get the public URL for the tunnel  
# public_url = subprocess.check_output(['ngrok', 'http', '8999']).decode('utf-8').split('\n')[2].split(': ')[1]  

# # Print the public URL and open it in the default web browser  
# print(f"Your public URL is: {public_url}")  
# webbrowser.open(public_url)  

# # Keep the script running until the user terminates it  
# try:  
#     ngrok_process.wait()  
# except KeyboardInterrupt:  
#     ngrok_process.terminate()  
#     print("Shutting down...")

#test = subprocess.getoutput('wmic cpu get name')
#test = subprocess.Popen(['wmic','cpu','get','name'])
#os.system('wmic cpu get name')
#print(test)


res = '''[<div class="nooverflow" id="ResultData">
<h3 class="ls1 t400 h2long">Response Content</h3><pre class="brush: html; toolbar: false; wrap-lines: true;">
{"ok":true,"result":[{"update_id":679218537,
"message":{"message_id":17,"from":{"id":673330561,"is_bot":false,"first_name":"Daya","last_name":"Yahay","username":"Davoodyahay","language_code":"en"},"chat":{"id":673330561,"first_name":"Daya","last_name":"Yahay","username":"Davoodyahay","type":"private"},"date":1723755156,"text":"/none","entities":[{"offset":0,"length":5,"type":"bot_command"}]}}]}
</pre>
</div>]'''

res2 = '2long">Response Content</h3><pre class="brush: html; toolbar: false; wrap-lines: true;">'
#print(len(res))
print(res[151:-14])
print(len(res2))