import socket
import json

HOST = 'host do Pedro'
PORT = 4598

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Servidor pronto para receber conexões.')

# Aguarda as conexões dos clientes
while True:
    client_socket, addr = server_socket.accept()
    print('Conexão estabelecida com', addr)

    request = client_socket.recv(1024).decode()
    print('Mensagem recebida do cliente:', request)

    response_dict = {'message': 'Resposta do servidor'}

    response_json = json.dumps(response_dict)

    client_socket.send(response_json.encode())

# Fechada a conexão com o cliente
    client_socket.close()
