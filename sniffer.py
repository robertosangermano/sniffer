import os
from socket import socket
# host sul quale ascoltare
host = "192.161.0.196"
#creare un socket raw e assegnalo all'interfaccia pubblica
if  os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
         socket_protocol = socket.IPPROTO_ICMP
sniffer= socket.socket (socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host,0))
# vogliamo l'handler IP nella cattura
sniffer.setsockopt (socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# se usiamo windows  dobbiamo spedire un IOCTL
# per impostare la modalità promiscua
if  os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.rRCVALL_ON)
# leggi un singolo pacchettosocket.
    printsniffer.recvfrom(65565)
# se siamo su windows, disabilitiamo la modalità promisqua
if os.name ==  "nt":
    sniffer.ioctl (socket.SIO_RCVALL, socket.rRCVALL_Off )
    