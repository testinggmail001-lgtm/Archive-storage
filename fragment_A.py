import hashlib

candidate = input("PASSWORD:")
salt = "BLACKWATCH-E04-0217"

# 1. ASCII
ascii_values = [ord(c) for c in candidate]
ascii_output = " ".join(map(str, ascii_values))
print("ASCII:", ascii_output)

# 2. HEX
hex_output = "".join(f"{n:02x}" for n in ascii_values)
print("HEX:", hex_output)

# 3. SHA-256
sha_output = hashlib.sha256((salt + candidate).encode()).hexdigest()
print("SHA256:", sha_output)

# hardcoded verification key
target = ""

if sha_output == target:
    print("MATCH")
else:
    print("NO MATCH")
