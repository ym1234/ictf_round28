import string
from pprint import pprint
from functools import reduce

def f(s):
    if len(s) == 0:
        return []
    return [([s[0]], s[0], s[-1])] + list(map(lambda x: ([s[0]] + x[0], x[1], x[2]), f(s[::-1][1:])))

flag = [20, 37, 47, 47, 56, 52, 38, 46, 51, 56, 23, 58, 57, 50, 86, 95, 95, 103, 0]

z = [[ord(i)] for i in "ictf{"] + [[] for i in range(15)] + [[ord('}')]]
a = [ord(i) for i in "ictf{T7HEMKC2E1IFDL}"]
pprint(f(a), width=1000)
#ictf{T7HEMKC2E1IFDL}
#iLcDtFfI{1TE72HCEKMM
# pattern:
# even left to right starting from zero
# odd right to left starting from the end

o = f(z)
pprint(o, width=1000)
for i in range(len(o)):
    l, f, s = o[i]
    if len(s) == 0:
        f, s = s, f
    try:
        andv = reduce(lambda x, y: x if len(y) == 0 else x and y[0] , l, 0xff)
        for k in string.printable:
            x = ord(k)
            if andv and x and (x ^ s[0]) == flag[i]:
                f.append(x)
    except:
        pass

x = ''.join(map(lambda x: '0' if len(x) == 0 else chr(x[0]), o[-1][0]))
flag = list('0' * (len(x) - 2))
for i in range(0, len(x) - 2, 2):
    flag[i//2] = x[i]
for i in range(1, len(x) - 2, 2):
    flag[-(i//2)-2] = x[i]
flag[-1] = '}'
print(''.join(flag))
