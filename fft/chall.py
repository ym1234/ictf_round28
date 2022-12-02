import numpy as np

# flag = open("flag.txt", "rb").read().strip()
flag = b"ictf{Hello world}"
flag += b'1' * (72 - len(flag))
# print(list(flag))
N = len(flag)
freq = np.fft.fft(list(flag))
print(freq)
print(freq[-N // 2:])
print(np.fft.ifft(freq))
# np.save("output.npy", np.insert(freq, 0, N), allow_pickle=False)
