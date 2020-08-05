import RPi.GPIO as GPIO
import sys, logging, json, datetime, requests
from time import sleep
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
sys.path.append('/home/pi/py532lib-master')
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

# Function to Read the RFID card Using RC522 Reader
def rfid_read_RC522():
  print("Hold a tag near the RC522 reader")
  uid, text = reader.read()
  return uid

# Function to Read the RFID card Using PN532 Reader
def rfid_read_PN532():
  print("Hold a tag near the PN532 reader")
  pn532 = Pn532_i2c()
  pn532.SAMconfigure()
  card_data = pn532.read_mifare().get_data()
  uid = uid_to_num(card_data[7:11])
  return uid

# Function to convert UID bytearray to a decimal UID
def uid_to_num(uid):
  n = 0
  for i in range(0, 4):
    n = n * 256 + uid[i]
  return n

# Function to Validate the Card UID against JSON list of allowed users
def validate_access( uid, data ):
  try:
    name = (data["users"][str(uid)]["firstName"]) + " " + (data["users"][str(uid)]["lastName"])
    authorised = (data["users"][str(uid)]["active"])
    if authorised:
      # open_door()
      logging.info("ALLOW: Access by: " + str(uid) + " (" + name + ")")
      logging.debug((data["users"][str(uid)]))
      now = datetime.datetime.now()
      data["users"][str(uid)]["lastEntered"] = now.strftime("%Y-%m-%d %H:%M:%S")
      with open('rfid-door-lock.json', 'w') as f:
        json.dump(data, f)
      led_green()
    else:
      logging.info("BLOCK: Deactivated card attempt by: " + str(uid) + " (" + name + ")")
      logging.debug((data["users"][str(uid)]))
      led_red()
  except KeyError:
    authorised = False
    logging.info("BLOCK: Access attempt by: " + str(uid))
    led_red()

  return authorised;

# Function to Open the Door lock via URL post to door system
def open_door():
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
  }
  data = {
    'login': '',
    'username': 'door',
    'password': '<Password>',
    'button': 'Open Door'
  }
  response = requests.post('http://192.168.0.210/dyn', headers=headers, data=data)

# Function to Turn on LED green
def led_green():
  GPIO.output(29, GPIO.HIGH) # Turn on
  GPIO.output(31, GPIO.LOW) # Turn off

# Function to Turn on LED red
def led_red():
  GPIO.output(29, GPIO.LOW) # Turn off
  GPIO.output(31, GPIO.HIGH) # Turn on

# Function to Turn off LED
def led_off():
  GPIO.output(29, GPIO.LOW) # Turn off
  GPIO.output(31, GPIO.LOW) # Turn off

# Read the config file and store in memory
with open('rfid-door-lock.json') as f:
  data = json.load(f)

# Enable & configure logging
logging.basicConfig(filename=(data["config"]["log_file"]),level=logging.INFO,format='%(asctime)s %(levelname)s:%(message)s')

# Setup GPIO Pins for use with Bi-Colour LED
# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 29 & 31 to be an output pin and set initial value to low (off)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)

# Create RFID reader object
reader = SimpleMFRC522()

# Main Loop
try:
  while True:
    if (data["config"]["reader"] == "RC522"):
      uid = rfid_read_RC522()
    elif (data["config"]["reader"] == "PN532"):
      uid = rfid_read_PN532()
    else:
      uid = 0
    authorised = validate_access( uid, data );
    print(str(authorised))
    sleep(2);
    led_off()

except KeyboardInterrupt:
  GPIO.cleanup()
