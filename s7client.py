import snap7
client = snap7.client.Client()
client.connect("127.0.0.1", 0, 0, 1012)
client.get_connected()
data = client.db_read(1, 0, 4)
bytearray(b"\x00\x00\x00\x00")
data[3] = 0b00000001
bytearray(b'\x00\x00\x00\x01')
data.db_write(1, 0, data)