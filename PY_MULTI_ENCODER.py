#
#python multi encoder/decoder by tree43
#version 1.0.0
#





import time


def encode():
 import base64
    #user input--------------------
 print("----------------")
 text_to_encode = input("text to encode:")
 print("origanal text^")
 print("----------------")

  #base 32------------------------

 start_time = time.time()
 original_text = text_to_encode


 bytes_to_encode = original_text.encode('utf-8')


 encoded_base32_bytes = base64.b32encode(bytes_to_encode)


 encoded_base32_string = encoded_base32_bytes.decode('ascii')

 print(f"Encoded Base32: {encoded_base32_string}")

 #bianare-------------------------

 def text_to_binary(text):
    """
    Converts a given text string into its binary representation.
    Each character is converted to its 8-bit binary equivalent.
    """
    binary_representation = []
    for char in text:
        # Get the ASCII/Unicode ordinal value of the character
        ordinal_value = ord(char)
        # Convert the ordinal value to its binary string representation
        # 'b' format specifier converts to binary, zfill(8) pads with leading zeros to 8 bits
        binary_char = format(ordinal_value, 'b').zfill(8)
        binary_representation.append(binary_char)
    
    # Join the binary representations of each character with a space for readability
    return ' '.join(binary_representation)

 # Example usage:
 input_text = text_to_encode
 binary_output = text_to_binary(input_text)
 print(f"binary: {binary_output}")

 #ascii values
 input_string = text_to_encode
 ascii_values = [ord(char) for char in input_string]
 print(f"ascii values: {ascii_values}")


 #base64------------------------

 import base64

 # The original text string
 original_text = text_to_encode

 # Step 1: Encode the string to bytes (using UTF-8)
 text_bytes = original_text.encode('utf-8')

 # Step 2: Encode the bytes to Base64
 base64_bytes = base64.b64encode(text_bytes)

 # Step 3: Decode the Base64 bytes back to a string (optional, for display)
 base64_string = base64_bytes.decode('utf-8')

 print(f"Base64 Encoded: {base64_string}")

 #mores_code-------------------------

 MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.',
        ' ': '/'  # Space between words
    }


 def text_to_morse(text):
        morse_code = []
        # Convert the input text to uppercase for dictionary lookup
        text = text.upper()
        for char in text:
            if char in MORSE_CODE_DICT:
                morse_code.append(MORSE_CODE_DICT[char])
            else:
                # Handle characters not in the dictionary (e.g., ignore or warn)
                print(f"Warning: Character '{char}' not found in Morse code dictionary.")
        # Join the individual Morse code characters with a space
        return ' '.join(morse_code)


 converted_morse = text_to_morse(text_to_encode)
 print(f"Morse Code: {converted_morse}")

 #hex----------------

 # Encode the string to bytes
 bytes_representation = text_to_encode.encode('utf-8')

 # Convert the bytes to a hexadecimal string
 hex_representation = bytes_representation.hex()

 print(f"Hexadecimal: {hex_representation}")

 end_time = time.time()
 print("----------------")
 elapsed_time = end_time - start_time
 print(f"Program took {elapsed_time:.8f} seconds to run (wall clock time).")
 print("----------------")

def decode():
    import base64
    print("----------------")
    text_to_decode = input("text to decode:")
    print("encoded text^")
    print("----------------")
    
    try:
     encoded_bytes = text_to_decode.encode('ascii')
     decoded_bytes = base64.b64decode(encoded_bytes)

     decoded_string = decoded_bytes.decode('utf-8')
     print(f"Decoded base64: {decoded_string}")
    except:
        print("base64 err")

    try:
     encoded_bytes32 = text_to_decode.encode('ascii')
     decoded_bytes32 = base64.b32decode(encoded_bytes32)

     decoded_string32 = decoded_bytes32.decode('utf-8')
     print(f"Decoded base32: {decoded_string32}")
    except:
        print("base32 err")
    





encode_decode = input("encode or decode(decode is in progress)")

if encode_decode == "encode":
    encode()

if encode_decode =="decode":
      decode()






input("press enter to exit")