def encrypt(message, shift):
    encrypted = ""

    for char in message:
        if char == " ":
            encrypted += " "
        elif char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:
        if char == " ":
            decrypted += " "
        elif char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted += char

    return decrypted


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)