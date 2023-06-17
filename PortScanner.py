from socket import *

def Scan(Host, Port):
    try:
        socket = socket(AF_INET, SOCK_STREAM)
        socket.connect((Host, Port))
        print('[+] %d/tcp open' % Port)
        socket.close()
    except:
        print('[-] %d/tcp closed' % Port)

def portScan(Host, Ports):
    try:
        ip = gethostbyname(Host)
    except:
        print('[-] Cannot resolve %s ' % Host)
        return
    try:
        TargetName = gethostbyaddr(ip)
        print('\n[+] Scan result of: %s' % TargetName[0])
    except:
        print('\n[+] Scan result of: %s' % ip)
    setdefaulttimeout(1)
    for Port in Ports:
        print('Scanning Port: %d' % Port)
        Scan(Host, int(Port))
if __name__ == '__main__':
    Host = input("Enter the host website to scan:")
    for i in range(1023):
     portScan(Host,[i])
