import csv

dados = [
    ["Nome", "Idade"],
    ["Antonio", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Eduardo", 28],
    ["Fabricio", 35]
]

with open('dados.csv', 'w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados)

dados_lista = []

with open('dados.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        dados_lista.append(linha)

def verificar_nome(nome_digitado):
    for pessoa in dados_lista[1:]:
        nome, idade = pessoa
        idade = int(idade)

        if nome.lower() == nome_digitado.lower():
            idade_mais_velha = max(int(d[1]) for d in dados_lista[1:])
            if idade == idade_mais_velha:
                return f"{nome} tem {idade} anos, é a pessoa mais velha da lista."
            else:
                return f"{nome} tem {idade} anos, não é a pessoa mais velha da lista."

    return "Nome não encontrado."

nome_usuario = input("Digite um nome: ")

resultado = verificar_nome(nome_usuario)

print(resultado)