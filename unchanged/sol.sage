from Crypto.Util import number

with open("nums.txt", "r") as f:
    y = [Integer(int(z, 16)) for z in f.read().strip().split('\n')]

x = var('x')
flag = b""
for i in range(0, len(y), 2):
    flag += number.long_to_bytes(int(solve_mod((x * y[i] + y[i+1]) == x, 2**64)[0][0]))[::-1]
print(flag.decode("utf8"))
