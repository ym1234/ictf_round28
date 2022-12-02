#!/usr/bin/env python3

# Their solution;
# lines = ["y=input()# ", "eval(y)#"]
# def checksum(s):
#     ret = 0
#     for c in s:
#         ret ^= ord(c)
#     return ret
# for line in lines:
#     print(line + chr(checksum(line)))

# My dumbass solution after tons of trial and error
# Use comments you fucking genius
# kq1=vars
# exit=kq1;-2345

# Problem
while True:
    inp = input('>>> ')
    check = 0
    used = set()
    for c in inp:
        check ^= ord(c)
        if c in used:
            print("DRY!")
            exit()
        used |= {c}
    if check:
        print("Non-zero checksum!")
        exit()
    exec(inp)
