#servidor
from multiprocessing.connection import Listener
listener = Listener(('localhost', 6000), authkey=b'contrasena')
conn = listener.accept()
data = conn.recv()
conn.send(data.upper())
conn.close()