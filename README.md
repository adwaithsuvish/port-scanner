# 🔍 Python Port Scanner
 
> A simple TCP port scanner built using Python's `socket` module — checks which ports are open on a given IP address or domain.
 
---
 
## 📖 About
 
This program scans a target IP address (or domain name) across all TCP ports (1–65534) and reports which ones are **open**, writing the results to a text file. Ports that are closed or unreachable are printed to the console.
 
If you enter a domain name instead of an IP address, the program automatically resolves it to an IP using `socket.gethostbyname()`.
 
---
 
## ✨ Features
 
- 🌐 Accepts either an IP address or a domain name as input
- 📝 Accepts the choice of UDP, TCP or both
- 🔁 Scans all TCP ports from 1 to 65534
- 📄 Saves the list of open ports to a text file named `<ip>_ports.txt`
- 🐍 Pure Python — uses only the built-in `socket` module
---
 
## 🚀 Getting Started
 
```bash
# Clone the repo
git clone https://github.com/adwaithsuvish/port-scanner.git
cd port-scanner
 
# Run it
python main.py
```
 
You'll be prompted to enter an IP address or domain name, and the scan will begin.
 
---
 
## 💡 Example
 
```
Enter the IP address or domain name: localhost
Port 21 is closed
Port 22 is closed
Port 80 is closed
...
```
 
Open ports found during the scan are saved to a file like `127.0.0.1_ports.txt` in the same folder.
 
---
 
## ⚠️ Known Limitations
 
- **CLI ARGUMENTS**: there is no support for command line arguments yet.

---
 
## 🧩 Planned Improvements
 
- [ ] Add command-line arguments (e.g. specify port range) instead of scanning the full range every time
---
 
## 🛠️ Built With
 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
 
---
 
## 📌 Why I Built This
 
Port scanning is one of the most fundamental techniques in network security — understanding which ports are open on a system is often the first step in both offensive (penetration testing) and defensive (hardening a system) security work. Building a basic scanner from scratch helped me understand how TCP connections succeed or fail at a low level, using nothing but Python's built-in `socket` module.
 
---
 
## 📄 License
 
No license specified yet.
 