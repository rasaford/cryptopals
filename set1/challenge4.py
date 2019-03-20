import math

ENG = {' ': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406,
       'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074}
CHRS = bytearray('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ascii')


def xor(s, chr):
    return bytearray([a ^ chr for a in s])


def distance(s, freq):
    sum = 0
    for l, f in freq.items():
        d = f - (s.count(ord(l.lower())) + s.count(ord(l.upper()))) / len(s)
        sum = sum + d * d
    return math.sqrt(sum)


def decode(d):
    min = 1 << 30
    min_b = ()
    for c in CHRS:
        x = xor(d, c)
        s = distance(x, ENG)
        if s < min:
            min = s
            min_b = (s, x)
    return min_b


def find_word(path):
    with open(path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for line in content:
        d = decode(bytearray.fromhex(line))
        try:
            print("{} {} -> {}".format(line, d[0], d[1].decode('ascii')))
        except:
            a = 4


find_word("./4.txt")
