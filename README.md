# Python Security Tools

A collection of Python security tools built whilst 
learning ethical hacking and penetration testing 
as part of my cybersecurity studies.

--- 

## Tool 1 - Port Scanner

A threaded TCP port scanner built from scratch in Python.

**How to run:**
python3 portscanner.py

**Version History:**

Version 1 - Basic Sequential Scanner
Scanned ports one at a time. Functional but slow, 
scanning 1024 ports with a 0.5 second timeout took 
several minutes due to single threaded execution.

Version 2 - Threaded Scanner
Implemented concurrent.futures ThreadPoolExecutor 
with 100 workers to scan ports simultaneously.
Reduced scan time from several minutes to under 
30 seconds on the same target.

**Behaviour Notes:**
- If no open ports found the tool prints "Scan complete"
- Ctrl+C exits with "Scan interrupted by user"
- High thread counts on virtual networks can cause 
  missed results
- Detects open ports only, not filtered ports

**Known Limitations:**
- No service name detection
- Single target scanning only
- No file output, shows in terminal display only

---

## Tool 2 - Subdomain Enumerator

A threaded subdomain enumeration tool that discovers 
active subdomains using DNS lookups against a 
customisable wordlist.

**How to run:**
python3 subdomain-enumerator.py

**Version History:**

Version 1 - Single hardcoded lookup
...

Version 2 - Hardcoded wordlist loop
...

Version 3 - External wordlist file
...

Version 4 - Threaded enumeration
...
