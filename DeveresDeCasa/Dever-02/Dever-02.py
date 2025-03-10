#    - Solicitar ao usuário que insira uma frase.
#    - Verificar se a entrada não está vazia e tratar o erro caso necessário. (crie uma nova função no bloco de funções)

def verificar_entrada(entrada):
    if not entrada.strip(): 
        raise ValueError("A entrada não pode ser vazia.")
    return entrada

# MAIOR PALAVRA
def maior_palavra(frase):
    palavras = frase.split()

    maior_palavra = max(palavras, key=len)
    return maior_palavra

# INVERTER CARACTERES E PALAVRAS
def inverter_frase(frase):
    frase_invertida_por_caracteres = frase[::-1]
    
    palavras = frase.split()
    frase_invertida_por_palavras = ' '.join(palavras[::-1])

    return frase_invertida_por_caracteres, frase_invertida_por_palavras

# SOLICITAR A FRASE
def solicitar_frase():
    try:
        frase = input("Digite uma frase: ")
        frase_valida = verificar_entrada(frase)
        print(f"- Frase recebida: {frase_valida}")

#       - Contagem de Caracteres: Calcular o número total de caracteres da frase (incluindo espaços).
        num_caracteres = len(frase)

#       - Maior Palavra: Identificar a palavra com o maior número de caracteres dentre as encontradas.
        palavra_maior = maior_palavra(frase_valida)

#       - Inverter a frase por meio dos caracteres (utilizando slicing com `[::-1]`);  
#       - Inverter a ordem das palavras e reconstruir a frase.
        frase_invertida_por_caracteres, frase_invertida_por_palavras = inverter_frase(frase_valida)

        
#       - Converte a frase para maiúsculas e minúsculas
        frase_maiuscula = frase_valida.upper()
        frase_minuscula = frase_valida.lower()

#       - Cria uma tupla contendo todas as palavras da frase
        tupla_palavras = tuple(frase_valida.split())

        # Exibe os resultados
        print(f"\nResultados:\n")
        print(f"- Número de caracteres da frase: {num_caracteres}")
        print(f"- Número de palavras: {len(frase_valida.split())}")
        print(f"- A palavra com maior comprimento é: {palavra_maior}")
        print(f"- Frase invertida por caracteres: {frase_invertida_por_caracteres}")
        print(f"- Frase invertida por palavras: {frase_invertida_por_palavras}")
        print(f"- Frase em maiúsculas: {frase_maiuscula}")
        print(f"- Frase em minúsculas: {frase_minuscula}")
        print(f"- Tupla de palavras: {tupla_palavras}")


    except ValueError as e:
        print(f"Erro: {e}")

solicitar_frase()