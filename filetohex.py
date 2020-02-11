import binascii

filename = ''
with open(filename, 'rb') as f:
    convert = f.read()

hex_text = binascii.hexlify(convert)

print(hex_text)


