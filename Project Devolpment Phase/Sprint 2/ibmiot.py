import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "lryrya"
deviceType = "Gas_Sensor"
deviceId = "G1"
authMethod = "token"
authToken = "123456789"
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="lighton":
        print ("led is on")
    else :
        print ("led is off")
#print(cmd)
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
        #Get Sensor Data from DHT11
        
        NO2=random.randint(0,30)
        CO2=random.randint(0,25)
        CO=random.randint(0,5)
        
        data = { 'Nitrogen Di Oxide' : NO2 , 'Carbon di Oxide': CO2,'Carbon monooxide' : CO}
        #print data
        def myOnPublishCallback():
            print ("Published Nitrogen di Oxide = %s C" % NO2, "Carbon di oxide = %s %%" % CO2, "Carbon monoxide = %s %%" % CO2, "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
deviceCli.disconnect()
