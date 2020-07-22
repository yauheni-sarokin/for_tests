import OSC
import time, random

if __name__ == "__main__":
    client = OSC.OSCClient()
    client.connect(("127.0.0.1", 57120))
    msg = OSC.OSCMessage()
    msg.setAddress("/print")
    msg.append(600)
    client.send(msg)