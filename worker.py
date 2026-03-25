#cliente 
from multiprocessing.connection import Client
conn = Client(('localhost', 6000), authkey=b'contrasena')
conn.send("hola k ase")
respuesta = conn.recv()
print(respuesta)
conn.close()