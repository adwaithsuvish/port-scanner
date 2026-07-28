import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("Enter the IP address or domain name: ")
if not ip[0:4].isnumeric():
    ip = socket.gethostbyname(ip)

s.settimeout(30)
f =  open (f"{ip}_ports.txt", "w")
for i in range(1,65535):
    
    try:
        s.connect((ip,i))
        
        f.write(f"Port {i} is open\n")
        

    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"Port {i} is closed")

s.close()        
f.close()
