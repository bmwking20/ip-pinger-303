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

# Login-Funktion (hinzugefügt)
def login():
    print("\033[H\033[J")  # Clear screen
    print("=== 303 IP Pinger ===")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    return username == USERNAME and password == PASSWORD

# Ping-Funktion
def ping_ip(ip, count=1, timeout=1):
    try:
        output = subprocess.check_output(
            ["ping", "-c", str(count), "-W", str(timeout), ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return "1 received" in output
    except subprocess.CalledProcessError:
        return False

# Dauerping mit Logging
def continuous_ping(ip, interval=2, max_pings=None):
    print(f"\n[303] Starte Dauerping für {ip} (Intervall: {interval}s). Drücke STRG+C zum Stoppen.")
    try:
        count = 0
        while True:
            count += 1
            status = "🟢 ONLINE" if ping_ip(ip) else "🔴 OFFLINE"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] {status} – Ping #{count} zu {ip}")
            if max_pings and count >= max_pings:
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[303] Ping gestoppt.")

# IP-Bereich scannen
def scan_ip_range(base_ip, start, end):
    print(f"\n[303] Scanne IP-Bereich {base_ip}.{start}-{end}...")
    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        if ping_ip(ip, timeout=0.5):
            print(f"[303] {ip} ist \033[32monline\033[0m!")
        else:
            print(f"[303] {ip} ist \033[31moffline\033[0m")

# Hauptprogramm
def main():
    if not login():  # Jetzt korrekt definiert
        print("Falsche Anmeldedaten!")
        sys.exit(1)

    print_303_animation()
    print("\033[H\033[J")
    print("=== 303 IP Pinger (Dauer-Modus) ===")
    print("Wähle eine Option:")
    print("1: Einzelner Dauerping")
    print("2: IP-Bereich scannen")
    print("3: Einmaliger Ping")
    choice = input("> ")

    if choice == "1":
        ip = input("IP-Adresse: ")
        continuous_ping(ip)
    elif choice == "2":
        base_ip = input("Basis-IP (z.B. 192.168.1): ")
        start = int(input("Start-IP (letzte Zahl): "))
        end = int(input("End-IP (letzte Zahl): "))
        scan_ip_range(base_ip, start, end)
    elif choice == "3":
        ip = input("IP-Adresse: ")
        print(f"\nPinge {ip}...")
        print(f"[303] {ip} ist {'\033[32monline\033[0m' if ping_ip(ip) else '\033[31moffline\033[0m'}")
    else:
        print("Ungültige Option!")

if __name__ == "__main__":
    main()