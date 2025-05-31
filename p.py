def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            base = ord('A') if char.isupper() else ord('a')  # Base ASCII
            # Shift the character
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-letters the same
    return result

'''This function shifts each letter by the given shift value.

It handles both uppercase and lowercase letters.

% 26 makes sure it wraps around the alphabet.'''


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

#To decrypt, we reverse the shift.


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

#Takes user input.


encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)




