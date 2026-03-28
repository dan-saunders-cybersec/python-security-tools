import socket
import concurrent.futures

target = input("Enter IP address to scan: ")
print(f"Scanning {target}...")

def scan_port(port):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        print(f"Port {port} is OPEN")

try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(1, 8001))

except KeyboardInterrupt:
    print("\nScan interrupted by user")

print("Scan complete")
