import socket
from main import calcolaBWT

HOST = "127.0.0.1"
PORT = 2027

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#usiamo gli indirizzi ip IPv4 standard e il protocollo FTP
server.bind((HOST, PORT))#collego il socket all indirizzo e alla porta scelti
server.listen(1)#server in ascolto
print("Server in attesa di connessione...")
conn, addr = server.accept()#il server restituisce il canale di comunicazione, l'ip e la porta
print("Connesso con:", addr)
parola = conn.recv(1024).decode()# ricevo i byte dal client e li ritrasformo in stringa
print("Parola ricevuta:", parola)
risultato = calcolaBWT(parola)
conn.send(str(risultato).encode()) # trasformo la lista in stringa, poi in byte e la mando al client
conn.close() 
server.close()
