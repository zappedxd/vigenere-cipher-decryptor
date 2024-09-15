import string

def generate_vigenere_table():
    table = {}
    for i, char in enumerate(string.ascii_uppercase):
        shifted_alphabet = string.ascii_uppercase[i:] + string.ascii_uppercase[:i]
        table[char] = shifted_alphabet
    return table

def generate_key(message, key):
    key = key.upper()
    key_index = 0
    extended_key = ''
    for char in message:
        if char in string.ascii_uppercase:
            extended_key += key[key_index]
            key_index = (key_index + 1) % len(key)
        else:
            extended_key += char
    return extended_key

def decrypt(ciphertext, key):
    vigenere_table = generate_vigenere_table()
    key = generate_key(ciphertext, key)
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:
            row = key[i]
            col = vigenere_table[row].index(char)
            decrypted_text += string.ascii_uppercase[col]
        else:
            decrypted_text += char
    return decrypted_text

def main():
    ciphertext = input("Enter the ciphertext to decrypt: ").upper()
    key = input("Enter the keyword: ").upper()

    decrypted = decrypt(ciphertext, key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
