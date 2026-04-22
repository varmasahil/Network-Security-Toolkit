# Network Security Toolkit

Python-based cybersecurity tools built from scratch.

## 📁 Tools Included

| Tool | Description |
|------|-------------|
| Port Scanner | TCP port scanner (1-1024) using socket library |
| Subdomain Finder | DNS enumeration using wordlist |
| Hash Cracker | Dictionary attack on MD5, SHA1, SHA256 hashes |

---

## 🛠️ Port Scanner

**File:** `port_scanner.py`

**Usage:**
```bash
python port_scanner.py
```

Enter target (IP or domain): scanme.nmap.org
Enter port range (e.g., 1-1024): 1-1024

[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN

==================================================
[+] SCAN COMPLETE. Open ports found: 3
[+] Open ports: [22, 80, 443]
==================================================

## 🛠️ Subdomain Finder

**File:** `subdomain_finder.py`  
**Wordlist:** `wordlist.txt`

**Description:**
DNS enumeration tool that discovers active subdomains using a wordlist.

**Features:**
- Reads subdomains from `wordlist.txt`
- Resolves each subdomain using DNS lookup
- Displays only active subdomains
- Shows total count at the end

**Usage:**
```bash
python subdomain_finder.py
```

Enter domain (e.g., google.com): google.com

[+] www.google.com is active
[+] mail.google.com is active
[+] admin.google.com is active

[+] SCAN COMPLETE. Active subdomains found: 3
[+] Active subdomains: ['www', 'mail', 'admin']


## 🛠️ Hash Cracker

**File:** `hash_cracker.py`  
**Wordlist:** `passwords.txt`

**Description:**
Dictionary attack tool that cracks MD5, SHA1, and SHA256 hashes using a wordlist.

**Features:**
- Supports MD5, SHA1, SHA256 hash types
- Case-insensitive hash type input
- File existence validation
- Clean, professional output format

**Usage:**
```bash
python hash_cracker.py
```

==================================================
Network Security Toolkit - Hash Cracker
==================================================
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
Enter hash type (md5/sha1/sha256): md5

[*] Cracking hash: 5f4dcc3b5aa765d61d8327deb882cf99
[*] Using hash type: md5
[*] Wordlist contains 10 passwords

[+] Password found: password
==================================================
[+] CRACK COMPLETE
==================================================
