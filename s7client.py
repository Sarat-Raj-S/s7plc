#! /usr/bin/env python
from time import sleep
import snap7
from snap7.util import *
import struct
plc = snap7.client.Client()
plc.connect("127.0.0.1",0,1)    
byte = plc.read_area(0x82,0,0,1)
print ("Q0.0:",get_bool(mbyte,0,0))
plc.disconnect()