import socket

domain_input=input("Enter domain (e.g., google.com):")

with open("wordlist.txt","r") as file:
    subdomain=file.read().splitlines()
    active_subdomain=[]
    for sub in subdomain:
        fulldomain=sub+"."+domain_input
        domain=fulldomain
        try:
            ip=socket.gethostbyname(domain)
            active_subdomain.append(sub)
            print(f"[+] {fulldomain} is active")
        except socket.error as err:
            pass

print(f"\n[+] SCAN COMPLETE. Active subdomains found: {len(active_subdomain)}")
print(f"[+] Active subdomains: {active_subdomain}")
                

