import RPi.GPIO as GPIO
import sys, logging, json, datetime
from time import sleep
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

def led_green():
  GPIO.output(29, GPIO.HIGH) # Turn on
  GPIO.output(31, GPIO.LOW) # Turn off

def led_red():
  GPIO.output(29, GPIO.LOW) # Turn off
  GPIO.output(31, GPIO.HIGH) # Turn on

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
    uid = rfid_read();
    authorised = validate_access( uid, data );
    print(str(authorised))
    sleep(2);
    led_off()

except KeyboardInterrupt:
  GPIO.cleanup()
