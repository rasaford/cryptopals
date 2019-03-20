

def repeating_XOR(input, cypher):
    i = 0
    l = []
    for c in input:
        l.append(c ^ cypher[i])
        i = (i+1) % len(cypher)
    return bytearray(l)

def hamming(a, b):
    


input = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

input = bytearray(input, 'ascii')
cypher = bytearray('ICE', 'ascii')

print(repeating_XOR(input, cypher).hex())
