ct = [20, 37, 47, 47, 56, 52, 38, 46, 51, 56, 23, 58, 57, 50, 86, 95, 95, 103, 0]
ct = ct[:-1] # cutting the extra 0
flag_start = []
flag_end = [ord('}')]

start = 1

for c in ct:
    if start:
        flag_start.append(flag_end[0]^c)
    else:
        flag_end = [flag_start[-1]^c] + flag_end
    start = not start
    print(bytes(flag_start), bytes(flag_end))
print(bytes(flag_start) + bytes(flag_end))
