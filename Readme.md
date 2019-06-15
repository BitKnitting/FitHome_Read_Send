# Read the Meter and Send Readings to Firebase RT
This is an exploratory project to explore getting readings from the energy monitor over SPI and then sending the readings to a Firebase RT datastore using their REST API.
## Constraints/challenges
The Firebase RT database is set up such that anyone who knows the path can write data.  This is because we are using micropython and only explored a simple POST, which worked well.
# What is stored
In [simple_test.py](simple_test.py), we read:  
```
v1 = energy_sensor.line_voltageA
v2 = energy_sensor.line_voltageC
i1 = energy_sensor.line_currentA
i2 = energy_sensor.line_currentC
power = energy_sensor.active_power  
```
As shown in [send_reading.py](lib/send_reading.py), we then send  the reading to our Firebase RT.  An additional field - timestamp - is added.  The timestamp field is calculated by Firebase.  Thus, it is the timestamp when the data arrived at the db and not when it was sampled.  We chose to timestamp on the server side to simplify the micropython code.
# Configuration
Private configuration info is stored as JSON in the lib/config.dat file.  This file needs to be created.  It includes:  
```  
{
    "ssid":"YOUR SSID",
    "password":"YOUR PASSWORD",
    "project_id":"THE PROJECT ID OF YOUR FIRESTORE RT DB"
}  
```
# Testing the Firebase RT
## Create the database
Go to your Firebase console and create a new project. After the project is ready, go to the database section and create a Realtime Database. Select start in test mode.
## Test
Test adding readings by opening a Terminal window and sending REST commands using CURL.

Looking in the authentication area of this database, the user id for foo@gmail.com is tTDUQZWPEqhkTwFz9AYK9I5iEKa2
curl -X POST -d '{"V1" : 1233, "V2" : 1254, "I1":106, "I2":6,"P":199678}' \
  'https://iot-test-1e426.firebaseio.com/bambi/tTDUQZWPEqhkTwFz9AYK9I5iEKa2/.json'  
## Curl to HTTP Post
I found this great web page that [converts curl commands to Python  ](https://curl.trillworks.com/).  VERY HELPFUL.


