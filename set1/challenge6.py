import base64
from challenge3 import decode
from challenge5 import repeating_XOR


def hamming(a, b):
    s = 0
    for i, j in zip(a, b):
        x = i ^ j
        while x > 0:
            s += x & 1
            x >>= 1
    return s


path = "./6.txt"
with open(path) as f:
    input = ''.join([x.strip() for x in f.readlines()])
input = base64.b64decode(input)
# input = bytearray('1234567890', 'ascii')

distances = []
# find possible keysizes
for keysize in range(2, 40):
    numblocks = int(len(input) / keysize)
    blocksum = 0
    for i in range(numblocks-1):
        a = input[i * keysize: (i+1) * keysize]
        b = input[(i+1) * keysize: (i+2) * keysize]
        blocksum += hamming(a, b)
    distances.append((keysize, blocksum / keysize / numblocks))

distances.sort(key=lambda x: x[1])

distances = distances[:1]
print('distances: ', distances)


# break into blocks of keysize and transpose
for keysize in list(list(zip(*distances))[0]):
    key = []
    for i in range(keysize):
        block = input[i::keysize]
        dec = decode(block)
        key.append(dec[1])
    # use key to decode input
    print('key:', key, ''.join(chr(x) for x in key))
    print('decrypted:', repeating_XOR(input, key).decode())
