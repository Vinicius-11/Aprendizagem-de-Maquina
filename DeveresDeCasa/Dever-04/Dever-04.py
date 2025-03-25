import random
import pandas as pd

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

with open("minhas_frutas.txt", "w") as f:
    for fruta in frutas:
        quantidade = random.randint(0, 100)
        f.write(f"{fruta},{quantidade}\n")

dados = {}

with open("minhas_frutas.txt", "r") as f:
    for line in f:
        fruta, quantidade = line.strip().split(",")
        quantidade = int(quantidade)
        
        if fruta in dados:
            dados[fruta] += quantidade
        else:
            dados[fruta] = quantidade

DataFrame = pd.DataFrame(list(dados.items()), columns=["Fruta", "Quantidade"])

print(DataFrame)