import random

# Caesar

def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

def hackdecrypt(c):
    container = []
    for el in set(c):
        container.append((el, c.count(el)))
    container.sort(key = lambda x:x[1] , reverse = True)
    shifts = [ord(" ") - ord(el[0]) for el in container]
    for shift in shifts:
        decrypted = encrypt(shift, c)
        print(decrypted)
        cmd = input("Если текст можно прочитать - введите любое сообщение, иначе нажмите Enter | ")
        if cmd:
            return ''.join(map(chr, [(x - abs(shift)) % 65536 for x in map(ord, c)]))
        
    return "CAN'T ENCRYPT"

# Vernam

def encryptVernam(text, key = None):
    text_len = len(text)
    if not key:
        key = ''.join([chr(random.randint(0,65535)) for _ in range(text_len)])
    encrypted_text = ''.join([chr(ord(text[i])^ord(key[i])) for i in range(text_len)])
    return encrypted_text, key

# CPC

def cipher_block_chaining(text, key, vector):
    if not text:
        return ""
    block_size = len(key)
    summary_text = encryptVernam(text[:block_size], vector)[0]
    encrypted = encryptVernam(summary_text, key)[0]
    return encrypted + cipher_block_chaining(text[block_size:], key, encrypted)

def encodeCPC(text, key = None, vector = None):
    if key:
        block_size = len(key)
    else:
        block_size= 32
        key = ''.join([chr(random.randint(0,65535)) for _ in range(block_size)])
    if not vector or (len(vector) != block_size):
        vector = ''.join([chr(random.randint(0,65535)) for _ in range(block_size)])
    return cipher_block_chaining(text, key, vector), key, vector

def decodeCPC(encrypted, key, vector):
    if not encrypted:
        return ""
    block_size = len(key)
    block = len(encrypted) % block_size
    block = block_size if not block else block
    summary_text = encryptVernam(encrypted[-block:], key)[0]
    previous_vector = vector if len(encrypted) <= block_size else encrypted[- block - block_size: - block]
    decrypted = encryptVernam(summary_text, previous_vector)[0]
    return decodeCPC(encrypted[:-block], key, vector) + decrypted

# tests

if __name__ == '__main__':
    s = input('choose encrypt [1 - Caesar, 2 - Vernam, 3 - CBC]: ')
    if s.isnumeric():
        if int(s) == 1:
            text = input('input text: ')
            key = int(input('input key (number): '))
            h = encrypt(key, text)
            print(f'Caesar | e: {h}, d: {decrypt(key,h)}')
            print(f'HackCaesar | e: {h}, d: {hackdecrypt(h)}')
        elif int(s) == 2:
            text = input('input text: ')
            encrypted, key = encryptVernam(text)
            decrypted, key = encryptVernam(encrypted, key)
            print(f'Vernam | e: {encrypted}, d: {decrypted}')
        elif int(s) == 3:
            text = input('input text: ')
            encrypted, key, vector = encodeCPC(text)
            decrypted = decodeCPC(encrypted, key, vector)
            print(f'Cipher block chaining | e: {encrypted}, d: {decrypted}')
    else:
        print('failed.')
