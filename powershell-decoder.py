import base64

print("=== PowerShell Base64 Decoder ===\n")

filename = input("Enter path to file containing encoded string: ")

try:
    with open(filename, "r") as f:
        encoded = f.read().strip()

    # Fix padding if missing
    encoded += "=" * (4 - len(encoded) % 4)

    # Decode from Base64
    decoded_bytes = base64.b64decode(encoded)

    # Decode from UTF-16LE
    decoded_text = decoded_bytes.decode("utf-16-le", errors="ignore")

    print("\nDecoded output:")
    print("-" * 40)
    print(decoded_text)
    print("-" * 40)

    # Save output to file
    output_file = "decoded_output.txt"
    with open(output_file, "w") as f:
        f.write(decoded_text)
    
    print(f"\nOutput saved to {output_file}")

except FileNotFoundError:
    print("File not found - check the path")

except Exception as e:
    print(f"Error: {e}")
