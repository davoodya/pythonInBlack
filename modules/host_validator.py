import socket
import validators

def get_host_ip(url):
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

def host_validator(url):
    status = validators.url(url)
    result = f"Schema OK" if status else f'Schema ERROR'
    return result





def main():

    url = input('Input url(Host) to Obtain IP: ')
    print(f'Host IP: {get_host_ip(url)}')
    print(host_validator(url))

    
if __name__ == '__main__':
    print('app start')
    main()