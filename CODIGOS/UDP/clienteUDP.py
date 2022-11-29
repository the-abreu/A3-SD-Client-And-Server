# ------------------
# Cliente Socket UDP
# ------------------

print('-----------------------------------------------------------')
print('|                   CLIENTE SOCKET UDP                    |')
print('-----------------------------------------------------------')

# Importando a biblioteca
import socket

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

# Definindo ip e porta
HOST = '127.0.0.1'       # Substituir pelo endereco IP do Servidor
PORT = 5000              # Porta que o Servidor ficará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)

#METÓDO PARA REALIZAR UMA NOVA VENDA
def realizarVenda():
        iterator = codOperation[0] + 1

        codOperation.insert(0, iterator)

        novaVenda = {}

        menuLojas()

        selecionarLoja = int(input('DIGITE UM NUMERO ENTRE 1 E 2 PARA UTILIZAR O MENU: ')) 
        if selecionarLoja == 1:
            novaVenda['codigo'] = codOperation[0]
            novaVenda['filial'] = "BA"
            menuFilialBa()

            selecionarVendedor = int(input('DIGITE UM NUMERO ENTRE 1 E 2 PARA UTILIZAR O MENU DE VENDEDORES: ')) 
            if selecionarVendedor == 0:
                novaVenda['vendedor'] = listaFuncionarios[selecionarVendedor]['nome']

            elif selecionarVendedor == 1:
                novaVenda['vendedor'] = listaFuncionarios[selecionarVendedor]['nome']

        elif selecionarLoja == 2:
            novaVenda['codigo'] = codOperation[0]
            novaVenda['filial'] = "SP"
            menuFilialSp()

            selecionarVendedor = int(input('DIGITE UM NUMERO ENTRE 2 E 4 PARA UTILIZAR O MENU DE VENDEDORES: ')) 
            if selecionarVendedor == 2:
                novaVenda['vendedor'] = listaFuncionarios[selecionarVendedor]['nome']

            elif selecionarVendedor == 3:
                novaVenda['vendedor'] = listaFuncionarios[selecionarVendedor]['nome']

            elif selecionarVendedor == 4:
                novaVenda['vendedor'] = listaFuncionarios[selecionarVendedor]['nome']

        menuProdutos()
        selecionarProduto = int(input('DIGITE UM NUMERO ENTRE 1 E 3 PARA SELECIONAR O PRODUTO: '))
        if selecionarProduto == 1:
            novaVenda['produto'] = "PS5"
            novaVenda['valor'] = 4000

        elif selecionarProduto == 2:
            novaVenda['produto'] = "XBOX"
            novaVenda['valor'] = 3000

        elif selecionarProduto == 3:
            novaVenda['produto'] = "NINTENDO SWITCH"
            novaVenda['valor'] = 1500

        menuPeriodo()
        selecionarPeriodo = int(input('DIGITE UM NUMERO ENTRE 1 E 12 PARA SELECIONAR O MES DA VENDA: '))
        if selecionarPeriodo == 1:
            novaVenda['codPeriodoMes'] = '1'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))            

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 2:
            novaVenda['codPeriodoMes'] = '2'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 3:
            novaVenda['codPeriodoMes'] = '3'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 4:
            novaVenda['codPeriodoMes'] = '4'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 5:
            novaVenda['codPeriodoMes'] = '5'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))            

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 6:
            novaVenda['codPeriodoMes'] = '6'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))            

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 7:
            novaVenda['codPeriodoMes'] = '7'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 8:
            novaVenda['codPeriodoMes'] = '8'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
             
        elif selecionarPeriodo == 9:
            novaVenda['codPeriodoMes'] = '9'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
            
        elif selecionarPeriodo == 10:
            novaVenda['codPeriodoMes'] = '10'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)
                        
        elif selecionarPeriodo == 11:
            novaVenda['codPeriodoMes'] = '11'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8")) 

            historicoVendas.append(novaVenda)
                        
        elif selecionarPeriodo == 12:
            novaVenda['codPeriodoMes'] = '12'
            newMensage = '\n[OK] VENDA REALIZADA COM SUCESSO: ' + str(novaVenda) 
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            historicoVendas.append(novaVenda)

        else:
            newMensage = '\n[ERRO] VENDA NAO REALIZADA! '
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))
            print('\nSELECIONE APENAS NUMEROS ENTRE 1 E 12 PROPORCIONAL AO MES')
            print('\nRETORNANDO AO MENU PRINCIPAL...\n')

#METÓDO PARA CONSULTAR VENDA POR PERIODO DE TEMPO
def consultarVendaPorPeriodo():
    menuPeriodo()

    periodoInicial = int(input('\n[PERIODO INICIAL] DIGITE O NUMERO PROPORCIONAL AO MES QUE DESEJA SELECIONAR: '))
    periodoFinal = int(input('\n[ PERIODO FINAL ] DIGITE O NUMERO PROPORCIONAL AO MES QUE DESEJA SELECIONAR: '))

    if periodoInicial < int(1) or periodoFinal > int(12):
        print('\n[ERRO] O PERIODO INICIAL NAO PODE SER MENOR DO QUE 1 E O PERIODO FINAL NÃO PODE SER MAIOR QUE 12')
    elif periodoFinal < periodoInicial:
        print('\n[ERRO] O PERIODO INICIAL NÃO PODE SER MAIOR DO QUE O PERIODO FINAL')
    else:
        totalPorPeriodo = 0
        print('\n-----------------------------------------------------------')
        print('|        TODAS AS VENDAS DO PERIODO INICIAL AO FINAL      |')
        print('-----------------------------------------------------------')

        while periodoInicial <= periodoFinal:
            for p in historicoVendas:
                if p['codPeriodoMes'] in str(periodoInicial):
                    totalPorPeriodo += p['valor']
                    print('[CODIGO: {}] NOME DO VENDEDOR: {} (FILIAL: {}) \n\nPRODUTO: {}, VALOR: R$ {}, MES DA VENDA: {}'.format(p['codigo'], p['vendedor'], p['filial'], p['produto'], p['valor'], p['codPeriodoMes'] ))
                    print('-----------------------------------------------------------')
            periodoInicial+= 1

        print('               TOTAL POR PERIODO FOI: R$', totalPorPeriodo  )
        print('-----------------------------------------------------------')

    print('\nRETORNANDO AO MENU PRINCIPAL...\n')   

#METÓDO PARA CONSULTAR TODAS AS VENDAS
def consultarVenda():

        print('\n-----------------------------------------------------------')
        print('|                    TODAS AS VENDAS                      |')
        print('-----------------------------------------------------------')

        for p in historicoVendas:
            print('[CODIGO: {}] NOME DO VENDEDOR: {} (FILIAL: {}) \n\nPRODUTO: {}, VALOR: R$ {}, MES DA VENDA: {}'.format(p['codigo'], p['vendedor'], p['filial'], p['produto'], p['valor'], p['codPeriodoMes'] ))
            print('-----------------------------------------------------------')

        print('|                    FIM DA CONSULTA                      |')
        print('-----------------------------------------------------------\n')

        print('RETORNANDO AO MENU PRINCIPAL...\n')

#METÓDO PARA CONSULTAR O TOTAL DE VENDAS DE UM VENDEDOR
def consultarTotalVendasVendedor():

    nomeDoVendedor = str(input('\nINFORME O NOME DO VENDEDOR PARA RETORNAR O TOTAL DE VENDAS DO MESMO: ').upper())

    if nomeDoVendedor == 'LEVI':
        somaDoVendedor = 0
        for v in historicoVendas:
            if v['vendedor'] in 'LEVI':
                somaDoVendedor += v['valor']

        print('\nO TOTAL DE VENDAS DO VENDEDOR {} FOI: R$ {} '.format(dadosFuncionarios2['nome'], somaDoVendedor))

    elif nomeDoVendedor == 'RENAN':
        somaDoVendedor = 0
        for v in historicoVendas:
            if v['vendedor'] in 'RENAN':
                somaDoVendedor += v['valor']

        print('\nO TOTAL DE VENDAS DO VENDEDOR {} FOI: R$ {} '.format(dadosFuncionarios['nome'], somaDoVendedor))

    elif nomeDoVendedor == 'CLEISON':
        somaDoVendedor = 0
        for v in historicoVendas:
            if v['vendedor'] in 'CLEISON':
                somaDoVendedor += v['valor']

        print('\nO TOTAL DE VENDAS DO VENDEDOR {} FOI: R$ {} '.format(dadosFuncionarios4['nome'], somaDoVendedor))

    elif nomeDoVendedor == 'BRUNO':
        somaDoVendedor = 0
        for v in historicoVendas:
            if v['vendedor'] in 'BRUNO':
                somaDoVendedor += v['valor']

        print('\nO TOTAL DE VENDAS DO VENDEDOR {} FOI: R$ {} '.format(dadosFuncionarios3['nome'], somaDoVendedor) + '\n')

    elif nomeDoVendedor == 'LEONARDO':
        somaDoVendedor = 0
        for v in historicoVendas:
            if v['vendedor'] in 'LEONARDO':
                somaDoVendedor += v['valor']

        print('\nO TOTAL DE VENDAS DO VENDEDOR {} FOI: R$ {} '.format(dadosFuncionarios5['nome'], somaDoVendedor))

    else:
        print('\n[ERRO] VENDEDOR NAO EXISTE! PROCURE POR UM DOS VENDEDORES CADASTRADOS!\n')
    menuPrincipal()

#METÓDO PARA CONSULTAR O TOTAL DE VENDAS DE UMA LOJA
def consultarTotalVendasLoja():
    menuLojas()

    print('\nOBS: VOCE DEVE DIGITAR APENAS BA OU SP')

    nomeDoFilial = str(input('\nINFORME A IDENTIFICACAO DA LOJA PARA RETORNAR O TOTAL DE VENDAS DA MESMA: ').upper())

    if nomeDoFilial == 'BA':
        totalDaFilial = 0
        for f in historicoVendas:
            if f['filial'] in 'BA':
                totalDaFilial += f['valor']

        print('\nO TOTAL DE VENDAS DA LOJA FILIAL {} FOI: R$ {} '.format(dadosFuncionarios['filial'], totalDaFilial))

    elif nomeDoFilial == 'SP':
        totalDaFilial = 0
        for f in historicoVendas:
            if f['filial'] in 'SP':
                totalDaFilial += f['valor']

        print('\nO TOTAL DE VENDAS DA LOJA FILIAL {} FOI: R$ {} '.format(dadosFuncionarios3['filial'], totalDaFilial))

    else:
        print('\n[ERRO] FILIAL INEXISTENTE! PROCURE DIGITANDO APENAS POR "BA" OU "SP"!')

    print('\nRETORANDO AO MENU PRINCIPAL...')

#METÓDO PARA CONSULTAR O MELHOR VENDEDOR
def consultarMelhorVendedor():
    print('\n-----------------------------------------------------------')
    print('|            TOTAL DE VENDAS DE CADA VENDEDOR             |')
    print('-----------------------------------------------------------')

    totalVendedorRenan = 0
    totalVendedorLevi = 0
    totalVendedorBruno =     0
    totalVendedorCleison = 0
    totalVendedorLeonardo = 0
    for v in historicoVendas:
        if v['vendedor'] in 'RENAN':
            totalVendedorRenan += v['valor']

        if v['vendedor'] in 'LEVI':
            totalVendedorLevi += v['valor']

        if v['vendedor'] in 'BRUNO':
            totalVendedorBruno += v['valor']

        if v['vendedor'] in 'CLEISON':
            totalVendedorCleison += v['valor']

        if v['vendedor'] in 'LEONARDO':
            totalVendedorLeonardo += v['valor']

    print(' (FILIAL: BA)       VENDEDOR RENAN:            R$', totalVendedorRenan)
    print(' (FILIAL: BA)       VENDEDOR LEVI:             R$', totalVendedorLevi)
    print(' (FILIAL: SP)       VENDEDOR BRUNO:            R$', totalVendedorBruno)
    print(' (FILIAL: SP)       VENDEDOR CLEISON:          R$', totalVendedorCleison)
    print(' (FILIAL: SP)       VENDEDOR LEONARDO:         R$', totalVendedorLeonardo)

    print('-----------------------------------------------------------')
    print('|               RESULTADO DO MELHOR VENDEDOR              |')

    if totalVendedorRenan > totalVendedorLevi and totalVendedorRenan > totalVendedorBruno and totalVendedorRenan > totalVendedorCleison and totalVendedorRenan > totalVendedorLeonardo:
        print('-----------------------------------------------------------')
        print('|                 MELHOR VENDEDOR: RENAN                  |')
        print('-----------------------------------------------------------')
    elif totalVendedorLevi > totalVendedorRenan and totalVendedorLevi > totalVendedorBruno and totalVendedorLevi > totalVendedorCleison and totalVendedorLevi > totalVendedorLeonardo:
        print('-----------------------------------------------------------')
        print('|                 MELHOR VENDEDOR: LEVI                  |')
        print('-----------------------------------------------------------')
    elif totalVendedorBruno > totalVendedorRenan and totalVendedorBruno > totalVendedorLevi and totalVendedorBruno > totalVendedorCleison and totalVendedorBruno > totalVendedorLeonardo:
        print('-----------------------------------------------------------')
        print('|                 MELHOR VENDEDOR: BRUNO                  |')
        print('-----------------------------------------------------------')
    elif totalVendedorCleison > totalVendedorRenan and totalVendedorCleison > totalVendedorLevi and totalVendedorCleison > totalVendedorBruno and totalVendedorCleison > totalVendedorLeonardo:
        print('-----------------------------------------------------------')
        print('|                MELHOR VENDEDOR: CLEISON                 |')
        print('-----------------------------------------------------------')
    else:
        print('-----------------------------------------------------------')
        print('|               MELHOR VENDEDOR: LEONARDO                 |')
        print('-----------------------------------------------------------')

    print('\nRETORNANDO AO MENU PRINCIPAL...\n')

#METÓDO PARA CONSULTAR A MELHOR LOJA
def consultarMelhorLoja():
    print('\n-----------------------------------------------------------')
    print('|              TOTAL DE VENDAS DE CADA LOJA               |')
    print('-----------------------------------------------------------')

    totalVendasBa = 0
    totalVendasSp = 0
    for f in historicoVendas:
        if f['filial'] in 'BA':
            totalVendasBa += f['valor']

        if f['filial'] in 'SP':
            totalVendasSp += f['valor']
    print('TOTAL DE VENDAS DA FILIAL BA:              R$', totalVendasBa)
    print('TOTAL DE VENDAS DA FILIAL SP:              R$', totalVendasSp)

    print('-----------------------------------------------------------')
    print('|                RESULTADO DO MELHOR LOJA                 |')

    if totalVendasBa > totalVendasSp:
        print('-----------------------------------------------------------')
        print('|                    MELHOR LOJA: BA                      |')
        print('-----------------------------------------------------------')  
    else:
        print('-----------------------------------------------------------')
        print('|                    MELHOR LOJA: SP                      |')
        print('-----------------------------------------------------------')   

    print('\nRETORNANDO AO MENU PRINCIPAL...\n')                

#METÓDO EXIBIR O MENU COM OS PRODUTOS
def menuProdutos():

        print('PARA SELECIONAR UM DOS PRODUTOS, DIGITE UM DOS CODIGOS ABAIXO: ')

        print('-----------------------------------------------------------')
        print('|                    MENU DE PRODUTOS                     |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [1] PS5                    (VALOR: R$ 4.000,00)         |')
        print('| [2] XBOX                   (VALOR: R$ 3.000,00)         |')
        print('| [3] NINTENDO SWITCH        (VALOR: R$ 1.500,00)         |')
        print('|                                                         |')
        print('-----------------------------------------------------------')

#METÓDO EXIBIR O MENU COM OS PERIODOS
def menuPeriodo():
        print('\nPARA SELECIONAR UM DOS MESES, DIGITE UM DOS CODIGOS ABAIXO: ')

        print('-----------------------------------------------------------')
        print('|                     SELECIONE O MES                     |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [1] JANEIRO                       [7]  JULHO            |')
        print('| [2] FEVEREIRO                     [8]  AGOSTO           |')
        print('| [3] MARCO                         [9]  SETEMBRO         |')
        print('| [4] ABRIL                         [10] OUTUBRO          |')
        print('| [5] MAIO                          [11] NOVEMBRO         |')
        print('| [6] JUNHO                         [12] DEZEMBRO         |')
        print('|                                                         |')
        print('-----------------------------------------------------------') 

#METÓDO EXIBIR O MENU COM AS LOJAS
def menuLojas():
        print('\nPARA UTILIZAR O SISTEMA ABAIXO, SELECIONE UMA DAS LOJAS: \n')

        print('-----------------------------------------------------------')
        print('|                     MENU DE LOJAS                       |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [1] FILIAL DA BAHIA                                     |')
        print('| [2] FILIAL DE SÃO PAULO                                 |')
        print('|                                                         |')
        print('-----------------------------------------------------------')

#METÓDO EXIBIR O MENU COM OS VENDEDORES DA FILIAL BA
def menuFilialBa():
        print('\nPARA SELECIONAR UM DOS VENDEDORES, DIGITE UM DOS CODIGOS ABAIXO: \n')

        print('-----------------------------------------------------------')
        print('|                    MENU DE VENDEDORES                   |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [0] RENAN                                               |')
        print('| [1] LEVI                                                |')
        print('|                                                         |')
        print('-----------------------------------------------------------')

#METÓDO EXIBIR O MENU COM OS VENDEDORES DA FILIAL SP
def menuFilialSp():
        print('PARA SELECIONAR UM DOS VENDEDORES, DIGITE UM DOS CODIGOS ABAIXO: ')

        print('-----------------------------------------------------------')
        print('|                    MENU DE VENDEDORES                   |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [2] BRUNO                                               |')
        print('| [3] CLEISON                                             |')
        print('| [4] LEONARDO                                            |')
        print('|                                                         |')
        print('-----------------------------------------------------------')

#METÓDO EXIBIR O MENU DO VENDEDOR
def menuVendedor():
        print('\nVOCÊ ESCOLHEU A OPÇÃO: [1] VENDEDOR\n')

        print('-----------------------------------------------------------')
        print('|                    MENU DO VENDEDOR                     |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [1] REALIZAR NOVA VENDA                                 |')
        print('| [2] VOLTAR PARA O MENU PRINICIPAL                       |')
        print('|                                                         |')
        print('-----------------------------------------------------------')
        
        opcoesMenuVendedor = int(input('\nDIGITE UM NUMERO ENTRE 1 E 2 PARA UTILIZAR O MENU DO VENDEDOR: '))

        if opcoesMenuVendedor == 1:
            realizarVenda()

            menuPrincipal()

        elif opcoesMenuVendedor == 2:
            menuPrincipal()

        else:
            print('\n[ERRO] SELECIONE UMAS DAS OPCOES DE 1 A 2 PARA USAR O MENU DO VENDEDOR')
            menuVendedor()

#METÓDO EXIBIR O MENU DO GERENTE
def menuGerente():

        print('\nVOCÊ ESCOLHEU A OPÇÃO: [2] GERENTE\n')
        
        print('-----------------------------------------------------------')
        print('|                     MENU DO GERENTE                     |')
        print('-----------------------------------------------------------')
        print('|                                                         |')
        print('| [1] CONSULTAR TODAS AS VENDAS                           |')
        print('| [2] CONSULTAR TOTAL DE VENDAS DE UM VENDEDOR            |')
        print('| [3] CONSULTAR TOTAL DE VENDAS DE UMA LOJA               |')
        print('| [4] CONSULTAR QUAL O MELHOR VENDEDOR                    |')
        print('| [5] CONSULTAR QUAL O MELHOR LOJA                        |')
        print('| [6] CONSULTAR TOTAL DE VENDAS POR PERIODO               |')
        print('| [7] VOLTAR PARA O MENU PRINICIPAL                       |')
        print('|                                                         |')
        print('-----------------------------------------------------------')
        
        opcoesMenuGerente = int(input('\nDIGITE UM NUMERO ENTRE 1 E 7 PARA UTILIZAR O MENU DO GERENTE: '))
        if opcoesMenuGerente == 1:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 1 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarVenda()
            menuPrincipal()

        elif opcoesMenuGerente == 2:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 2 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarTotalVendasVendedor()
            menuPrincipal()

        elif opcoesMenuGerente == 3:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 3 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarTotalVendasLoja()
            menuPrincipal()

        elif opcoesMenuGerente == 4:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 4 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarMelhorVendedor()
            menuPrincipal()

        elif opcoesMenuGerente == 5:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 5 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarMelhorLoja()
            menuPrincipal()

        elif opcoesMenuGerente == 6:
            newMensage = '\n[OK] CONSULTA DE CODIGO N° 6 AUTORIZADA'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            consultarVendaPorPeriodo()
            menuPrincipal()

        elif opcoesMenuGerente == 7:
            menuPrincipal()

        else:
            newMensage = '\n[ERRO] SOLICITACAO ENVIADA COM DADOS INCORRETOS'
		    #Enviando mensagem ao servidor			
            cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		    #Recebendo resposta do servidor
            msg, endereco = cliente.recvfrom(9000)
            print(msg.decode("utf-8"))

            print('\nSELECIONE ENTRE AS OPCOES DE 1 A 7 PARA UTILIZAR O MENU DO GERENTE')
            menuGerente()              

#METÓDO CHAMAR O SUB-MENU A PARTIR DO MENU PRINCIPAL
def subMenu():
	mensagem = int(input('DIGITE UM NUMERO ENTRE 1 E 3 PARA UTILIZAR O MENU: '))

	while (mensagem != 3):
		if mensagem == 1:
			newMensage = '\n[OK] ACESSO CONCEDIDO AO VENDEDOR'
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
			cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
			msg, endereco = cliente.recvfrom(9000)
			print(msg.decode("utf-8"))			

			menuVendedor()

		elif mensagem == 2:
			newMensage = '\n[OK] ACESSO CONCEDIDO AO GERENTE'
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
			cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
			msg, endereco = cliente.recvfrom(9000)
			print(msg.decode("utf-8"))		
									
			menuGerente()

		else:
			newMensage = '[ERRO]'
		# Enviando mensagem ao servidor			
			#print("... Vou mandar uma mensagem para o servidor")
			cliente.sendto(newMensage.encode("utf-8"), enderecoServidor)

		# Recebendo resposta do servidor
			msg, endereco = cliente.recvfrom(9000)
			print(msg.decode("utf-8"))		
			print('\nSELECIONE ENTRE AS OPCOES DE 1 A 3 PARA UTILIZAR O SISTEMA!')
			menuPrincipal()

	print('\nVOCÊ ESCOLHEU A OPÇÃO: [3] SAIR\n')
	print('ENCERRANDO O SISTEMA...\n')
	print("ENCERRANDO CONEXAO COMO CLIENTE...\n")
	cliente.close()

#METÓDO EXIBIR O MENU PRINCIPAL		
def menuPrincipal():
    print('-----------------------------------------------------------')
    print('|                     MENU PRINCIPAL                      |')
    print('-----------------------------------------------------------')
    print('|                                                         |')
    print('| [1] VENDEDOR                                            |')
    print('| [2] GERENTE                                             |')
    print('| [3] SAIR                                                |')
    print('|                                                         |')
    print('-----------------------------------------------------------\n')
    subMenu()

menuPrincipal()
