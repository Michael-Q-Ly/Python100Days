"""
Caesar Cipher
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    """
    Shift origininal text forward by user-specified amount
    """
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    """
    Shift origininal text backward by user-specified amount
    """
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")


def caesar(encode_or_decode, original_text, shift_amount):
    """
    Combine encrypt and decrypt functions into one
    """
    cipher_text = ""
    if encode_or_decode.lower() == "encode":
        shift_amount *= 1
    elif encode_or_decode == "decode":
        shift_amount *= -1
    else:
        print("Invalid choice!")
        exit()
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


if __name__ == "__main__":
    caesar(direction, text, shift)
