#!/usr/bin/env python3
import base64
import sys

def decode_base64(encoded_str):
    # Decoding the Base64 encoded string
    decoded_bytes = base64.b64decode(encoded_str)
    try:
        # Assuming UTF-8 encoding for the decoded bytes
        decoded_str = decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # Fallback to UTF-16 if UTF-8 fails
        decoded_str = decoded_bytes.decode('utf-16')
    return decoded_str

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./decode.py \"Base64EncodedString\"")
        sys.exit(1)
    
    encoded_str = sys.argv[1]
    print(decode_base64(encoded_str))
