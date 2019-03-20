def xor(a, b):
    return [a ^ b for a, b in zip(bytearray.fromhex(a), bytearray.fromhex(b))]


a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
print(bytearray(xor(a, b)).hex())
