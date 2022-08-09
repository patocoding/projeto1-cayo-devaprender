import socket
import threading

username = input('Escolha seu username: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receber():
    while True:
        try:
            mensagem = client.recv(1024).decode('ascii')
            if mensagem == 'NICK':
                client.send(username.encode('ascii'))
            else:
                print(mensagem)
        except:
            print('Ocorreu um erro!')
            client.close()
            break

def escrever():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii'))

receber_thread = threading.Thread(target = receber)
receber_thread.start()

escrever_thread = threading.Thread(target = escrever)
escrever_thread.start()
        
