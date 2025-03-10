def verificar_entrada(entrada):
    # Verifica se a entrada está vazia
    if not entrada.strip():  # O método strip() remove espaços em branco no início e no fim
        raise ValueError("A entrada não pode ser vazia.")
    return entrada

def maior_palavra(frase):
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Encontrar a palavra com o maior número de caracteres
    maior_palavra = max(palavras, key=len)
    return maior_palavra

def inversao_frase(frase):
    # Inversão da frase por caracteres
    frase_invertida_por_caracteres = frase[::-1]
    
    # Inversão da ordem das palavras
    palavras = frase.split()
    frase_invertida_por_palavras = ' '.join(palavras[::-1])
    
    return frase_invertida_por_caracteres, frase_invertida_por_palavras

def solicitar_frase():
    try:
        # Solicita ao usuário que insira uma frase
        frase = input("Por favor, insira uma frase: ")
        frase_valida = verificar_entrada(frase)

        # Calcula o número total de caracteres (incluindo espaços)
        numero_de_caracteres = len(frase_valida)
        
        # Identifica a maior palavra
        palavra_maior = maior_palavra(frase_valida)

        # Inverte a frase (por caracteres e por palavras)
        frase_invertida_por_caracteres, frase_invertida_por_palavras = inversao_frase(frase_valida)

        # Converte a frase para maiúsculas e minúsculas
        frase_maiuscula = frase_valida.upper()
        frase_minuscula = frase_valida.lower()

        # Cria uma tupla contendo todas as palavras da frase
        tupla_palavras = tuple(frase_valida.split())

        # Exibe os resultados
        print(f"\nResultados:\n")
        print(f"Número total de caracteres (incluindo espaços): {numero_de_caracteres}")
        print(f"Número de palavras: {len(frase_valida.split())}")
        print(f"A maior palavra é: ( {palavra_maior} ) com {len(palavra_maior)} caracteres")
        print(f"Frase invertida por caracteres: {frase_invertida_por_caracteres}")
        print(f"Frase invertida por palavras: {frase_invertida_por_palavras}")
        print(f"Frase em maiúsculas: {frase_maiuscula}")
        print(f"Frase em minúsculas: {frase_minuscula}")
        print(f"Tupla de palavras: {tupla_palavras}")

    except ValueError as e:
        print(f"Erro: {e}")

# Chama a função para solicitar a frase e exibir os resultados
solicitar_frase()