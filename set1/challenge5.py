def repeating_XOR(input, cypher):
    i = 0
    l = []
    for c in input:
        l.append(c ^ cypher[i])
        i = (i+1) % len(cypher)
    return bytearray(l)


input = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

input = bytearray(input, 'ascii')
cypher = bytearray('ICE', 'ascii')

if __name__ == '__main__':
    print(repeating_XOR(input, cypher).hex())
