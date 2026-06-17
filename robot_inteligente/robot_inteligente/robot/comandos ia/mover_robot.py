import socket
import time
import sys

ROBOT_IP   = "192.168.X.X"  # ← cambia por la IP del carro
ROBOT_PORT = 4000

comandos = {
    "adelante":  "CMD_MOTOR#2500#2500#2500#2500\n",
    "atras":     "CMD_MOTOR#-2500#-2500#-2500#-2500\n",
    "izquierda": "CMD_MOTOR#-2500#-2500#2500#2500\n",
    "derecha":   "CMD_MOTOR#2500#2500#-2500#-2500\n",
    "parar":     "CMD_MOTOR#0#0#0#0\n"
}

direccion = sys.argv[1] if len(sys.argv) > 1 else "parar"
duracion  = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ROBOT_IP, ROBOT_PORT))
    s.sendall(comandos.get(direccion, comandos["parar"]).encode())
    time.sleep(duracion)
    s.sendall(comandos["parar"].encode())

print(f"✅ Robot movido {direccion} por {duracion} segundos")