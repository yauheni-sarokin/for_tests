import pyOSC3
import time, random
client = pyOSC3.OSCClient()
client.connect( ( '127.0.0.1', 57110 ) )
msg = pyOSC3.OSCMessage()
msg.setAddress("/print")
msg.append(400)
client.send(msg)