import socket

def hostIp_hostIP(url):
                # One Line url Schema Remover
    url = url[8:] if url.startswith('https://') else url[7:] if url.startswith('http://') else url

                # Onle Line url Schema Adder
    #url2 = f'https://{url2}' if not url2.startswith('https://') else url2
    
    try:
        hostIp = socket.gethostbyname(url)
        hostName = socket.gethostname()
        result = {'isExist':True,'HostName':hostName,'hostIp':hostIp} if hostIp else {'isExist':False,'HostName':hostName,'hostIp':hostIp}
        print(f'Send Request from {hostName} to {url} => {hostIp} is {result["isExist"]} \n')
        return result
    except socket.getaddrinfo:
        print('Host Not Found')
        return False
    except socket.gaierror:
        print('Enter host name correctly, Host Not Found')
        return False
    except Exception as e:
        print(f'Unhandled Error: {e}')
        return False

def main():
    url = input('Input url(Host) to Obtain IP: ')
    print(hostIp_hostIP(url))

if __name__ == '__main__':
    main()