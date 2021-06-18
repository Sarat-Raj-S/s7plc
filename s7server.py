import snap7
from snap7.util import *
import time

server = snap7.server.Server()
# size = 100
# data = (snap7.types.wordlen_to_ctypes[snap7.types.S7WLByte] * size)()
# data[0] = 5
# server.register_area(snap7.types.srvAreaDB, 1, data)
# server.start()
# while True:
#     while True:
#         event = server.pick_event()
#         if event:
#             print(server.event_text(event))
#         else:
#             break
#         time.sleep(.01)
# server.stop()
# server.destroy()