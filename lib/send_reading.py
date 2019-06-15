import network
import urequests as requests
from wifi_connect import do_connect
import ujson as json

CONFIG_FILE = 'lib/config.dat'



class SendReading:
    def __init__(self,device_name,userID):
       self.device_name = device_name
       self.userID = userID
        # Log into wifi
       with open(CONFIG_FILE) as f:
         lines = f.readlines()
         config_vars = json.loads(lines[0])
         self.ssid = config_vars['ssid']
         self.password = config_vars['password']
         self.project_id = config_vars['project_id']
         print('ssid: {}...password: {}.....project ID: {}'.format(self.ssid,self.password,self.project_id))
         
    def send_reading(self, v1, v2, i1, i2, power):
        do_connect(self.ssid, self.password)
        # .sv timestamp: http://bit.ly/2MO0XNt
        #data = '{'+'"V1":{},"V2":{},"I1":{},"I2":{},"P":{},".sv":"timestamp"'.format(v1,v2,i1,i2,power) +'}'
        data = '{'+'"V1":{},"V2":{},"I1":{},"I2":{},"P":{}'.format(v1,v2,i1,i2,power) +',"timestamp": {".sv":"timestamp"}}'
        print(data)
        path = 'https://iot-test-1e426.firebaseio.com/'+self.device_name+'/'+self.userID+'/.json'
        print(path)
        response = requests.post(path, data=data)
        print('response: {}'.format(response.text))











