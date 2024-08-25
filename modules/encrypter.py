from cryptography.fernet import Fernet
import subprocess


def text_encryptor():
    text = input('Enter your text: ')

    key = Fernet.generate_key()

    encryptData = Fernet(key).encrypt(text.encode())

    with open("key_data.txt","w") as f:
        f.write('Key: \n')
        f.write(f'{key.decode()}\n')
        f.write('Data Content: \n')
        f.write(f'{encryptData.decode()}\n')

    subprocess.Popen("notepad .\\key_data.txt", shell=True)

    print(f'Your Key Is: {key.decode()} \n')
    print(f'Encrypted Data Is: {encryptData.decode()} \n')

    keyData = []
    with open("key_data.txt","r") as f:
        for line in f:
            keyData.append(line.strip())
            
    #keyUsed = b'SeExLvFTMx0Cxq5caUq1XSbpUYTB06kjb07y8NwIZp4='
    #encData = b'gAAAAABmy5AMSPIeyohe_uFlBqphCLMOjFt_eQSTZMCTUcixuey5WSGoIYXE5ECxM1wOTpz51RjDph6Fh7LAkIr3hLUahKSxSw=='
    
    decryptor = Fernet(keyData[1]).decrypt(keyData[3])

    print(f'Decrypted Data Is: {decryptor.decode()} \n')

def file_encryptor():
    path = input('[+] File Encryptor => Enter file path to be Encrypted: ')
    with open(rf'{path}','rb') as f:
        dataFile = f.read()
    
    key = Fernet.generate_key()
    
    encryptData = Fernet(key).encrypt(dataFile)
    print(f'[+] File Encryptor => File Encrypted & Encryption Key Is: {key.decode()} \n')
    
    #Write key to file
    with open("key_data.txt","w") as f:
        f.write('Key: \n')
        f.write(f'{key.decode()}\n')
        f.write('Data Content: \n')
        f.write(f'{encryptData.decode()}\n')
    
    subprocess.Popen("notepad .\\key_data.txt", shell=True)
        
    #Write Encrypted Data to file
    with open(rf'{path}','wb') as encryptFile:
        encryptFile.write(encryptData)
    
def file_decryptor():
    path = input('[+] File Decryptor => Enter file path to be Decrypted: ')
    fileExt = path.split('.')[1]
    
    keyData = []
    with open("key_data.txt","r") as f:
        for line in f:
            keyData.append(line.strip())
        
    decryptor = Fernet(keyData[1]).decrypt(keyData[3])
    print(f'[+] File Decryptor => File Decrypted & Decryption Key Is: \n{keyData[1]} \n')
    
    with open(rf'{path}_decrypted.{fileExt}','wb') as decryptFile:
        decryptFile.write(decryptor)
    #decryptor()

    # with open(rf'{path}','wb') as f:
    #     f.write(encryptData)

def main():
    #text_encryptor()
    file_encryptor()
    file_decryptor()
    
if __name__ == "__main__":
        main()