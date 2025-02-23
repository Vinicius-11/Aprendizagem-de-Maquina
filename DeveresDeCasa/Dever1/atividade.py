import csv
from datetime import datetime

dados = [
    ["Neymar Junior", "1992-02-05", "2025-02-19", "14:30"],
    ["Vinicius Junior", "2000-07-12", "2025-02-19", "09:15"],
    ["Lionel Messi", "1987-06-24", "2025-02-20", "11:45"],
    ["Cristiano Ronaldo", "1985-02-05", "2025-02-20", "17:00"],
    ["Gabriel Barbosa", "1996-08-30", "2025-02-21", "08:00"]
]

nome_arquivo = "dados.csv"

# Criando o arquivo CSV
with open(nome_arquivo, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Data de Nascimento", "Dia de Cadastro", "Hora de Cadastro"])  # Cabeçalho
    writer.writerows(dados)
    
print(f"Arquivo {nome_arquivo} criado com sucesso!")

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Ignorar o cabeçalho
        registros = list(reader)
    return registros

# Função para formatar a data no padrão brasileiro
def formatar_data(data_str):
    data_obj = datetime.strptime(data_str, "%Y-%m-%d")
    return data_obj.strftime("%d/%m/%Y")

# Ler o arquivo CSV
registros = ler_arquivo_csv(nome_arquivo)

# Solicitar ao usuário qual registro ele deseja ver
num = int(input("Digite o número do registro que deseja visualizar (1 a 5): "))

# Verificar se o número do registro é válido
if 1 <= num <= len(registros):
    # Obter o registro solicitado
    registro = registros[num - 1]
    
    # Formatar as datas no formato brasileiro
    nome, data_nascimento, dia_cadastro, hora_cadastro = registro
    data_nascimento = formatar_data(data_nascimento)
    dia_cadastro = formatar_data(dia_cadastro)
    
    # Imprimir o registro
    print(f"Registro {num}: {nome}, Nascimento: {data_nascimento}, Cadastro: {dia_cadastro} {hora_cadastro}")
else:
    print("Registro inválido. Por favor, escolha um número entre 1 e 5.")