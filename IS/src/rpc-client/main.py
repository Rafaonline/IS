import xmlrpc.client
import xml.etree.ElementTree as ET

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')


def menu():
    print("1-Consultar")
    print("2-Pesquisar")
    print("3-Sair")

def consultar():
    print("1-Lojas")
    print("2-Cidades")
    print("3-Tipos de loja")
    print("4-Categoria de clientes")
    print("5-Voltar")

def pesquisar():
    print("1- Id de transacao")
    print("2- Estacao do ano")
    print("3- Cidade da loja")
    print("4- Voltar")




while True:
    menu()

    escolha = input("Escolha a opcao: ")

    if escolha == "1":
        consultar()
        escolha_consulta = input("Escolha a opcao")

        if escolha_consulta == "1":
            """
            # Chamar a função remota para consultar lojas
            lojas = server.consultar_lojas()

            # Exibir as informações das lojas
            if lojas:
                for loja in lojas:
                    print(f"ID da Transação: {loja['transaction_id']}, ID da Loja: {loja['store_id']}")
            else:
                print("Nenhuma loja encontrada.")
            """
        #if escolha_consulta == "2":

        #if escolha_consulta == "3":

        #if escolha_consulta == "4":

        if escolha_consulta == "5":
            menu()

    elif escolha == "2":
        pesquisar()
        escolha_pesquisa = input("Escolha a opcao")

        #if escolha_pesquisa == "1":

       # if escolha_pesquisa == "2":

        #if escolha_pesquisa == "3":

        if escolha_pesquisa == "4":
            menu()
