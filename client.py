import socket

HOST = "127.0.0.1"
PORT = 2027

parola = input("inserisci la parola da codificare: ").lower()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creo il socket con IPv4 e protocollo TCP
client.connect((HOST, PORT)) # mi collego al server usando l indirizzo e la porta
client.send(parola.encode())  # trasformo la parola in byte e la mando al server
risposta = client.recv(1024).decode() # ricevo i byte della risposta e li ritrasformo in stringa
print("Trasformata BWT ricevuta:", risposta)
client.close()
