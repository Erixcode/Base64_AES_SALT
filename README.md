# Base64_AES_Salt
Decode BASE64 salted with AES

Use Case: you find a hash which looks like base64 but hashid identifies it as UNKNOWN. 
Normal "base64 -d" results in unreadable content. the hash is salted via AES-128, AES-192 or AES-256. normally salted key is embeded in the hash, what this tool do is to check for any of these three salt method inside the hash and tries to find the key in every possible offset.


<code>hashid '57iOQI4Vf9tHC2sA/mlPRQSOdFcys/tdkoxQtA+0L30xkxtZtqu+rrx7e26lihWb5sb4tuGZlGaMuGl61fPYwtQA3iKYRV+/CyAWX0yxkK8HAgwlRQEZ4Am9lQ=='
Analyzing '57iOQI4Vf9tHC2sA/mlPRQSOdFcys/tdkoxQtA+0L30xkxtZtqu+rrx7e26lihWb5sb4tuGZlGaMuGl61fPYwtQA3iKYRV+/CyAWX0yxkK8HAgwlRQEZ4Am9lQ=='
[+] Unknown hash</code>

<code>python decode_base64_AES.py 
Starting brute-force search for AES keys at all offsets...

Trying AES-128 keys...
[*] Checking Offset: 0, Key Size: 16 bytes, Key: e7b88e408e157fdb470b6b00fe694f45
[*] Checking Offset: 1, Key Size: 16 bytes, Key: b88e408e157fdb470b6b00fe694f4504
[*] Checking Offset: 2, Key Size: 16 bytes, Key: 8e408e157fdb470b6b00fe694f45048e
[*] Checking Offset: 3, Key Size: 16 bytes, Key: 408e157fdb470b6b00fe694f45048e74
[*] Checking Offset: 4, Key Size: 16 bytes, Key: 8e157fdb470b6b00fe694f45048e7457
[*] Checking Offset: 5, Key Size: 16 bytes, Key: 157fdb470b6b00fe694f45048e745732
[*] Checking Offset: 6, Key Size: 16 bytes, Key: 7fdb470b6b00fe694f45048e745732b3
[*] Checking Offset: 7, Key Size: 16 bytes, Key: db470b6b00fe694f45048e745732b3fb
[*] Checking Offset: 8, Key Size: 16 bytes, Key: 470b6b00fe694f45048e745732b3fb5d
[*] Checking Offset: 9, Key Size: 16 bytes, Key: 0b6b00fe694f45048e745732b3fb5d92
[*] Checking Offset: 10, Key Size: 16 bytes, Key: 6b00fe694f45048e745732b3fb5d928c
[*] Checking Offset: 11, Key Size: 16 bytes, Key: 00fe694f45048e745732b3fb5d928c50
[*] Checking Offset: 12, Key Size: 16 bytes, Key: fe694f45048e745732b3fb5d928c50b4
[*] Checking Offset: 13, Key Size: 16 bytes, Key: 694f45048e745732b3fb5d928c50b40f
[*] Checking Offset: 14, Key Size: 16 bytes, Key: 4f45048e745732b3fb5d928c50b40fb4
[*] Checking Offset: 15, Key Size: 16 bytes, Key: 45048e745732b3fb5d928c50b40fb42f
[*] Checking Offset: 16, Key Size: 16 bytes, Key: 048e745732b3fb5d928c50b40fb42f7d
[*] Checking Offset: 17, Key Size: 16 bytes, Key: 8e745732b3fb5d928c50b40fb42f7d31
[*] Checking Offset: 18, Key Size: 16 bytes, Key: 745732b3fb5d928c50b40fb42f7d3193
[*] Checking Offset: 19, Key Size: 16 bytes, Key: 5732b3fb5d928c50b40fb42f7d31931b
[*] Checking Offset: 20, Key Size: 16 bytes, Key: 32b3fb5d928c50b40fb42f7d31931b59
[*] Checking Offset: 21, Key Size: 16 bytes, Key: b3fb5d928c50b40fb42f7d31931b59b6
[*] Checking Offset: 22, Key Size: 16 bytes, Key: fb5d928c50b40fb42f7d31931b59b6ab
[*] Checking Offset: 23, Key Size: 16 bytes, Key: 5d928c50b40fb42f7d31931b59b6abbe
[*] Checking Offset: 24, Key Size: 16 bytes, Key: 928c50b40fb42f7d31931b59b6abbeae
[*] Checking Offset: 25, Key Size: 16 bytes, Key: 8c50b40fb42f7d31931b59b6abbeaebc
[*] Checking Offset: 26, Key Size: 16 bytes, Key: 50b40fb42f7d31931b59b6abbeaebc7b
[*] Checking Offset: 27, Key Size: 16 bytes, Key: b40fb42f7d31931b59b6abbeaebc7b7b
[*] Checking Offset: 28, Key Size: 16 bytes, Key: 0fb42f7d31931b59b6abbeaebc7b7b6e
[*] Checking Offset: 29, Key Size: 16 bytes, Key: b42f7d31931b59b6abbeaebc7b7b6ea5
[*] Checking Offset: 30, Key Size: 16 bytes, Key: 2f7d31931b59b6abbeaebc7b7b6ea58a
[*] Checking Offset: 31, Key Size: 16 bytes, Key: 7d31931b59b6abbeaebc7b7b6ea58a15
[*] Checking Offset: 32, Key Size: 16 bytes, Key: 31931b59b6abbeaebc7b7b6ea58a159b
[*] Checking Offset: 33, Key Size: 16 bytes, Key: 931b59b6abbeaebc7b7b6ea58a159be6
[*] Checking Offset: 34, Key Size: 16 bytes, Key: 1b59b6abbeaebc7b7b6ea58a159be6c6
[*] Checking Offset: 35, Key Size: 16 bytes, Key: 59b6abbeaebc7b7b6ea58a159be6c6f8
[*] Checking Offset: 36, Key Size: 16 bytes, Key: b6abbeaebc7b7b6ea58a159be6c6f8b6
[*] Checking Offset: 37, Key Size: 16 bytes, Key: abbeaebc7b7b6ea58a159be6c6f8b6e1
[*] Checking Offset: 38, Key Size: 16 bytes, Key: beaebc7b7b6ea58a159be6c6f8b6e199
[*] Checking Offset: 39, Key Size: 16 bytes, Key: aebc7b7b6ea58a159be6c6f8b6e19994
[*] Checking Offset: 40, Key Size: 16 bytes, Key: bc7b7b6ea58a159be6c6f8b6e1999466
[*] Checking Offset: 41, Key Size: 16 bytes, Key: 7b7b6ea58a159be6c6f8b6e19994668c
[*] Checking Offset: 42, Key Size: 16 bytes, Key: 7b6ea58a159be6c6f8b6e19994668cb8
[*] Checking Offset: 43, Key Size: 16 bytes, Key: 6ea58a159be6c6f8b6e19994668cb869
[*] Checking Offset: 44, Key Size: 16 bytes, Key: a58a159be6c6f8b6e19994668cb8697a
[*] Checking Offset: 45, Key Size: 16 bytes, Key: 8a159be6c6f8b6e19994668cb8697ad5
[*] Checking Offset: 46, Key Size: 16 bytes, Key: 159be6c6f8b6e19994668cb8697ad5f3
[*] Checking Offset: 47, Key Size: 16 bytes, Key: 9be6c6f8b6e19994668cb8697ad5f3d8
[*] Checking Offset: 48, Key Size: 16 bytes, Key: e6c6f8b6e19994668cb8697ad5f3d8c2
[*] Checking Offset: 49, Key Size: 16 bytes, Key: c6f8b6e19994668cb8697ad5f3d8c2d4
[*] Checking Offset: 50, Key Size: 16 bytes, Key: f8b6e19994668cb8697ad5f3d8c2d400
[*] Checking Offset: 51, Key Size: 16 bytes, Key: b6e19994668cb8697ad5f3d8c2d400de
[*] Checking Offset: 52, Key Size: 16 bytes, Key: e19994668cb8697ad5f3d8c2d400de22
[*] Checking Offset: 53, Key Size: 16 bytes, Key: 9994668cb8697ad5f3d8c2d400de2298
[*] Checking Offset: 54, Key Size: 16 bytes, Key: 94668cb8697ad5f3d8c2d400de229845
[*] Checking Offset: 55, Key Size: 16 bytes, Key: 668cb8697ad5f3d8c2d400de2298455f
[*] Checking Offset: 56, Key Size: 16 bytes, Key: 8cb8697ad5f3d8c2d400de2298455fbf
[*] Checking Offset: 57, Key Size: 16 bytes, Key: b8697ad5f3d8c2d400de2298455fbf0b
[*] Checking Offset: 58, Key Size: 16 bytes, Key: 697ad5f3d8c2d400de2298455fbf0b20

Trying AES-192 keys...
[*] Checking Offset: 0, Key Size: 24 bytes, Key: e7b88e408e157fdb470b6b00fe694f45048e745732b3fb5d
[*] Checking Offset: 1, Key Size: 24 bytes, Key: b88e408e157fdb470b6b00fe694f45048e745732b3fb5d92
[*] Checking Offset: 2, Key Size: 24 bytes, Key: 8e408e157fdb470b6b00fe694f45048e745732b3fb5d928c
[*] Checking Offset: 3, Key Size: 24 bytes, Key: 408e157fdb470b6b00fe694f45048e745732b3fb5d928c50
[*] Checking Offset: 4, Key Size: 24 bytes, Key: 8e157fdb470b6b00fe694f45048e745732b3fb5d928c50b4
[*] Checking Offset: 5, Key Size: 24 bytes, Key: 157fdb470b6b00fe694f45048e745732b3fb5d928c50b40f
[*] Checking Offset: 6, Key Size: 24 bytes, Key: 7fdb470b6b00fe694f45048e745732b3fb5d928c50b40fb4
[*] Checking Offset: 7, Key Size: 24 bytes, Key: db470b6b00fe694f45048e745732b3fb5d928c50b40fb42f
[*] Checking Offset: 8, Key Size: 24 bytes, Key: 470b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d
[*] Checking Offset: 9, Key Size: 24 bytes, Key: 0b6b00fe694f45048e745732b3fb5d928c50b40fb42f7d31
[*] Checking Offset: 10, Key Size: 24 bytes, Key: 6b00fe694f45048e745732b3fb5d928c50b40fb42f7d3193
[*] Checking Offset: 11, Key Size: 24 bytes, Key: 00fe694f45048e745732b3fb5d928c50b40fb42f7d31931b
[*] Checking Offset: 12, Key Size: 24 bytes, Key: fe694f45048e745732b3fb5d928c50b40fb42f7d31931b59
[*] Checking Offset: 13, Key Size: 24 bytes, Key: 694f45048e745732b3fb5d928c50b40fb42f7d31931b59b6
[*] Checking Offset: 14, Key Size: 24 bytes, Key: 4f45048e745732b3fb5d928c50b40fb42f7d31931b59b6ab
[*] Checking Offset: 15, Key Size: 24 bytes, Key: 45048e745732b3fb5d928c50b40fb42f7d31931b59b6abbe
[*] Checking Offset: 16, Key Size: 24 bytes, Key: 048e745732b3fb5d928c50b40fb42f7d31931b59b6abbeae
[*] Checking Offset: 17, Key Size: 24 bytes, Key: 8e745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc
[*] Checking Offset: 18, Key Size: 24 bytes, Key: 745732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b
[*] Checking Offset: 19, Key Size: 24 bytes, Key: 5732b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b
[*] Checking Offset: 20, Key Size: 24 bytes, Key: 32b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b6e
[*] Checking Offset: 21, Key Size: 24 bytes, Key: b3fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b6ea5
[*] Checking Offset: 22, Key Size: 24 bytes, Key: fb5d928c50b40fb42f7d31931b59b6abbeaebc7b7b6ea58a
[*] Checking Offset: 23, Key Size: 24 bytes, Key: 5d928c50b40fb42f7d31931b59b6abbeaebc7b7b6ea58a15
[*] Checking Offset: 24, Key Size: 24 bytes, Key: 928c50b40fb42f7d31931b59b6abbeaebc7b7b6ea58a159b
[*] Checking Offset: 25, Key Size: 24 bytes, Key: 8c50b40fb42f7d31931b59b6abbeaebc7b7b6ea58a159be6
[*] Checking Offset: 26, Key Size: 24 bytes, Key: 50b40fb42f7d31931b59b6abbeaebc7b7b6ea58a159be6c6
[*] Checking Offset: 27, Key Size: 24 bytes, Key: b40fb42f7d31931b59b6abbeaebc7b7b6ea58a159be6c6f8
[*] Checking Offset: 28, Key Size: 24 bytes, Key: 0fb42f7d31931b59b6abbeaebc7b7b6ea58a159be6c6f8b6
[*] Checking Offset: 29, Key Size: 24 bytes, Key: b42f7d31931b59b6abbeaebc7b7b6ea58a159be6c6f8b6e1
[*] Checking Offset: 30, Key Size: 24 bytes, Key: 2f7d31931b59b6abbeaebc7b7b6ea58a159be6c6f8b6e199
[*] Checking Offset: 31, Key Size: 24 bytes, Key: 7d31931b59b6abbeaebc7b7b6ea58a159be6c6f8b6e19994
[*] Checking Offset: 32, Key Size: 24 bytes, Key: 31931b59b6abbeaebc7b7b6ea58a159be6c6f8b6e1999466
[*] Checking Offset: 33, Key Size: 24 bytes, Key: 931b59b6abbeaebc7b7b6ea58a159be6c6f8b6e19994668c
[*] Checking Offset: 34, Key Size: 24 bytes, Key: 1b59b6abbeaebc7b7b6ea58a159be6c6f8b6e19994668cb8
[*] Checking Offset: 35, Key Size: 24 bytes, Key: 59b6abbeaebc7b7b6ea58a159be6c6f8b6e19994668cb869
[*] Checking Offset: 36, Key Size: 24 bytes, Key: b6abbeaebc7b7b6ea58a159be6c6f8b6e19994668cb8697a
[*] Checking Offset: 37, Key Size: 24 bytes, Key: abbeaebc7b7b6ea58a159be6c6f8b6e19994668cb8697ad5
[*] Checking Offset: 38, Key Size: 24 bytes, Key: beaebc7b7b6ea58a159be6c6f8b6e19994668cb8697ad5f3
[*] Checking Offset: 39, Key Size: 24 bytes, Key: aebc7b7b6ea58a159be6c6f8b6e19994668cb8697ad5f3d8
[*] Checking Offset: 40, Key Size: 24 bytes, Key: bc7b7b6ea58a159be6c6f8b6e19994668cb8697ad5f3d8c2
[*] Checking Offset: 41, Key Size: 24 bytes, Key: 7b7b6ea58a159be6c6f8b6e19994668cb8697ad5f3d8c2d4
[*] Checking Offset: 42, Key Size: 24 bytes, Key: 7b6ea58a159be6c6f8b6e19994668cb8697ad5f3d8c2d400
[*] Checking Offset: 43, Key Size: 24 bytes, Key: 6ea58a159be6c6f8b6e19994668cb8697ad5f3d8c2d400de
[*] Checking Offset: 44, Key Size: 24 bytes, Key: a58a159be6c6f8b6e19994668cb8697ad5f3d8c2d400de22
[*] Checking Offset: 45, Key Size: 24 bytes, Key: 8a159be6c6f8b6e19994668cb8697ad5f3d8c2d400de2298
[*] Checking Offset: 46, Key Size: 24 bytes, Key: 159be6c6f8b6e19994668cb8697ad5f3d8c2d400de229845
[*] Checking Offset: 47, Key Size: 24 bytes, Key: 9be6c6f8b6e19994668cb8697ad5f3d8c2d400de2298455f
[*] Checking Offset: 48, Key Size: 24 bytes, Key: e6c6f8b6e19994668cb8697ad5f3d8c2d400de2298455fbf
[*] Checking Offset: 49, Key Size: 24 bytes, Key: c6f8b6e19994668cb8697ad5f3d8c2d400de2298455fbf0b
[*] Checking Offset: 50, Key Size: 24 bytes, Key: f8b6e19994668cb8697ad5f3d8c2d400de2298455fbf0b20

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
