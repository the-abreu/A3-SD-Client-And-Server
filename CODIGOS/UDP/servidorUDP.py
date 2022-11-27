# -------------------
# Servidor Socket UDP
# -------------------

# importando a biblioteca
import socket

print("\nEu sou o SERVIDOR UDP!")

# definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 5000              # Porta que o Servidor ficará escutando


# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print("\nAguardando cliente...\n")

while (True):
	print("-----")
	# cliente conectou - recuperando informações do cliente
	msg, enderecoCliente = servidor.recvfrom(9000)
	print(f"Cliente {enderecoCliente} enviou mensagem")
	mensagem = msg.decode("utf-8")
	print(f"Mensagem enviada pelo cliente: {mensagem}")
	print(f"Este servidor vai devolver a mensagem ao cliente {enderecoCliente}")
	resposta = "\nRESPOSTA DO SERVIDOR: " + mensagem
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
	if (mensagem == "adeus"):
		# Fim da conversa. Servidor vai encerrar.
		break

print("Encerrando o servidor...")
servidor.close()
