import socket

print("="*40)
print("Network Security Toolkit - Port Scanner")
print("="*40)

target_host = input("Enter target (IP or domain): ")
target_port = input("Enter port range (e.g., 1-1024): ")

if "-" in target_port:
    start_port, end_port = map(int, target_port.split("-"))
else:
    start_port = int(target_port)
    end_port = int(target_port)

print(f"Scanning from port {start_port} to {end_port}\n")

open_port = []

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_host, port))
    if result == 0:
        open_port.append(port)
        print(f"[+] Port {port} is OPEN")
    s.close()



print("\n" + "="*40)
if open_port:
    print(f"[+] SCAN COMPLETE. Open ports found: {len(open_port)}")
    print(f"[+] Open ports: {open_port}")
else:
    print("[-] No open ports found in given range")
print("="*40)
