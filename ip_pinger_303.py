
---

### **🐍 `ip_pinger_303.py` (Hauptscript)**  
```python
#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# Login-Daten
USERNAME = "bmwking20"
PASSWORD = "weed"

# 303-Logo-Animation
def print_303_animation():
    frames = [
        """
          _____   _____   _____ 
         |___ /  |___ /  |___ / 
           |_ \\    |_ \\    |_ \\ 
          |___/  |___/  |___/ 
        """,
        """
          _____   _____   _____ 
         |___ /  |___ /  |___ / 
           |_ \\    |_ \\    |_ \\ 
          |___/  |___/  |___/ 
        """,
        """
          _____   _____   _____ 
         |___ /  |___ /  |___ / 
           |_ \\    |_ \\    |_ \\ 
          |___/  |___/  |___/ 
        """
    ]
    for _ in range(3):
        for frame in frames:
            print("\033[H\033[J")  # Clear screen
            print(frame)
            time.sleep(0.3)

# Login-Abfrage
def login():
    print("\033[H\033[J")  # Clear screen
    print("=== 303 IP Pinger ===")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    return username == USERNAME and password == PASSWORD

# Ping-Funktion
def ping_ip(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return "1 packets transmitted, 1 received" in output
    except subprocess.CalledProcessError:
        return False

# Hauptprogramm
def main():
    if not login():
        print("Falsche Anmeldedaten!")
        sys.exit(1)

    print_303_animation()
    print("\033[H\033[J")  # Clear screen
    print("=== 303 IP Pinger ===")
    
    while True:
        ip = input("Gib die IP-Adresse ein (oder 'exit' zum Beenden): ")
        if ip.lower() == 'exit':
            break
        
        print(f"\nPinge {ip}...")
        if ping_ip(ip):
            print(f"[303] {ip} ist \033[32monline\033[0m!")
        else:
            print(f"[303] {ip} ist \033[31moffline\033[0m!")

if __name__ == "__main__":
    main()