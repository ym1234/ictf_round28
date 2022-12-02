from pwn import *
from re import *

# apparently this format works, idfk lmfao
# TOOK A TON OF TIME FUCK THIS I HATE REGEX
# []\151^+\-[0-9\\][^\143][^\012]+
# c = remote("puzzler7.imaginaryctf.org", 7003)
c = process(("python", "/home/ym/fun/ctfs/regrets_revenge/flag.py"))
c.recvuntil(b"Enter your regex: ")

# Wrote a program to try all string.printable[:-6] one by one
flag_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'*._{|}"
flag = ''
while True:
    high = len(flag_characters)
    low = 0
    while (high - low) > 1:
        mid = (high + low) // 2
        r = flag_characters[mid:high]
        l = flag_characters[low:mid]
        print("Trying: " + l)
        regex = ''.join('[]^+\\-\\' + oct(ord(x))[2:] + '[0-9\\\\]' for x in flag)
        regex += "[^" + ''.join('\\' + oct(ord(x))[2:]  for x in l) + ']'
        regex += "[^" + '\\0' + oct(ord('\n'))[2:] + ']+'
        print("Regex: " + regex + '\n')
        c.send(bytes(regex + '\n', 'ascii'))
        if c.recvuntil(b"Enter your regex: ").decode('utf8').split('\n')[0] == "Nope!":
            high = mid
        else:
            low = mid
    flag += flag_characters[low]
    print("current flag: " + flag)
    # Doesn't work for some reason, idfc
    if flag[-1] == '}':
        break

