from time import sleep
import RPi.GPIO as GPIO
import sys
import json
import logging
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

# Function to Read the RFID card
def rfid_read():
  print("Hold a tag near the reader")
  uid, text = reader.read()
  return uid;

# Function to Validate the Card UID against JSON list of allowed users
def validate_access( uid, data ):
  try:
    name = (data["users"][str(uid)]["firstName"]) + " " + (data["users"][str(uid)]["lastName"])
    authorised = (data["users"][str(uid)]["active"])
    if authorised:
      logging.info("Access by:" + name)
    else:
      logging.warning("Deactivated card attempt by: " + str(uid) + " (" + name + ")")
    # print(name + " " + str(status))
    # print((data["users"][str(uid)]["firstName"]) + " " + (data["users"][str(uid)]["lastName"]) + " - Status: " + str(data["users"][str(uid)]["active"]))
    #print(data["users"][str(uid)])
  except KeyError:
    print("ID doesn't exist")
    logging.warning("Access attempt by: " + str(uid))
    authorised = False

  return authorised;

# Read the config file and store in memory
with open('rfid-door-lock.json') as f:
  data = json.load(f)

# Enable & configure logging
logging.basicConfig(filename=(data["config"]["log_file"]),level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s')

# Create RFID reader object
reader = SimpleMFRC522()

# Main Loop
try:
  while True:
    uid = rfid_read();
    authorised = validate_access( uid, data );
    print(str(authorised))
    sleep(5);

except KeyboardInterrupt:
  GPIO.cleanup()
