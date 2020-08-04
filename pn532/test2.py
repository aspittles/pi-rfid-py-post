import binascii

def uid_to_num(uid):
  n = 0
  for i in range(0, 5):
    n = n * 256 + uid[i]
  return n

# KeyCard 1
print("Test1 = [162, 220, 84, 28, 54]")
print("ID: 699481201718")
# b'4b010100040804a2dc541c'
test1 = bytearray(b'K\x01\x01\x00\x04\x08\x04\xa2\xdcT\x1c')

# KeyCard 2
print("Test2 = [182, 230, 120, 43, 3]")
print("ID: 785550682883")
# b'4b010100040804b6e6782b'
test2 = bytearray(b'K\x01\x01\x00\x04\x08\x04\xb6\xe6x+')

# KeyCard 3
print("Test3 = [18, 156, 180, 52, 14]")
print("ID: 79938466830")
test3 = bytearray(b'K\x01\x01\x00\x04\x08\x04\x12\x9c\xb44')

# CreditCard
#    ATQA (SENS_RES): 00  44
print("CreditCard = UID: 02  b0  fe  01  c0  c4  40")
#      SAK (SEL_RES): 20
#                ATS: 78  80  74  02  00  31  c1  73  c8  21  10  64  47  4d  31  33  00  90  00
test4 = bytearray(b'K\x01\x01\x00D \x07\x02\xb0\xfe\x01\xc0\xc4@\x14x\x80t\x02\x001\xc1s\xc8!\x10dGM13\x00\x90\x00')
# b'4b01010044200702b0fe01c0c44014788074020031c173c8211064474d3133009000'

print("Test 1 = ", test1)
print("Test 2 = ", test2)
print("Test 3 = ", test3)
print("Test 4 = ", test4)
print("")

readable_data1 = binascii.b2a_hex(test1)
print(readable_data1)
readable_data2 = binascii.b2a_hex(test2)
print(readable_data2)
readable_data3 = binascii.b2a_hex(test3)
print(readable_data3)
readable_data4 = binascii.b2a_hex(test4)
print(readable_data4)
print("")

test11 = test1[7:11] + bytearray(b'\x36')
test21 = test2[7:11] + bytearray(b'\x03')
test31 = test3[7:11] + bytearray(b'\x0e')
test41 = test4[7:14]

print(test11[0],test11[1],test11[2],test11[3],test11[4])
print(test21[0],test21[1],test21[2],test21[3],test21[4])
print(test31[0],test31[1],test31[2],test31[3],test31[4])
print(test41[0],test41[1],test41[2],test41[3],test41[4],test41[5],test41[6])
print("")

print(str(uid_to_num(test11)))
print(str(uid_to_num(test21)))
print(str(uid_to_num(test31)))
print("")

