import binascii


test4 = bytearray(b'\x04\xf7F\xc4{')
test7 = bytearray(b'\xf7F\xc4{')
test1 = bytearray(b'K\x01\x01\x00\x04\x08\x04\xf7F\xc4{')
test5 = bytearray(b'\x04\xc9Qr\xa2')
test8 = bytearray(b'\xc9Qr\xa2')
test2 = bytearray(b'K\x01\x01\x00\x04\x08\x04\xc9Qr\xa2')
test6 = bytearray(b'\x04\xfb\xa1\x9f\x1b')
test9 = bytearray(b'\xfb\xa1\x9f\x1b')
test3 = bytearray(b'K\x01\x01\x00\x04\x08\x04\xfb\xa1\x9f\x1b')

print(test1)
print(test2)
print(test3)
readable_data1 = binascii.b2a_hex(test1)
print(readable_data1)
readable_data2 = binascii.b2a_hex(test2)
print(readable_data2)
readable_data3 = binascii.b2a_hex(test3)
print(readable_data3)
readable_data4 = binascii.b2a_hex(test4)
print(readable_data4)
readable_data5 = binascii.b2a_hex(test5)
print(readable_data5)
readable_data6 = binascii.b2a_hex(test6)
print(readable_data6)
readable_data7 = binascii.b2a_hex(test7)
print(readable_data7)
readable_data8 = binascii.b2a_hex(test8)
print(readable_data8)
readable_data9 = binascii.b2a_hex(test9)
print(readable_data9)

def uid_to_num(uid):
  n = 0
  for i in range(0, 5):
    n = n * 256 + uid[i]
  return n

#print(str(int.from_bytes(b'1b', byteorder='big')))
#print(str(binascii.b2a_uu(readable_data4)))
#print(str(binascii.b2a_base64(b'1b')))
print(str(int(readable_data4, 16)))
print(str(int(readable_data5, 16)))
print(str(int(readable_data6, 16)))

print(str(uid_to_num(readable_data7)))
print(str(uid_to_num(readable_data8)))
print(str(uid_to_num(readable_data9)))
