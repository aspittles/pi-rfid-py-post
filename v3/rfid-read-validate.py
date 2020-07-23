#  "config": {
#    "log_level": "DEBUG",
#    "log_file": "~/pi-rfid-py-post/v3/rfid-read-validate.log"
#    "reader": "RF522" }
# rfid-door-lock.json  rfid-read-validate.log  rfid-read-validate.py  rfid.sh

from time import sleep
import RPi.GPIO as GPIO
import sys
import json
import logging

sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

with open('rfid-door-lock.json') as f:
  data = json.load(f)

logging.basicConfig(filename=(data["config"]["log_file"]),level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s')

reader = SimpleMFRC522()

try:
  print("Hold a tag near the reader")
  uid, text = reader.read()
  print("Key UID: %s" % (uid))

  try:
    print((data["users"][str(uid)]["firstName"]) + " " + (data["users"][str(uid)]["lastName"]) + " - Status: " + str(data["users"][str(uid)]["active"]))
    logging.info("Access by:" + (data["users"][str(uid)]["firstName"]) + " " + (data["users"][str(uid)]["lastName"]))
    print(data["users"][str(uid)])
  except KeyError:
    print("ID doesn't exist")
    logging.warning("Access attempt by: " + str(uid))
finally:
#  sleep(2)
  GPIO.cleanup()
