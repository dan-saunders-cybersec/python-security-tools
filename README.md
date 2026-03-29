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
Tested core DNS lookup concept against 
one hardcoded subdomain.

Version 2 - Hardcoded wordlist loop
Looped through a hardcoded list of common 
subdomains printing any that resolved successfully.

Version 3 - External wordlist file
Replaced hardcoded list with file input allowing 
any wordlist to be used. Added FileNotFoundError 
handling for invalid paths.

Version 4 - Threaded enumeration
Added concurrent.futures ThreadPoolExecutor with 
50 workers. Results return in response order rather 
than wordlist order confirming simultaneous execution.
Notable speed improvement over sequential version.
...

## Tool 3 - PowerShell Base64 Decoder

A forensic tool for decoding obfuscated PowerShell 
commands commonly found in malware analysis and 
incident response investigations.

Built to replicate the CyberChef From Base64 and 
UTF-16LE decode process in a portable Python script. 
Reads encoded strings from a text file, decodes them 
and automatically saves the output for documentation.

**How to run:**
python3 powershell-decoder.py

**How to use:**
1. Save the encoded string to a .txt file
2. Run the script and enter the filename when prompted
3. Decoded output prints to terminal and saves 
   automatically to decoded_output.txt

**Real world application:**
Used during a supply chain compromise investigation 
to decode a malicious PowerShell dropper discovered 
in Splunk logs. See soc-investigations repository 
for full write up
