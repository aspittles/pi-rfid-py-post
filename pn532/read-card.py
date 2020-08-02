import sys
sys.path.append('/home/pi/pi-rfid-py-post/pn532/py532lib-master')
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

pn532 = Pn532_i2c()
pn532.SAMconfigure()

card_data = pn532.read_mifare().get_data()

#lines.append(line.decode('utf-8', 'slashescape'))
#b"abcde".decode("utf-8")
print(card_data)
