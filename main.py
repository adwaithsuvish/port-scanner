import socket
from concurrent.futures import ThreadPoolExecutor




def ports_checker_TCP(port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
        
    try:
        s.connect((ip,port))
        output.append(f"Port {port} is open(TCP)\n")

    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"Port {port} is closed(TCP)")

    finally:
        s.close()

def ports_checker_UDP(port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
        
    try:
        s.connect((ip,port))
        s.send(b'')
        data,addr = s.recvfrom(1024)
        output.append(f"Port {port} is open(UDP)\n")

    except socket.timeout:
        print(f"Port {port} no response(UDP)\n")

    except ConnectionResetError:
         print(f"Port {port}: closed(UDP)\n")

    finally:
        s.close()

choice = input("Enter protocol (TCP/UDP OR BOTH)")
ip = input("Enter the IP address or domain name: ")
if not ip[0:4].isnumeric():
    ip = socket.gethostbyname(ip)
f =  open (f"{ip}_ports.txt", "w")
output = []


if choice.upper() == "TCP":
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(ports_checker_TCP, range(1, 65536))

elif choice.upper() == "UDP":
    with ThreadPoolExecutor(max_workers=200) as executor:
            executor.map(ports_checker_UDP, range(1, 65536))

elif choice.upper() == "BOTH":
    with ThreadPoolExecutor(max_workers=200) as executor:
            executor.map(ports_checker_TCP, range(1, 65536))
    with ThreadPoolExecutor(max_workers=200) as executor:
                executor.map(ports_checker_UDP, range(1, 65536))

else:
     print("Incorrect Choice")
    



f.writelines(output)
f.close()
