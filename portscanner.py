import sys
import socket

ipAddress = sys.argv[1]

for portas in range (1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s.connect_ex((ipAddress, portas)) == 0:
        print(f"Portas {portas} estão abertas")
        s.close()
