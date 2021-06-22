#! /usr/bin/env python
from time import sleep
import snap7
from snap7.util import *
import struct

plc = snap7.client.Client()
plc.connect("127.0.0.1",0,1)

area = 0x82    # area for Q memory in 
start = 0      # location we are going to start the read
length = 1     # length in bytes of the read
bit = 0        # which bit in the Q memory byte we are reading

byte = plc.read_area(area,0,start,length)
print ("Q0.0:",get_bool(mbyte,0,bit))
plc.disconnect()