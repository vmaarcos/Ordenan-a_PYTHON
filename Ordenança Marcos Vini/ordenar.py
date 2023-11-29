import random

# Script para exibir 
def exibir_ordem_decrescente(valores, sites):
    valores_ordenados = sorted(zip(valores, sites), key=lambda x: x[0], reverse=True) #funcao sorted para ordenar os valores, zip para juntar os valores e sites, key para ordenar os valores, reverse para ordenar em ordem decrescente espero q entendam o ufoi idiota 
    for valor, site in valores_ordenados:
        print(f"Site: {site['Nome']}, Pontos: {valor}") #F string para exibir o nome do site e os pontos 
        print(f"Informações Vazadas: ")
        print(f"  - CPF: {site['CPF']}")
        print(f"  - RG: {site['RG']}")
        print(f"  - E-mail: {site['Email']}")
        print(f"  - Senha: {site['Senha']}")
        print()

#   
nome_usuario = input("Informe o seu email aqui meu bom: ")

# Info ja prontas preguiça de ficar digitando
sites = [
    {"Nome": "Kalli Linux", "CPF": "123.456.789-00", "RG": "987654321", "Email": "kalli@linux.com", "Senha": "kalli123"},
    {"Nome": "PicPay", "CPF": "987.654.321-00", "RG": "123456789", "Email": "picpay@example.com", "Senha": "picpay456"},
    {"Nome": "Proa.org", "CPF": "111.222.333-44", "RG": "555666777", "Email": "proa@org.org", "Senha": "proa123"}
]

# funcao random 
def gerar_pontos():
    return random.randint(1, 10)

# Calculo
valores = []
for site in sites:
    pontos = gerar_pontos()
    valores.append(pontos)

print("\nPontos em ordem decrescente:") #o /n é para pular uma linha
exibir_ordem_decrescente(valores, sites)
