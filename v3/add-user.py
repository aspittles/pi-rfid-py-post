import RPi.GPIO as GPIO
import sys, json, datetime
from time import sleep
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

# Function to Read the RFID card
def rfid_read():
  print("Hold a tag near the reader")
  uid, text = reader.read()
  return uid;

def led_green():
  GPIO.output(29, GPIO.HIGH) # Turn on
  GPIO.output(31, GPIO.LOW) # Turn off

def led_off():
  GPIO.output(29, GPIO.LOW) # Turn off
  GPIO.output(31, GPIO.LOW) # Turn off

# Setup GPIO Pins for use with Bi-Colour LED
# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 29 & 31 to be an output pin and set initial value to low (off)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)

# Create RFID reader object
reader = SimpleMFRC522()

# Read the config file and store in memory
with open('rfid-door-lock.json') as f:
  data = json.load(f)

# Main Loop
firstname = input('Enter First Name:')
lastname = input('Enter Last Name:')
keytype = input('Enter Key Type (KeyFob/KeyCard/Android/iOS):')

uid = 1080748350430
#rfid_read();

led_green()

a_dictionary = {"users": {"1234567899012": {"created": "2020-07-01 19:00:00","lastEntered": "","keyType": "KeyFob","active": True,"firstName": "Krish","lastName": "Lee"}}}

#data["users"][str(uid)]["lastEntered"] = ''
#data["users"][str(uid)]["active"] = True
#now = datetime.datetime.now()
#data["users"][str(uid)]["created"] = now.strftime("%Y-%m-%d %H:%M:%S")
#data["users"][str(uid)]["keyType"] = keytype
#data["users"][str(uid)]["firstName"] = firstname
#data["users"][str(uid)]["lastName"] = lastname

with open('rfid-door-lock.json', 'r+') as f:
  data = json.load(f)
  data.update(a_dictionary)
  f.seek(0)
  json.dump(data, f)

#with open("sample_file.json", "r+") as file:
#    data = json.load(file)
#    data.update(a_dictionary)
#    file.seek(0)
#    json.dump(data, file)


sleep(2)
led_off()

GPIO.cleanup()

#{
#  "users": {
#    "36199966818": {
#      "created": "2020-07-01 19:00:00",
#      "lastEntered": "",
#      "keyType": "Android",
#      "active": false,
#      "firstName": "Jone",
#      "lastName": "Mac"
#    }
#  }
#}
