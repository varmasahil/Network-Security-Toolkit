import hashlib

print("="*50)
print("Network Security Toolkit - Hash Cracker")
print("="*50)

hash_input = input("Enter hash: ").strip()
hash_type = input("Enter hash type (md5/sha1/sha256): ").strip().lower()

# Supported hash types
supported_hashes = ["md5", "sha1", "sha256"]

if hash_type not in supported_hashes:
    print("[-] Invalid hash type. Please choose from: md5, sha1, sha256")
    exit()

try:
    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print("[-] passwords.txt file not found in current directory")
    exit()

print(f"\n[*] Cracking hash: {hash_input}")
print(f"[*] Using hash type: {hash_type}")
print(f"[*] Wordlist contains {len(passwords)} passwords\n")

found = False

for pwd in passwords:
    pwd = pwd.strip()
    
    if hash_type == "md5":
        calculated_hash = hashlib.md5(pwd.encode()).hexdigest()
    elif hash_type == "sha1":
        calculated_hash = hashlib.sha1(pwd.encode()).hexdigest()
    elif hash_type == "sha256":
        calculated_hash = hashlib.sha256(pwd.encode()).hexdigest()
    
    if calculated_hash == hash_input:
        print(f"[+] Password found: {pwd}")
        found = True
        break

print("="*50)
if found:
    print("[+] CRACK COMPLETE")
else:
    print("[-] Password not found in wordlist")
print("="*50)