import math


def xor(s, chr):
    return[a ^ chr for a in s]


def score(s, freq):
    sum = 0
    for l, f in freq.items():
        d = f - (s.count(ord(l.lower())) + s.count(ord(l.upper()))) / len(s)
        sum = sum + d * d
    return math.sqrt(sum)


english = {' ': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406,
           'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}

i = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
chrs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


i = bytearray.fromhex(i)
chrs = bytearray(chrs, 'ascii')
l = []

for c in chrs:
    x = xor(i, c)
    s = score(x, english)
    l.append((s, chr(c), bytearray(x).decode()))

l.sort(key=lambda x: x[0])
print(l[0])
