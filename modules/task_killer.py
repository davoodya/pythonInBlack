import psutil
from colorama import Fore, Back, Style
import os, platform, subprocess 

#os.system('cls')

#print(os.system('dir'))
#print(subprocess.getoutput('dir'))

#print(platform.uname()[0])  # platform.uname()[0] == OS-NAME => 'Windows'

#for proc in psutil.process_iter(['pid', 'name', 'status']):
    #print(f'PID: {proc.info['pid']} | Name: {proc.info['name']} | Status: {proc.info['status']}')
    
''' Summary - kill_proc()
0. get proc list => for proc in psutil.process_iter(['pid', 'name', 'status']):
1. check input process exist in proc list => if proc.name() == procName:
2. if process exist print pid, proc name, is running status
3. kill process if exist => proc.terminate() || proc.kill()
'''
def kill_proc(procName):
    for proc in psutil.process_iter():
        if proc.name().lower() == f'{procName}.exe'.lower():
            print(f'{proc.pid}: {proc.name()} => {proc.is_running()}')
            try:
                proc.terminate() #pname = psutil.Process(proc.pid)
            except:
                proc.kill()
            else:
                print(f'{proc.name()} Killed!') # proc.name() == psutil.Process(proc.id)
                return True
        
            if proc.is_running() == True:
                print('Error, Cant kill task')
                return False
    else:
        print(f'{procName} is Not Running')
''' Summary - kill_os_proc()
0. get OS name => osName = platform.uname()[0]
1. check OS name => to run compatible command base on OS
2. get list all process => subprocess.getoutput('tasklist') | subprocess.run(['tasklist'])
3. check process exist => if taskName in taskList
4. if exist, Kill process => res = subprocess.run(['taskkill', '/F', '/IM', taskName], getoutput=True, text=True)
# Note: using getoutput=True to check command running status using res.returncode == 0[OK] 1[ERROR]
'''
def kill_os_proc(taskName):
    os.system('cls')
    osName = platform.uname()[0]
    if osName.lower() == 'windows':
        print(Fore.LIGHTCYAN_EX+'You Are in Windows'+Style.RESET_ALL)        
        taskList = subprocess.getoutput('tasklist') #os.system('tasklist') # print automatically without need print()
        if taskName.lower() in taskList.lower():
            print(f'{taskName}.exe is running, now we kill it for you')
            taskName = f'{taskName}.exe'
                #subprocess.getoutput(f'taskkill /F /IM {taskList}')
            result = subprocess.run(['taskkill', '/F', '/IM', taskName],\
                capture_output=True, text=True)
            if result.returncode == 0:
                print(Fore.GREEN+f'{taskName} Killed succefully')
                return True
            else:
                result2 = subprocess.run(['taskkill', '/F', '/IM', taskName.capitalize()],\
                    capture_output=True, text=True)
                if result2.returncode == 0:
                    print(f'{Fore.GREEN}{taskName} Killed succefully')
                    return True
                else:
                    print(f'{Fore.RED}Failed to kill {taskName},{Fore.WHITE} Write {taskName} Correctly')
                    return False
        else:
            print(f'{taskName}.exe is not running')
            
    if osName.lower() == 'linux':
        print(Fore.LIGHTCYAN_EX+'You Are in Linux'+Style.RESET_ALL)
        taskList = subprocess.getoutput('ps -ef') #os.system('ps -ef') # print automatically without need print()
        if taskName.lower() in taskList.lower():
            print(f'{taskName} is running, now we kill it for you')
            taskName = f'{taskName}'
            #subprocess.getoutput(f'taskkill /F /IM {taskList}')
            result = subprocess.run(['killall', taskName],\
                capture_output=True, text=True)
            if result.returncode == 0:
                print({Fore.GREEN}+f'{taskName} Killed succefully')
                return True
            else:
                result2 = subprocess.run(['kill', taskName.capitalize()],\
                    capture_output=True, text=True)
                if result2.returncode == 0:
                    print(f'{Fore.GREEN}{taskName} Killed succefully')
                else:
                    print(f'{Fore.RED}Failed to kill {taskName},{Fore.WHITE} Write {taskName} Correctly')
        else:
            print(f'{taskName} is not running')

    if osName.lower() == 'darwin':
        print(Fore.LIGHTCYAN_EX+'You Are in Mac'+Style.RESET_ALL)
        taskList = subprocess.getoutput('ps -a')
        if taskName.lower() in taskList.lower():
            print('taskName is running, now we kill it for you')
            result = subprocess.run(['killall','-9', taskName], capture_output=True, text=True)
            if result.returncode == 0:
                print({Fore.GREEN}+f'{taskName} Killed succefully')
                return True
            else:
                result2 = subprocess.run(['killall','-9', taskName.capitalize()], capture_output=True, text=True)
                if result2.returncode == 0:
                    print(f'{Fore.GREEN}{taskName} Killed succefully')
                else:
                    print(f'{Fore.RED}Failed to kill {taskName},{Fore.WHITE} Write {taskName} Correctly')
        else:
            print(f'{taskName} is not running')
                
def run_killer():
    try:
        while True: 
            print(Back.MAGENTA+Fore.WHITE+'Task Killer'+Style.RESET_ALL)
            taskName = input(f'{Fore.LIGHTYELLOW_EX}Enter Task Name: ')
            print(f'{Back.MAGENTA+Fore.WHITE} Enter 1 for Normal Kill, Enter 2 for OS Base Kill, Enter 99 to exit{Style.RESET_ALL}')
            option = int(input(f'{Fore.LIGHTYELLOW_EX}Select Option: {Style.RESET_ALL}'))
            if option == 99:
                print(f'\n {Back.MAGENTA+Fore.WHITE} Keyboard Interrupt, Goodbye & Goodluck 👋 !!!{Style.RESET_ALL}')
                exit()
            elif option == 1:
                kill_proc(taskName)
            elif option == 2:
                kill_os_proc(taskName)
            else:
                print('Wrong Option !!! try again')
                continue
    except KeyboardInterrupt:
        print(f'\n {Back.MAGENTA+Fore.WHITE} Keyboard Interrupt, Goodbye & Goodluck 👋 !!!{Style.RESET_ALL}')
        exit()
    except Exception as e:
        print(f'\n {Fore.RED} Error: {e}')

def main():
    run_killer()
    
if __name__ == '__main__':
    main()
