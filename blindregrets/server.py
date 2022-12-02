#!/usr/bin/env python3

from re import *

flag = open('flag.txt').read().strip()
assert flag.startswith('ictf{') and flag.endswith('}')

print('='*80)
print(open(__file__).read())
print('='*80)

while True:
    fullmatch(input("Enter your regex: "), flag)
