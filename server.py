from http import client
import socket
import threading

host = '127.0.0.1' # local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clientes = []
usernames = []

def transmissao(mensagem):
    for client in clientes:
        client.send(mensagem)

def handle(client):
    while True:
        try:
            mensagem = client.recv(1024)
            transmissao(mensagem)
        except:
            index = clientes.index(client)
            clientes.remove(client)
            client.close()
            username = usernames[index]
            transmissao(f'{username} saiu do chat.'.enconde('ascii'))
            usernames.remove(username)
            break

def receber():
    while True:
        client, address = server.accept()
        print(f'Conectado com {str(address)} ')

        client.send('NICK'.encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username)
        clientes.append(client)

        print(f'Username do cliente: {username}!')
        transmissao(f'{username} entrou no chat'.encode('ascii'))
        client.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('Servidor online...')
receber()
