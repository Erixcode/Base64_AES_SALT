from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Function to attempt decryption with a given key
def try_decrypt(key, iv, ciphertext, offset, key_size):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        print(f"\n[+] Decryption succeeded!")
        print(f"Key (Hex): {key.hex()}")
        print(f"Offset: {offset}, Key Size: {key_size} bytes")
        print(f"Decrypted Output: {decrypted_data}")
        return True
    except Exception:
        return False

# Main logic
def brute_force_keys(data):
    print("Starting brute-force search for AES keys at all offsets...")

    iv_size = 16  # IV size for AES-CBC is always 16 bytes
    for key_size in [16, 24, 32]:  # AES-128, AES-192, AES-256 key sizes
        print(f"\nTrying AES-{key_size * 8} keys...")

        for offset in range(len(data) - key_size - iv_size):
            key_candidate = data[offset:offset + key_size]
            iv = data[offset + key_size:offset + key_size + iv_size]
            ciphertext = data[offset + key_size + iv_size:]

            # Debug output: Key being checked
            print(f"[*] Checking Offset: {offset}, Key Size: {key_size} bytes, Key: {key_candidate.hex()}")

            # Attempt decryption
            if try_decrypt(key_candidate, iv, ciphertext, offset, key_size):
                print(f"\n[+] Success with offset {offset}, key size {key_size} bytes.")
                return

    print("\n[-] Decryption unsuccessful: No valid keys found.")

# Read base64 string from file
def read_base64_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            base64_str = f.read().strip()
        return base64.b64decode(base64_str)
    except Exception as e:
        print(f"Error reading or decoding file: {e}")
        exit(1)

# File path to the Base64 file
file_path = "PATH_TO_YOUR_HASH.txt"  # Replace with your file path

# Decode data and run brute-force
decoded_data = read_base64_from_file(file_path)
brute_force_keys(decoded_data)
