# https://web.archive.org/web/20220506175823/https://www.quaxio.com/exploring_three_weaknesses_in_rsa/
# from gmpy2 import *
from functools import reduce
from Crypto.Util import number
from Crypto.PublicKey.RSA import *

# c = get_context()
# c.precision = 1024
# set_context(c)

n = []
c = []
e = 65537

with open('../messages.txt') as x:
    y = [i.strip() for i in x.read().strip().split('\n')]
    for i in y:
        j = i.split(',')
        n.append(int(j[0]))
        c.append(int(j[1]))


for i in range(1337):#len(n)):
    with open(str(i) + ".pem", "wb") as x:
        x.write(number.long_to_bytes(c[i]))
        # key = construct((n[i], e), consistency_check=False)
        # x.write(key.export_key())

# def invmod(x, p):
#     return pow(x, -1, p)

# def chinese_remainder(mods, remainders):
#     mx = reduce(lambda x, y:  x * y, mods)
#     series = list(map(lambda x: x[0] * mx * invert(mx/x[1], x[1]) / x[1], zip(remainders, mods)))
#     return reduce(lambda x, y: x + y, series) % mx

# # for i in range(1,1337):
# x = chinese_remainder(n[:461], c[:461])
# # print(x)
# print(root(x, e))
#     # print(mpz(rootn(x, e)))
