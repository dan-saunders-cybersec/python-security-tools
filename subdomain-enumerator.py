import socket
import concurrent.futures

domain = input("Enter target domain: ")
wordlist_file = input("Enter wordlist path: ")

with open(wordlist_file, "r") as f:
    subdomains = f.read().splitlines()

print(f"Enumerating subdomains for {domain}")

def check_subdomain(subdomain):
    try:
        result = socket.gethostbyname(f"{subdomain}.{domain}")
        print(f"Found: {subdomain}.{domain} - {result}")
    except socket.gaierror:
        pass

try: 
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_subdomain, subdomains)

except KeyboardInterrupt:
    print("\nScan interrupted by user")

print("Enumeration Complete")
