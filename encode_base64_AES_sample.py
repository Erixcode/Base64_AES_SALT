from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import base64

# Generate AES-256 key and IV
key = os.urandom(32)  # 32 bytes for AES-256
iv = os.urandom(16)   # 16 bytes IV for AES
plaintext = b"This is a test message"  # Example plaintext

# Encrypt the plaintext
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Create data with key at offset 11
offset = 11
padding_before_key = os.urandom(offset)
data_with_key = padding_before_key + key + iv + ciphertext

# Encode the final data as Base64
base64_data = base64.b64encode(data_with_key).decode()

# Save to file for testing
output_file = "test_with_key_at_offset_11.txt"
with open(output_file, "w") as f:
    f.write(base64_data)

print("Base64-encoded data with key at offset 11 generated successfully!")
print(f"Key (Hex): {key.hex()}")
print(f"IV (Hex): {iv.hex()}")
print(f"Output file: {output_file}")
