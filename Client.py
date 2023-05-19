# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import socket
import json

HOST = 'host do Pedro'
PORT = 4598

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Envia uma mensagem para o servidor
message = 'Solicitação do cliente'
client_socket.send(message.encode())

# Recebe a resposta do servidor
response = client_socket.recv(1024).decode()

response_obj = json.loads(response)

print('Resposta recebida do servidor:', response_obj)

# Fechada a conexão com o servidor
client_socket.close()
