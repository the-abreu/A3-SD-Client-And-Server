# (A3) Sistemas Distribuídos: Cliente e Servidor

## Apresentação
Esse projeto foi realizado pelos alunos da turma de Sistemas Distribuídos do turno noturno da UNIFACS (Nomes e RA's dos alunos no arquivo PDF)

## Descrição
Este projeto possui o propósito de realizar um sistema que possua um cliente que se comunique com o servidor, o sistema é orientado aos protocolos TCP e UDP (Neste repositório você encontrará duas pastas, uma para cada protocolo)

## Pré-Requisitos
* Possuir em sua máquina a linguagem Python instalada;
* Possuir instalado em sua máquina uma IDE, como o VsCode ou PyCharm (Onde você pode abrir os arquivos e ler o código);
* Clonar este repositório em sua máquina:

HTTPS:
```
git clone https://github.com/the-abreu/A3-SD-Client-And-Server.git
```

## Como manusear o sistema
* Após realizar o Clone ou Download deste repositório, escolha entre a pasta TCP e UDP;
* Independente da pasta que você escolher, inicie executando o arquivo do SERVIDOR que irá aguardar a conexão ou mensagem do CLIENTE (que é o segundo arquivo que você deve executar)

## Introdução as funcionalidades do sistema
Ao executar corretamente o arquivo do servidor e do cliente, você irá se deparar no terminal do Cliente a opção de operar como VENDEDOR ou como GERENTE. Segue abaixo o que cada um pode realizar no sistema:

![menu](https://user-images.githubusercontent.com/96211934/204113855-5968d13f-75f6-49b3-a6f6-22cc49093337.png)


<details open>
  <summary>
    <b>Vendedor</b>
  </summary>
  
  ![vendedor](https://user-images.githubusercontent.com/96211934/204113805-e90e2ad1-1b3d-4149-a30b-7739a51ba992.png)

- Funcionalidade: A partir do código de N° 1 você poderá iniciar uma nova venda

- Obs: Para realizar uma venda, é necessário que antes escolha qual filial você está operando, quem é o vendedor da filial, o produto (o valor é atribuído automaticamente) e o mês em que realizou a venda.
</details>

<details open>
  <summary>
    <b>Gerente</b>
  </summary>
  
  ![gerente](https://user-images.githubusercontent.com/96211934/204113786-c907190d-2f69-42da-96ae-5f277d099f1e.png)


- Funcionalidade: A partir do código de N° 1 você poderá consultar todas as vendas;
- Funcionalidade: A partir do código de N° 2 você poderá consultar o total de vendas realizadas por um vendedor;
- Funcionalidade: A partir do código de N° 3 você poderá consultar o total de vendas realizadas por uma das lojas;
- Funcionalidade: A partir do código de N° 4 você poderá consultar quem foi o melhor vendedor;
- Funcionalidade: A partir do código de N° 5 você poderá consultar qual foi a melhor loja;
- Funcionalidade: A partir do código de N° 6 você poderá consultar o total de vendas por período, escolhendo o mês inicial e o mês final para iniciar a consulta;

- Obs: Para utilizar a funcionalidade de N° 2 é necessário escrever o nome do vendedor, você pode escrever o primeiro nome de qualquer um dos integrantes do grupo deste projeto, como: Renan, Levi, Bruno, Cleison e Leonardo.
</details>
