# Base64_decode_Salt
Decode BASE64 salted with AES, OpenSSL, PBKDF2, ...

Use Case: you find a hash which looks like base64 but hashid identifies it as UNKNOWN. 
- AES: 
Normal "base64 -d" results in unreadable content. the hash is salted via AES-128, AES-192 or AES-256. normally salted key is embeded in the hash, what this tool do is to check for any of these three salt method inside the hash and tries to find the key in every possible offset.


<code>hashid '57iOQI4Vf9tHC2sA/mlPRQSOdFcys/tdkoxQtA+0L30xkxtZtqu+rrx7e26lihWb5sb4tuGZlGaMuGl61fPYwtQA3iKYRV+/CyAWX0yxkK8HAgwlRQEZ4Am9lQ=='
Analyzing '57iOQI4Vf9tHC2sA/mlPRQSOdFcys/tdkoxQtA+0L30xkxtZtqu+rrx7e26lihWb5sb4tuGZlGaMuGl61fPYwtQA3iKYRV+/CyAWX0yxkK8HAgwlRQEZ4Am9lQ=='
[+] Unknown hash</code>

<code>python decode_base64_AES.py 
Starting brute-force search for AES keys at all offsets...

Trying AES-128 keys...
[*] Checking Offset: 0, Key Size: 16 bytes, Key: e7b88e408e157fdb470b6b00fe694f45
[*] Checking Offset: 1, Key Size: 16 bytes, Key: b88e408e157fdb470b6b00fe694f4504
...

Trying AES-192 keys...
[*] Checking Offset: 0, Key Size: 24 bytes, Key: e7b88e408e157fdb470b6b00fe694f45048e745732b3fb5d
[*] Checking Offset: 1, Key Size: 24 bytes, Key: b88e408e157fdb470b6b00fe694f45048e745732b3fb5d92
...

Trying AES-256 keys...
[*] Checking Offset: 0, Key Size: 32 bytes, Key: e7b88e408e157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d
[*] Checking Offset: 1, Key Size: 32 bytes, Key: b88e408e157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31
[*] Checking Offset: 2, Key Size: 32 bytes, Key: 8e408e157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d3193
[*] Checking Offset: 3, Key Size: 32 bytes, Key: 408e157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b
[*] Checking Offset: 4, Key Size: 32 bytes, Key: 8e157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59
[*] Checking Offset: 5, Key Size: 32 bytes, Key: 157fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6
[*] Checking Offset: 6, Key Size: 32 bytes, Key: 7fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6ab
[*] Checking Offset: 7, Key Size: 32 bytes, Key: db470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbe
[*] Checking Offset: 8, Key Size: 32 bytes, Key: 470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeae
[*] Checking Offset: 9, Key Size: 32 bytes, Key: 0b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc
[*] Checking Offset: 10, Key Size: 32 bytes, Key: 6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b
[*] Checking Offset: 11, Key Size: 32 bytes, Key: 00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b

[+] Decryption succeeded!
Key (Hex): 00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b
Offset: 11, Key Size: 32 bytes
Decrypted Output: b'This is a test message'

[+] Success with offset 11, key size 32 bytes.</code>

- Installation:
  required libraries:<br>
  <code> pip install pycryptodome </code>

