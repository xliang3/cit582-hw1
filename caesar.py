
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
            ciphertext += chr(temp + chr('A'))
        else:
            ciphertext += letter
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for letter in ciphertext:
        plaintext += letter
    return plaintext


