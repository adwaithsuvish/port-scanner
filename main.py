import socket
from concurrent.futures import ThreadPoolExecutor


ip = input("Enter the IP address or domain name: ")
if not ip[0:4].isnumeric():
    ip = socket.gethostbyname(ip)
f =  open (f"{ip}_ports.txt", "w")

output = []

def ports_checker(port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(20)
        
    try:
        s.connect((ip,port))
        output.append(f"Port {port} is open\n")

    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"Port {port} is closed")

    finally:
        s.close()

with ThreadPoolExecutor(max_workers=500) as executor:
    executor.map(ports_checker, range(1, 65536))

f.writelines(output)
f.close()
