
def encrypt(key,plaintext):
    ciphertext=""
    for letter in plaintext:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            temp = ord(letter) - ord('a') + key
            temp %= 26
            ciphertext += chr(temp + ord('a'))
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp = ord(letter) - ord('A') + key
            temp %= 26
            ciphertext += chr(temp + ord('A'))
        else:
            ciphertext += letter
    print(plaintext)
    print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for letter in ciphertext:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            temp = ord(letter) - ord('a') + 26 - key
            temp %= 26
            plaintext += chr(temp + ord('a'))
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp = ord(letter) - ord('A') + 26 - key
            temp %= 26
            plaintext += chr(temp + ord('A'))
        else:
            plaintext += letter
    print(ciphertext)
    print(plaintext)
    return plaintext


# decrypt(1, encrypt(1, "wahaSDFWEF22rfd!@#ha"))