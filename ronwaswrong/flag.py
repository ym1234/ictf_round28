#!/usr/bin/env python

from Crypto.Util import number

flag = open("flag.txt", "rb").read()
m = number.bytes_to_long(flag)
e = 65537

for _ in range(1336):
    q = number.getPrime(1024)
    p = number.getPrime(1024)

    n = p * q
    c = pow(m, e, n)
    print(f"{n},{c}")

