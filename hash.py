from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import XOR
import base64
from datetime import datetime

def h (key):
    key1 = SHA256.new(key).hexdigest()
    key1_list = list(key1)
    for i in range (20, len(key1_list)):
        key1_list[i] = '0'
    key1 = "".join(key1_list)
    return key1

def H (key):
    public_keyA = Random.new().read(16)
    public_keyB = Random.new().read(16)
    time_stamp = str(datetime.now())
    result = SHA256.new(key + public_keyA + public_keyB + time_stamp).hexdigest()
    return result

def encrypt(key, email):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(email))

def decrypt(key, ctext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ctext))

def main():
    key0 = Random.new().read(16)
    key1 = h(key0)
    key2 = H(key1)[0:16]
    print key2
    email = 'This is an email message'
    ctext = encrypt(key2, email)
    print ctext

if __name__ == "__main__": main()
