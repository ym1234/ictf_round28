from Crypto.PublicKey import RSA
from Crypto.Util import number
from Crypto.Cipher import PKCS1_OAEP
cipher250 = open("../ciphers/250.rsa", "rb").read()
cipher461 = open("../ciphers/461.rsa", "rb").read()
key1 = open("1.key", "r").read().strip()
key2 = open("2.key", "r").read().strip()

for i in [key1, key2]:
    key = RSA.importKey(i)
    print(key.n)
    d = key.d
    n = key.n
    f = number.bytes_to_long(cipher250)
    s = number.bytes_to_long(cipher461)
    print(number.long_to_bytes(pow(f, d, n)))
    print(number.long_to_bytes(pow(s, d, n)))
