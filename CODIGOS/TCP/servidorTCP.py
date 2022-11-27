# -------------------
# Servidor Socket TCP
# -------------------

# importando a biblioteca
import socket
class Dados():
	codOperation = [0]

	dadosFuncionarios = {}
	dadosFuncionarios['nome'] = "RENAN"
	dadosFuncionarios['idade'] = "21"
	dadosFuncionarios['filial'] = "BA"

	dadosFuncionarios2 = {}
	dadosFuncionarios2['nome'] = "LEVI"
	dadosFuncionarios2['idade'] = "19"
	dadosFuncionarios2['filial'] = "BA"

	dadosFuncionarios3 = {}
	dadosFuncionarios3['nome'] = "BRUNO"
	dadosFuncionarios3['idade'] = "19"
	dadosFuncionarios3['filial'] = "SP"

	dadosFuncionarios4 = {}
	dadosFuncionarios4['nome'] = "CLEISON"
	dadosFuncionarios4['idade'] = "19"
	dadosFuncionarios4['filial'] = "SP"

	dadosFuncionarios5 = {}
	dadosFuncionarios5['nome'] = "LEONARDO"
	dadosFuncionarios5['idade'] = "18"
	dadosFuncionarios5['filial'] = "SP"

	listaFuncionarios = [dadosFuncionarios, dadosFuncionarios2, dadosFuncionarios3, dadosFuncionarios4, dadosFuncionarios5]

	vendasRealizadas = {}
	vendasRealizadas['codigo'] = 0
	vendasRealizadas['filial'] = "BA"
	vendasRealizadas['vendedor'] = "RENAN"
	vendasRealizadas['produto'] = "PS5"
	vendasRealizadas['valor'] = 4000
	vendasRealizadas['codPeriodoMes'] = '11'

	historicoVendas = [vendasRealizadas]

	print("Eu sou o SERVIDOR TCP!")

# definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORT))

# servidor escutando (aguardando cliente)
servidor.listen()
print("Aguardando cliente...")

# cliente conectou - recuperando informações do cliente
conexaoCliente, enderecoCliente = servidor.accept()
print(f"Cliente {enderecoCliente} conectou.")

# conversando com o cliente
while (True):
	# recebendo dados
	dados = conexaoCliente.recv(1024)
	# testando dados enviados
	if (not dados):
		# encerrando conexão e saindo do loop
		print ("Encerrando a conexão...")
		conexaoCliente.close()
		break
	# respondendo ao cliente
	mensagem = str(dados.decode("utf-8"))
	print("-----")
	print(f"Mensagem enviada pelo cliente: {mensagem}")
	print(f"Este servidor vai devolver a mensagem ao cliente {enderecoCliente}")
	resposta = "\nRESPOSTA DO SERVIDOR: " + mensagem
	conexaoCliente.sendall(resposta.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")
