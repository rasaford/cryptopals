import math
from challenge3 import decode


def find_word(path):
    with open(path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    dec = [decode(bytearray.fromhex(x)) for x in content]
    dec.sort(key=lambda x: x[0])
    d = dec[0]
    print(d[0], chr(d[1]), d[2].decode('ascii'))


find_word("./4.txt")
