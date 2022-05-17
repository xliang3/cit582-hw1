
def encrypt(key,plaintext):
    ciphertext=""
    for letter in plaintext:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            temp = ord(letter) - ord('a') 
            temp %= 26
            ciphertext += chr(temp + ord('a'))
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp = ord(letter) - ord('A')
            temp %= 26
            ciphertext += chr(temp + chr('A'))
        else:
            ciphertext += letter
    print(plaintext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for letter in ciphertext:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            temp = ord(letter) - ord('a') + 26
            temp %= 26
            plaintext += chr(temp + ord('a'))
        elif letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp = ord(letter) - ord('A') + 26
            temp %= 26
            plaintext += chr(temp + chr('A'))
        else:
            plaintext += letter
    return plaintext


