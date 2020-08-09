import binascii
import sys
sys.path.append('/home/pi/py532lib-master')
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

def uid_to_num(uid,size):
  n = 0
  for i in range(0, size):
    n = n * 256 + uid[i]
  return n

pn532 = Pn532_i2c()
pn532.SAMconfigure()


try:
  while True:
    card_data = pn532.read_mifare().get_data()
    uid = uid_to_num(card_data[7:7+card_data[6]],card_data[6])
    print(str(uid))
    sleep(2)
except KeyboardInterrupt:
  GPIO.cleanup()




